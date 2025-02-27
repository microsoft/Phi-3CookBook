
# MLflow

[MLflow](https://mlflow.org/) is an open-source platform designed to manage the end-to-end machine learning lifecycle.

![MLFlow](../../../../imgs/02/mlflow/MlFlowmlops.png)

MLFlow is used to manage the ML lifecycle, including experimentation, reproducibility, deployment and a central model registry ML flow currently offers four components. 

- **MLflow Tracking:** Record and query experiements, code, data config and results.
- **MLflow Projects:** Package data science code in a format to reproduce runs on any platform.
- **Mlflow Models:** Deploy machine learning models in diverse serving environments.
- **Model Registry:** Store, annotate and manage models in a central repository.

It includes capabilities for tracking experiments, packaging code into reproducible runs, and sharing and deploying models. MLFlow is integrated into Databricks and supports a variety of ML libraries, making it library-agnostic. It can be used with any machine learning library and in any programming language, as it provides a REST API and CLI for convenience.

![MLFlow](../../../../imgs/02/mlflow/MLflow2.png)

Key features of MLFlow include:

- **Experiment Tracking:** Record and compare parameters and results.
- **Model Management:** Deploy models to various serving and inference platforms.
- **Model Registry:** Collaboratively manage the lifecycle of MLflow Models, including versioning and annotations.
- **Projects:** Package ML code for sharing or production use.
MLFlow also supports the MLOps loop, which includes preparing data, registering and managing models, packaging models for execution, deploying services, and monitoring models. It aims to simplify the process of moving from a prototype to a production workflow, especially in cloud and edge environments.

## E2E Scenario - Building a wrapper and using Phi-3 as an MLFlow model

In this E2E sample we will demonstrate two different approaches to building a wrapper around Phi-3 small language model (SLM) and then running it as an MLFlow model either locally or in the cloud, e.g., in Azure Machine Learning workspace.

![MLFlow](../../../../imgs/02/mlflow/MlFlow1.png)

| Project | Description | Location |
| ------------ | ----------- | -------- |
| Transformer Pipeline | Transformer PIpeline is the easiest option to build a wrapper if you want to use a HuggingFace model with MLFlow’s experimental transformers flavour. | [**TransformerPipeline.ipynb**](../../../../code/06.E2E/E2E_Phi-3-MLflow_TransformerPipeline.ipynb) |
| Custom Python Wrapper | At the time of writing, the transformer pipeline did not support MLFlow wrapper generation for HuggingFace models in ONNX format, even with the experimental optimum Python package. For the cases like this, you can build your custom Python wrapper for MLFlow mode | [**CustomPythonWrapper.ipynb**](../../../../code/06.E2E/E2E_Phi-3-MLflow_CustomPythonWrapper.ipynb) |

## Project: Transformer Pipeline

1. You would require relevant Python packages from MLFlow and HuggingFace:

    ``` Python
    import mlflow
    import transformers
    ```

2. Next, you should initiate a transformer pipeline by referring to the target Phi-3 model in the HuggingFace registry. As can be seen from the _Phi-3-mini-4k-instruct_’s model card, its task is of a “Text Generation” type:

    ``` Python
    pipeline = transformers.pipeline(
        task = "text-generation",
        model = "microsoft/Phi-3-mini-4k-instruct"
    )
    ```

3. You can now save your Phi-3 model’s transformer pipeline into MLFlow format and provide additional details such as the target artifacts path, specific model configuration settings and inference API type:

    ``` Python
    model_info = mlflow.transformers.log_model(
        transformers_model = pipeline,
        artifact_path = "phi3-mlflow-model",
        model_config = model_config,
        task = "llm/v1/chat"
    )
    ```

## Project: Custom Python Wrapper

1. We can utilise here Microsoft's [ONNX Runtime generate() API](https://github.com/microsoft/onnxruntime-genai) for the ONNX model's inference and tokens encoding / decoding. You have to choose _onnxruntime_genai_ package for your target compute, with the below example targeting CPU:

    ``` Python
    import mlflow
    from mlflow.models import infer_signature
    import onnxruntime_genai as og
    ```

1. Our custom class implements two methods: _load_context()_ to initialise the **ONNX model** of Phi-3 Mini 4K Instruct, **generator parameters** and **tokenizer**; and _predict()_ to generate output tokens for the provided prompt:

    ``` Python
    class Phi3Model(mlflow.pyfunc.PythonModel):
        def load_context(self, context):
            # Retrieving model from the artifacts
            model_path = context.artifacts["phi3-mini-onnx"]
            model_options = {
                 "max_length": 300,
                 "temperature": 0.2,         
            }
        
            # Defining the model
            self.phi3_model = og.Model(model_path)
            self.params = og.GeneratorParams(self.phi3_model)
            self.params.set_search_options(**model_options)
            
            # Defining the tokenizer
            self.tokenizer = og.Tokenizer(self.phi3_model)
    
        def predict(self, context, model_input):
            # Retrieving prompt from the input
            prompt = model_input["prompt"][0]
            self.params.input_ids = self.tokenizer.encode(prompt)
    
            # Generating the model's response
            response = self.phi3_model.generate(self.params)
    
            return self.tokenizer.decode(response[0][len(self.params.input_ids):])
    ```

1. You can use now _mlflow.pyfunc.log_model()_ function to generate a custom Python wrapper (in pickle format) for the Phi-3 model, along with the original ONNX model and required dependencies:

    ``` Python
    model_info = mlflow.pyfunc.log_model(
        artifact_path = artifact_path,
        python_model = Phi3Model(),
        artifacts = {
            "phi3-mini-onnx": "cpu_and_mobile/cpu-int4-rtn-block-32-acc-level-4",
        },
        input_example = input_example,
        signature = infer_signature(input_example, ["Run"]),
        extra_pip_requirements = ["torch", "onnxruntime_genai", "numpy"],
    )
    ```

## Signatures of generated MLFlow models

1. In step 3 of the Transformer Pipeline project above, we set the MLFlow model’s task to “_llm/v1/chat_”. Such instruction generates a model’s API wrapper, compatible with OpenAI’s Chat API as shown below:

    ``` Python
    {inputs: 
      ['messages': Array({content: string (required), name: string (optional), role: string (required)}) (required), 'temperature': double (optional), 'max_tokens': long (optional), 'stop': Array(string) (optional), 'n': long (optional), 'stream': boolean (optional)],
    outputs: 
      ['id': string (required), 'object': string (required), 'created': long (required), 'model': string (required), 'choices': Array({finish_reason: string (required), index: long (required), message: {content: string (required), name: string (optional), role: string (required)} (required)}) (required), 'usage': {completion_tokens: long (required), prompt_tokens: long (required), total_tokens: long (required)} (required)],
    params: 
      None}
    ```

1. As a result, you can submit your prompt in the following format:

    ``` Python
    messages = [{"role": "user", "content": "What is the capital of Spain?"}]
    ```

1. Then, use OpenAI API-compatible post-processing, e.g., _response[0][‘choices’][0][‘message’][‘content’]_, to beautify your output to something like this:

    ``` JSON
    Question: What is the capital of Spain?
    
    Answer: The capital of Spain is Madrid. It is the largest city in Spain and serves as the political, economic, and cultural center of the country. Madrid is located in the center of the Iberian Peninsula and is known for its rich history, art, and architecture, including the Royal Palace, the Prado Museum, and the Plaza Mayor.
    
    Usage: {'prompt_tokens': 11, 'completion_tokens': 73, 'total_tokens': 84}
    ```

1. In step 3 of the Custom Python Wrapper project above, we allow the MLFlow package to generate the model’s signature from a given input example. Our MLFlow wrapper's signature will look like this:

    ``` Python
    {inputs: 
      ['prompt': string (required)],
    outputs: 
      [string (required)],
    params: 
      None}
    ```

1. So, our prompt would need to contain "prompt" dictionary key, similar to this:

    ``` Python
    {"prompt": "<|system|>You are a stand-up comedian.<|end|><|user|>Tell me a joke about atom<|end|><|assistant|>",}
    ```

1. The model's output will be provided then in string format:

    ``` JSON
    Alright, here's a little atom-related joke for you!
    
    Why don't electrons ever play hide and seek with protons?
    
    Because good luck finding them when they're always "sharing" their electrons!
    
    Remember, this is all in good fun, and we're just having a little atomic-level humor!
    ```
