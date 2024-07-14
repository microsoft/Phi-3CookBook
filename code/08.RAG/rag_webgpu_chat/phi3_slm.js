import * as ort from 'onnxruntime-web/webgpu';
import { env, AutoTokenizer,pipeline, cos_sim } from '@xenova/transformers';


ort.env.wasm.numThreads = 1;
ort.env.wasm.simd = true;
ort.env.wasm.wasmPaths = document.location.pathname.replace('index.html', '') + 'dist/';

export class Phi3SLM {

    sess = undefined;
    provider = "webgpu";
    profiler = 0;
    verbose = 0;
    dtype = "float16";
    max_tokens = 4000;


    feed = {};
    output_tokens = [];
    eos = 2;
    need_position_ids = true;
    stop = false;
    kv_dims = [];


    //https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx-web/resolve/main/config.json
    phi3_path = "models/Microsoft/Phi-3-mini-4k-instruct-onnx-web/";
    phi3_onnx_data = "model_q4f16.onnx_data";
    onnx_model_path = this.phi3_path + "onnx/model_q4f16.onnx"; //'https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx-web/resolve/main/onnx/model_q4f16.onnx';//this.phi3_path + "onnx/model_q4f16.onnx";
    onnx_model_external_data_path = this.phi3_path + "onnx/model_q4f16.onnx_data";//'https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx-web/resolve/main/onnx/model_q4f16.onnx_data'; 
    onnx_config_path = this.phi3_path + "config.json";  //'https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx-web/resolve/main/config.json'; //this.phi3_path + "config.json";

    constructor() {

        // setup for transformers.js tokenizer
        env.localModelPath = 'models';
        env.allowRemoteModels = 1; // disable remote models
        env.allowLocalModels = 1; // enable local models

    }

    async loadONNX() {


        const opt = {
            executionProviders: [this.provider],
            preferredOutputLocation: {},
        }
        // load onnx config
        const json_bytes = await this.fetchAndCache(this.onnx_config_path);
        let textDecoder = new TextDecoder();
        const model_config = JSON.parse(textDecoder.decode(json_bytes));

        // load onnx model
        const model_bytes = await this.fetchAndCache(this.onnx_model_path);
        const externaldata = await this.fetchAndCache(this.onnx_model_external_data_path);
        let modelSize = model_bytes.byteLength;
        if (externaldata) {
            modelSize += externaldata.byteLength;
        }


        for (let i = 0; i < model_config.num_hidden_layers; ++i) {
            opt.preferredOutputLocation[`present.${i}.key`] = 'gpu-buffer';
            opt.preferredOutputLocation[`present.${i}.value`] = 'gpu-buffer';
        }


        opt.externalData = [
            {
                data: externaldata,
                path: 'model_q4f16.onnx_data',
            },
        ]


        // opt.logSeverityLevel = 0;
        // opt.logVerbosityLevel = 0;
        // ort.env.logLevel = "verbose";


        ort.env.webgpu.profiling = {};


        // opt.enableProfiling = true;
        // ort.env.webgpu.profilingMode = 'default';
        // ort.env.webgpu.profiling.mode = 'default';


        this.sess = await ort.InferenceSession.create(model_bytes, opt);
        this.eos = model_config.eos_token_id;
        this.kv_dims = [1, model_config.num_key_value_heads, 0, model_config.hidden_size / model_config.num_attention_heads];
        this.dtype = "float16";
        this.num_layers = model_config.num_hidden_layers;
        this.initilize_feed();
    }


    async generate(tokens, callback, options) {
        const max_tokens = options.max_tokens || 256;
        const feed = this.feed;
        const input_ids = new ort.Tensor('int64', BigInt64Array.from(tokens.map(BigInt)), [1, tokens.length]);
        feed['input_ids'] = input_ids;
        this.stop = false;

        this.output_tokens.push(...input_ids.data);

        let last_token = 0n;
        let seqlen = this.output_tokens.length;
        const input_len = input_ids.size;

        if (this.need_position_ids) {
            feed['position_ids'] = new ort.Tensor('int64', BigInt64Array.from({ length: input_len }, (_, i) => BigInt(seqlen - input_len + i)), [1, input_len]);
        }

        while (last_token != this.eos && last_token != 32007 && seqlen < max_tokens && !this.stop) {
            seqlen = this.output_tokens.length;
            feed['attention_mask'] = new ort.Tensor('int64', BigInt64Array.from({ length: seqlen }, () => 1n), [1, seqlen]);
            const outputs = await this.sess.run(feed);
            last_token = BigInt(this.argmax(outputs.logits));
            this.output_tokens.push(last_token);
            if (callback && !this.profiler) {
                callback(this.output_tokens);
            }
            this.update_kv_cache(feed, outputs);
            feed['input_ids'] = new ort.Tensor('int64', BigInt64Array.from([last_token]), [1, 1]);
            if (this.need_position_ids) {
                feed['position_ids'] = new ort.Tensor('int64', BigInt64Array.from([BigInt(seqlen)]), [1, 1]);
            }
        }
        if (this.profiler) {
            this.sess.endProfiling();
        }
        return this.output_tokens;
    }

    initilize_feed() {
        const feed = this.feed;

        // dispose of previous gpu buffers
        for (const name in feed) {
            const t = feed[name];
            if (t.location === 'gpu-buffer') {
                t.dispose();
            }
        }
        this.feed = {};
        // key value cache is zero copy, just pass gpu buffer as referece
        const empty = (this.dtype === "float16") ? new Uint16Array() : [];
        for (let i = 0; i < this.num_layers; ++i) {
            this.feed[`past_key_values.${i}.key`] = new ort.Tensor(this.dtype, empty, this.kv_dims)
            this.feed[`past_key_values.${i}.value`] = new ort.Tensor(this.dtype, empty, this.kv_dims)
        }
        this.output_tokens = [];
    }

    //
    // poor mens argmax
    //xe
    argmax(t) {
        const arr = t.data;
        const start = t.dims[2] * (t.dims[1] - 1);
        let max = arr[start];
        let maxidx = 0;

        for (let i = 0; i < t.dims[2]; i++) {
            const val = arr[i + start];
            if (!isFinite(val)) {
                throw new Error("found infinitive in logits");
            }
            if (val > max) {
                max = arr[i + start];
                maxidx = i;
            }
        }
        return maxidx;
    }

    //
    // update key value cache
    //
    update_kv_cache(feed, outputs) {
        for (const name in outputs) {
            if (name.startsWith('present')) {
                let newName = name.replace('present', 'past_key_values');
                // dispose previous gpu buffers
                const t = feed[newName];
                if (t.location === 'gpu-buffer') {
                    t.dispose();
                }
                feed[newName] = outputs[name];
            }
        }
    }

    //
    // tell generate to stop()
    //
    abort() {
        this.stop = true;
    }


    async fetchAndCache(url) {
        try {
            const cache = await caches.open("onnx");
            let cachedResponse = await cache.match(url);
            if (cachedResponse === undefined) {
                console.log(`${url} (network)`);
                const buffer = await fetch(url).then(response => response.arrayBuffer());
                try {
                    await cache.put(url, new Response(buffer));
                } catch (error) {
                    console.error(error);
                }
                return buffer;
            }
            console.log(`${url} (cached)`);
            const data = await cachedResponse.arrayBuffer();
            return data;
        } catch (error) {
            console.log(`can't fetch ${url}`);
            throw error;
        }
    }

}