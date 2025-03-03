# MLflow

[MLflow](https://mlflow.org/) är en öppen plattform utformad för att hantera hela livscykeln för maskininlärning.

![MLFlow](../../../../../../translated_images/MlFlowmlops.e5d74ef39e988d267f5da3174105d728e556b25cee7d686689174acb1f07a11a.sv.png)

MLFlow används för att hantera ML-livscykeln, inklusive experimentering, reproducerbarhet, distribution och ett centralt modellregister. MLFlow erbjuder för närvarande fyra komponenter:

- **MLflow Tracking:** Spåra och fråga experiment, kod, datakonfiguration och resultat.
- **MLflow Projects:** Paketera data science-kod i ett format som kan köras på vilken plattform som helst.
- **Mlflow Models:** Distribuera maskininlärningsmodeller i olika servermiljöer.
- **Model Registry:** Lagra, kommentera och hantera modeller i ett centralt arkiv.

Plattformen innehåller funktioner för att spåra experiment, paketera kod till reproducerbara körningar samt dela och distribuera modeller. MLFlow är integrerat i Databricks och stöder olika ML-bibliotek, vilket gör det bibliotek-oberoende. Det kan användas med vilket maskininlärningsbibliotek som helst och på vilket programmeringsspråk som helst, eftersom det erbjuder ett REST API och CLI för bekvämlighet.

![MLFlow](../../../../../../translated_images/MLflow2.74e3f1a430b83b5379854d81f4d2d125b6e5a0f35f46b57625761d1f0597bc53.sv.png)

Nyckelfunktioner i MLFlow inkluderar:

- **Experiment Tracking:** Registrera och jämför parametrar och resultat.
- **Model Management:** Distribuera modeller till olika plattformar för servering och inferens.
- **Model Registry:** Hantera MLFlow-modellers livscykel tillsammans, inklusive versionshantering och kommentarer.
- **Projects:** Paketera ML-kod för delning eller produktionsanvändning.

MLFlow stöder också MLOps-cykeln, som inkluderar att förbereda data, registrera och hantera modeller, paketera modeller för körning, distribuera tjänster och övervaka modeller. Målet är att förenkla processen från prototyp till produktionsflöde, särskilt i moln- och edge-miljöer.

## E2E-scenario – Bygga en wrapper och använda Phi-3 som en MLFlow-modell

I detta E2E-exempel kommer vi att demonstrera två olika metoder för att bygga en wrapper kring Phi-3:s lilla språkmodell (SLM) och sedan köra den som en MLFlow-modell antingen lokalt eller i molnet, t.ex. i Azure Machine Learning-arbetsytan.

![MLFlow](../../../../../../translated_images/MlFlow1.03b29de8b4a8f3706a3e7b229c94a81ece6e3ba983c78592ed332f3ef6efcfe0.sv.png)

| Projekt | Beskrivning | Plats |
| ------------ | ----------- | -------- |
| Transformer Pipeline | Transformer Pipeline är det enklaste alternativet för att bygga en wrapper om du vill använda en HuggingFace-modell med MLFlow:s experimentella transformers-smak. | [**TransformerPipeline.ipynb**](../../../../../../code/06.E2E/E2E_Phi-3-MLflow_TransformerPipeline.ipynb) |
| Custom Python Wrapper | Vid tidpunkten för skrivandet stödde inte transformer-pipelinen generering av MLFlow-wrapper för HuggingFace-modeller i ONNX-format, inte ens med det experimentella optimum Python-paketet. För sådana fall kan du bygga din egen anpassade Python-wrapper för MLFlow-läge. | [**CustomPythonWrapper.ipynb**](../../../../../../code/06.E2E/E2E_Phi-3-MLflow_CustomPythonWrapper.ipynb) |

## Projekt: Transformer Pipeline

1. Du behöver relevanta Python-paket från MLFlow och HuggingFace:

    ``` Python
    import mlflow
    import transformers
    ```

2. Nästa steg är att initiera en transformer-pipeline genom att hänvisa till den målsatta Phi-3-modellen i HuggingFace-registret. Som framgår av modellkortet för _Phi-3-mini-4k-instruct_ är dess uppgift av typen ”Text Generation”:

    ``` Python
    pipeline = transformers.pipeline(
        task = "text-generation",
        model = "microsoft/Phi-3-mini-4k-instruct"
    )
    ```

3. Du kan nu spara Phi-3-modellens transformer-pipeline i MLFlow-format och ange ytterligare detaljer som mål för artefaktsökväg, specifika modellkonfigurationsinställningar och typ av inferens-API:

    ``` Python
    model_info = mlflow.transformers.log_model(
        transformers_model = pipeline,
        artifact_path = "phi3-mlflow-model",
        model_config = model_config,
        task = "llm/v1/chat"
    )
    ```

## Projekt: Custom Python Wrapper

1. Här kan vi använda Microsofts [ONNX Runtime generate() API](https://github.com/microsoft/onnxruntime-genai) för inferens av ONNX-modellen samt kodning/avkodning av tokens. Du måste välja _onnxruntime_genai_-paketet för din målmiljö, med nedanstående exempel som riktar sig till CPU:

    ``` Python
    import mlflow
    from mlflow.models import infer_signature
    import onnxruntime_genai as og
    ```

1. Vår anpassade klass implementerar två metoder: _load_context()_ för att initiera **ONNX-modellen** för Phi-3 Mini 4K Instruct, **generatorparametrar** och **tokenizer**; samt _predict()_ för att generera utgångstokens för den angivna prompten:

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

1. Du kan nu använda funktionen _mlflow.pyfunc.log_model()_ för att generera en anpassad Python-wrapper (i pickle-format) för Phi-3-modellen, tillsammans med den ursprungliga ONNX-modellen och nödvändiga beroenden:

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

## Signaturer för genererade MLFlow-modeller

1. I steg 3 av Transformer Pipeline-projektet ovan ställer vi in MLFlow-modellens uppgift till ”_llm/v1/chat_”. En sådan instruktion genererar en API-wrapper för modellen som är kompatibel med OpenAI:s Chat API enligt nedan:

    ``` Python
    {inputs: 
      ['messages': Array({content: string (required), name: string (optional), role: string (required)}) (required), 'temperature': double (optional), 'max_tokens': long (optional), 'stop': Array(string) (optional), 'n': long (optional), 'stream': boolean (optional)],
    outputs: 
      ['id': string (required), 'object': string (required), 'created': long (required), 'model': string (required), 'choices': Array({finish_reason: string (required), index: long (required), message: {content: string (required), name: string (optional), role: string (required)} (required)}) (required), 'usage': {completion_tokens: long (required), prompt_tokens: long (required), total_tokens: long (required)} (required)],
    params: 
      None}
    ```

1. Som resultat kan du skicka in din prompt i följande format:

    ``` Python
    messages = [{"role": "user", "content": "What is the capital of Spain?"}]
    ```

1. Använd sedan OpenAI API-kompatibel efterbearbetning, t.ex. _response[0][‘choices’][0][‘message’][‘content’]_, för att snygga till ditt resultat till något i stil med detta:

    ``` JSON
    Question: What is the capital of Spain?
    
    Answer: The capital of Spain is Madrid. It is the largest city in Spain and serves as the political, economic, and cultural center of the country. Madrid is located in the center of the Iberian Peninsula and is known for its rich history, art, and architecture, including the Royal Palace, the Prado Museum, and the Plaza Mayor.
    
    Usage: {'prompt_tokens': 11, 'completion_tokens': 73, 'total_tokens': 84}
    ```

1. I steg 3 av Custom Python Wrapper-projektet ovan låter vi MLFlow-paketet generera modellens signatur från ett givet exempel på indata. Signaturen för vår MLFlow-wrapper kommer att se ut så här:

    ``` Python
    {inputs: 
      ['prompt': string (required)],
    outputs: 
      [string (required)],
    params: 
      None}
    ```

1. Så vår prompt behöver innehålla nyckeln "prompt" i dictionary-format, liknande detta:

    ``` Python
    {"prompt": "<|system|>You are a stand-up comedian.<|end|><|user|>Tell me a joke about atom<|end|><|assistant|>",}
    ```

1. Modellens utdata kommer då att tillhandahållas i strängformat:

    ``` JSON
    Alright, here's a little atom-related joke for you!
    
    Why don't electrons ever play hide and seek with protons?
    
    Because good luck finding them when they're always "sharing" their electrons!
    
    Remember, this is all in good fun, and we're just having a little atomic-level humor!
    ```

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-baserade maskinöversättningstjänster. Även om vi strävar efter noggrannhet, vänligen notera att automatiserade översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.