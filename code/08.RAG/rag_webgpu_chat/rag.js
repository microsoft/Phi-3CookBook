
import { Phi3SLM } from './phi3_slm.js';
import { env, AutoTokenizer,pipeline, cos_sim } from '@xenova/transformers';


//
// class for RAG
//

export class RAG{

    extractor = undefined;
    phi3_slm = undefined;
    tokenizer = undefined;

    constructor(){
        this.phi3_slm = new Phi3SLM();
    }
    //
    // Init Phi-3 Model
    //
    async InitPhi3SLM(){



        this.tokenizer = await AutoTokenizer.from_pretrained("Microsoft/Phi-3-mini-4k-instruct-onnx-web");


         await this.phi3_slm.loadONNX();

        await this.load('Xenova/jina-embeddings-v2-base-en');
        // await this.phi3_slm.loadONNX();
    }
    //
    //
    //
    async loadONNX(){
        await this.phi3_slm.loadONNX();
    }
    //
    // Load embedding model
    //
    async load(embeddd_model) {

        this.extractor = await pipeline('feature-extraction', embeddd_model,
            { quantized: false } 
        );
        
    }
    //
    // Embedding Algorithm
    //
    async getEmbeddings(query,kbContents) { 

        const question = query;

        let sim_result = [];

        for(const content of kbContents) {
            const output = await this.extractor([question, content], { pooling: 'mean' });
            const sim = cos_sim(output[0].data, output[1].data);
            sim_result.push({ content, sim });
        }

        sim_result.sort((a, b) => b.sim - a.sim);

        var answer = '';

        console.log(sim_result);

        answer = sim_result[0].content;

        return answer;
    }
    //
    // Generate Summary Content
    //
    async generateSummaryContent(prompt) {

        const { input_ids } = await this.tokenizer(prompt, { return_tensor: false, padding: true, truncation: true });



        // clear caches 
        // TODO: use kv_cache for continuation
        this.phi3_slm.initilize_feed();

        const start_timer = performance.now();
        const output_index = this.phi3_slm.output_tokens.length + input_ids.length;
        let answer_result = '';
        const output_tokens = await this.phi3_slm.generate(input_ids, (output_tokens) => {
            if (output_tokens.length == input_ids.length + 1) {
            // time to first token
            const took = (performance.now() - start_timer) / 1000;
            console.log(`time to first token in ${took.toFixed(1)}sec, ${input_ids.length} tokens`);
            }
            answer_result = this.token_to_text(this.tokenizer, output_tokens, output_index);
        }, { max_tokens: 4000});

        const took = (performance.now() - start_timer) / 1000;
        // cb(this.token_to_text(this.tokenizer, output_tokens, output_index));
        const seqlen = output_tokens.length - output_index;
        console.log(`${seqlen} tokens in ${took.toFixed(1)}sec, ${(seqlen / took).toFixed(2)} tokens/sec`);
        return answer_result;
    }
    //
    // Generate Embeddings Content
    //
    async generateEmbeddingsContent(prompt) {


        const { input_ids } = await this.tokenizer(prompt, { return_tensor: false, padding: true, truncation: true });
    
        // clear caches 
        // TODO: use kv_cache for continuation
        this.phi3_slm.initilize_feed();

        const start_timer = performance.now();
        const output_index = this.phi3_slm.output_tokens.length + input_ids.length;
        let json_result = '';
        const output_tokens = await this.phi3_slm.generate(input_ids, (output_tokens) => {
            if (output_tokens.length == input_ids.length + 1) {
            // time to first token
            const took = (performance.now() - start_timer) / 1000;
            console.log(`time to first token in ${took.toFixed(1)}sec, ${input_ids.length} tokens`);
            }
            json_result = this.token_to_text(this.tokenizer, output_tokens, output_index);
        }, { max_tokens: 4000 });

        const took = (performance.now() - start_timer) / 1000;
        // cb(token_to_text(tokenizer, output_tokens, output_index));
        const seqlen = output_tokens.length - output_index;
        console.log(`${seqlen} tokens in ${took.toFixed(1)}sec, ${(seqlen / took).toFixed(2)} tokens/sec`);

        const json_result_index = json_result.indexOf(']');

        json_result = json_result.substring(0,json_result_index+1);

        return json_result;
    }
    //
    // Generate Answer
    //
    async generateAnswer(prompt, cb) {  
        
        
        // let prompt = (continuation) ? query : `<|system|>\nYou are a friendly assistant. Help me summarize answer of the knowledge points<|end|>\n<|user|>\n${answer}<|end|>\n<|assistant|>\n`;

        const { input_ids } = await this.tokenizer(prompt, { return_tensor: false, padding: true, truncation: true });
    
    
    
        // clear caches 
        // TODO: use kv_cache for continuation
        this.phi3_slm.initilize_feed();
    
        const start_timer = performance.now();
        const output_index = this.phi3_slm.output_tokens.length + input_ids.length;
        const output_tokens = await this.phi3_slm.generate(input_ids, (output_tokens) => {
        if (output_tokens.length == input_ids.length + 1) {
            // time to first token
            const took = (performance.now() - start_timer) / 1000;
            console.log(`time to first token in ${took.toFixed(1)}sec, ${input_ids.length} tokens`);
        }
        cb(this.token_to_text(tokenizer, output_tokens, output_index));
        }, { max_tokens: config.max_tokens });
    
        const took = (performance.now() - start_timer) / 1000;
        cb(this.token_to_text(tokenizer, output_tokens, output_index));
        const seqlen = output_tokens.length - output_index;
        console.log(`${seqlen} tokens in ${took.toFixed(1)}sec, ${(seqlen / took).toFixed(2)} tokens/sec`);
        // return answer;
    }
    
    token_to_text(tokenizer, tokens, startidx) {
        const txt = this.tokenizer.decode(tokens.slice(startidx), { skip_special_tokens: true, });
        return txt;
    }

}