## How use chat-completion components from the Azure ML system registry to fine tune a model

In this example we will undertake fine tuning of the Phi-3-mini-4k-instruct model to complete a conversation between 2 people using ultrachat_200k dataset.

![MLFineTune](../../imgs/03/ft/MLFineTune.png)

The example will show you how to undertake fine tuning using the Azure ML SDK and Python and then deploy the fine tuned model to an online endpoint for real time inference.

### Training data

We will use the ultrachat_200k dataset. This is a heavily filtered version of the UltraChat dataset and was used to train Zephyr-7B-β, a state of the art 7b chat model.

### Model

We will use the Phi-3-mini-4k-instruct model to show how user can finetune a model for chat-completion task. If you opened this notebook from a specific model card, remember to replace the specific model name.

### Tasks

- Pick a model to fine tune.
- Pick and explore training data.
- Configure the fine tuning job.
- Run the fine tuning job.
- Review training and evaluation metrics.
- Register the fine tuned model.
- Deploy the fine tuned model for real time inference.
- Clean up resources.

## 1. Setup pre-requisites

- Install dependencies
- Connect to AzureML Workspace. Learn more at set up SDK authentication. Replace <WORKSPACE_NAME>, <RESOURCE_GROUP> and <SUBSCRIPTION_ID> below.
- Connect to azureml system registry
- Set an optional experiment name
- Check or create compute.

> [!NOTE]
> Requirements a single GPU node can have multiple GPU cards. For example, in one node of Standard_NC24rs_v3 there are 4 NVIDIA V100 GPUs while in Standard_NC12s_v3, there are 2 NVIDIA V100 GPUs. Refer to the docs for this information. The number of GPU cards per node is set in the param gpus_per_node below. Setting this value correctly will ensure utilization of all GPUs in the node. The recommended GPU compute SKUs can be found here and here.

### Python Libraries

Install dependencies by running below cell. This is not an optional step if running in a new environment.

```bash
pip install azure-ai-ml
pip install azure-identity
pip install datasets==2.9.0
pip install mlflow
pip install azureml-mlflow
```

### Interacting with Azure ML

1. This Python script is used to interact with Azure Machine Learning (Azure ML) service. Here's a breakdown of what it does:

    - It imports necessary modules from the azure.ai.ml, azure.identity, and azure.ai.ml.entities packages. It also imports the time module.

    - It tries to authenticate using DefaultAzureCredential(), which provides a simplified authentication experience to quickly start developing applications run in the Azure cloud. If this fails, it falls back to InteractiveBrowserCredential(), which provides an interactive login prompt.

    - It then tries to create an MLClient instance using the from_config method, which reads the configuration from the default config file (config.json). If this fails, it creates an MLClient instance by manually providing the subscription_id, resource_group_name, and workspace_name.

    - It creates another MLClient instance, this time for the Azure ML registry named "azureml". This registry is where models, fine-tuning pipelines, and environments are stored.

    - It sets the experiment_name to "chat_completion_Phi-3-mini-4k-instruct".

    - It generates a unique timestamp by converting the current time (in seconds since the epoch, as a floating point number) to an integer and then to a string. This timestamp can be used for creating unique names and versions.

    ```python
    # Import necessary modules from Azure ML and Azure Identity
    from azure.ai.ml import MLClient
    from azure.identity import (
        DefaultAzureCredential,
        InteractiveBrowserCredential,
    )
    from azure.ai.ml.entities import AmlCompute
    import time  # Import time module
    
    # Try to authenticate using DefaultAzureCredential
    try:
        credential = DefaultAzureCredential()
        credential.get_token("https://management.azure.com/.default")
    except Exception as ex:  # If DefaultAzureCredential fails, use InteractiveBrowserCredential
        credential = InteractiveBrowserCredential()
    
    # Try to create an MLClient instance using the default config file
    try:
        workspace_ml_client = MLClient.from_config(credential=credential)
    except:  # If that fails, create an MLClient instance by manually providing the details
        workspace_ml_client = MLClient(
            credential,
            subscription_id="<SUBSCRIPTION_ID>",
            resource_group_name="<RESOURCE_GROUP>",
            workspace_name="<WORKSPACE_NAME>",
        )
    
    # Create another MLClient instance for the Azure ML registry named "azureml"
    # This registry is where models, fine-tuning pipelines, and environments are stored
    registry_ml_client = MLClient(credential, registry_name="azureml")
    
    # Set the experiment name
    experiment_name = "chat_completion_Phi-3-mini-4k-instruct"
    
    # Generate a unique timestamp that can be used for names and versions that need to be unique
    timestamp = str(int(time.time()))
    ```

## 2. Pick a foundation model to fine tune

1. Phi-3-mini-4k-instruct is a 3.8B parameters, lightweight, state-of-the-art open model built upon datasets used for Phi-2. The model belongs to the Phi-3 model family, and the Mini version comes in two variants 4K and 128K which is the context length (in tokens) it can support, we need to finetune the model for our specific purpose in order to use it. You can browse these models in the Model Catalog in the AzureML Studio, filtering by the chat-completion task. In this example, we use the Phi-3-mini-4k-instruct model. If you have opened this notebook for a different model, replace the model name and version accordingly.

    > [!NOTE]
    > the model id property of the model. This will be passed as input to the fine tuning job. This is also available as the Asset ID field in model details page in AzureML Studio Model Catalog.

2. This Python script is interacting with Azure Machine Learning (Azure ML) service. Here's a breakdown of what it does:

    - It sets the model_name to "Phi-3-mini-4k-instruct".

    - It uses the get method of the models property of the registry_ml_client object to retrieve the latest version of the model with the specified name from the Azure ML registry. The get method is called with two arguments: the name of the model and a label specifying that the latest version of the model should be retrieved.

    - It prints a message to the console indicating the name, version, and id of the model that will be used for fine-tuning. The format method of the string is used to insert the name, version, and id of the model into the message. The name, version, and id of the model are accessed as properties of the foundation_model object.

    ```python
    # Set the model name
    model_name = "Phi-3-mini-4k-instruct"
    
    # Get the latest version of the model from the Azure ML registry
    foundation_model = registry_ml_client.models.get(model_name, label="latest")
    
    # Print the model name, version, and id
    # This information is useful for tracking and debugging
    print(
        "\n\nUsing model name: {0}, version: {1}, id: {2} for fine tuning".format(
            foundation_model.name, foundation_model.version, foundation_model.id
        )
    )
    ```

## 3. Create a compute to be used with the job

The finetune job works ONLY with GPU compute. The size of the compute depends on how big the model is and in most cases it becomes tricky to identify the right compute for the job. In this cell, we guide the user to select the right compute for the job.

> [!NOTE]
> The computes listed below work with the most optimized configuration. Any changes to the configuration might lead to Cuda Out Of Memory error. In such cases, try to upgrade the compute to a bigger compute size.

> [!NOTE]
> While selecting the compute_cluster_size below, make sure the compute is available in your resource group. If a particular compute is not available you can make a request to get access to the compute resources.

### Checking Model for Fine Tuning Support

1. This Python script is interacting with an Azure Machine Learning (Azure ML) model. Here's a breakdown of what it does:

    - It imports the ast module, which provides functions to process trees of the Python abstract syntax grammar.

    - It checks if the foundation_model object (which represents a model in Azure ML) has a tag named finetune_compute_allow_list. Tags in Azure ML are key-value pairs that you can create and use to filter and sort models.

    - If the finetune_compute_allow_list tag is present, it uses the ast.literal_eval function to safely parse the tag's value (a string) into a Python list. This list is then assigned to the computes_allow_list variable. It then prints a message indicating that a compute should be created from the list.

    - If the finetune_compute_allow_list tag is not present, it sets computes_allow_list to None and prints a message indicating that the finetune_compute_allow_list tag is not part of the model's tags.

    - In summary, this script is checking for a specific tag in the model's metadata, converting the tag's value to a list if it exists, and providing feedback to the user accordingly.

    ```python
    # Import the ast module, which provides functions to process trees of the Python abstract syntax grammar
    import ast
    
    # Check if the 'finetune_compute_allow_list' tag is present in the model's tags
    if "finetune_compute_allow_list" in foundation_model.tags:
        # If the tag is present, use ast.literal_eval to safely parse the tag's value (a string) into a Python list
        computes_allow_list = ast.literal_eval(
            foundation_model.tags["finetune_compute_allow_list"]
        )  # convert string to python list
        # Print a message indicating that a compute should be created from the list
        print(f"Please create a compute from the above list - {computes_allow_list}")
    else:
        # If the tag is not present, set computes_allow_list to None
        computes_allow_list = None
        # Print a message indicating that the 'finetune_compute_allow_list' tag is not part of the model's tags
        print("`finetune_compute_allow_list` is not part of model tags")
    ```

### Checking Compute Instance

1. This Python script is interacting with Azure Machine Learning (Azure ML) service and performing several checks on a compute instance. Here's a breakdown of what it does:

    - It tries to retrieve the compute instance with the name stored in compute_cluster from the Azure ML workspace. If the compute instance's provisioning state is "failed", it raises a ValueError.

    - It checks if computes_allow_list is not None. If it's not, it converts all the compute sizes in the list to lowercase and checks if the size of the current compute instance is in the list. If it's not, it raises a ValueError.

    - If computes_allow_list is None, it checks if the size of the compute instance is in a list of unsupported GPU VM sizes. If it is, it raises a ValueError.

    - It retrieves a list of all available compute sizes in the workspace. It then iterates over this list, and for each compute size, it checks if its name matches the size of the current compute instance. If it does, it retrieves the number of GPUs for that compute size and sets gpu_count_found to True.

    - If gpu_count_found is True, it prints the number of GPUs in the compute instance. If gpu_count_found is False, it raises a ValueError.

    - In summary, this script is performing several checks on a compute instance in an Azure ML workspace, including checking its provisioning state, its size against an allow list or a deny list, and the number of GPUs it has.
    
    ```python
    # Print the exception message
    print(e)
    # Raise a ValueError if the compute size is not available in the workspace
    raise ValueError(
        f"WARNING! Compute size {compute_cluster_size} not available in workspace"
    )
    
    # Retrieve the compute instance from the Azure ML workspace
    compute = workspace_ml_client.compute.get(compute_cluster)
    # Check if the provisioning state of the compute instance is "failed"
    if compute.provisioning_state.lower() == "failed":
        # Raise a ValueError if the provisioning state is "failed"
        raise ValueError(
            f"Provisioning failed, Compute '{compute_cluster}' is in failed state. "
            f"please try creating a different compute"
        )
    
    # Check if computes_allow_list is not None
    if computes_allow_list is not None:
        # Convert all compute sizes in computes_allow_list to lowercase
        computes_allow_list_lower_case = [x.lower() for x in computes_allow_list]
        # Check if the size of the compute instance is in computes_allow_list_lower_case
        if compute.size.lower() not in computes_allow_list_lower_case:
            # Raise a ValueError if the size of the compute instance is not in computes_allow_list_lower_case
            raise ValueError(
                f"VM size {compute.size} is not in the allow-listed computes for finetuning"
            )
    else:
        # Define a list of unsupported GPU VM sizes
        unsupported_gpu_vm_list = [
            "standard_nc6",
            "standard_nc12",
            "standard_nc24",
            "standard_nc24r",
        ]
        # Check if the size of the compute instance is in unsupported_gpu_vm_list
        if compute.size.lower() in unsupported_gpu_vm_list:
            # Raise a ValueError if the size of the compute instance is in unsupported_gpu_vm_list
            raise ValueError(
                f"VM size {compute.size} is currently not supported for finetuning"
            )
    
    # Initialize a flag to check if the number of GPUs in the compute instance has been found
    gpu_count_found = False
    # Retrieve a list of all available compute sizes in the workspace
    workspace_compute_sku_list = workspace_ml_client.compute.list_sizes()
    available_sku_sizes = []
    # Iterate over the list of available compute sizes
    for compute_sku in workspace_compute_sku_list:
        available_sku_sizes.append(compute_sku.name)
        # Check if the name of the compute size matches the size of the compute instance
        if compute_sku.name.lower() == compute.size.lower():
            # If it does, retrieve the number of GPUs for that compute size and set gpu_count_found to True
            gpus_per_node = compute_sku.gpus
            gpu_count_found = True
    # If gpu_count_found is True, print the number of GPUs in the compute instance
    if gpu_count_found:
        print(f"Number of GPU's in compute {compute.size}: {gpus_per_node}")
    else:
        # If gpu_count_found is False, raise a ValueError
        raise ValueError(
            f"Number of GPU's in compute {compute.size} not found. Available skus are: {available_sku_sizes}."
            f"This should not happen. Please check the selected compute cluster: {compute_cluster} and try again."
        )
    ```

## 4. Pick the dataset for fine-tuning the model

1. We use the ultrachat_200k dataset. The dataset has four splits, suitable for Supervised fine-tuning (sft).
Generation ranking (gen). The number of examples per split is shown as follows:

    ```bash
    train_sft test_sft  train_gen  test_gen
    207865  23110  256032  28304
    ```

1. The next few cells show basic data preparation for fine tuning:

### Visualize some data rows

We want this sample to run quickly, so save train_sft, test_sft files containing 5% of the already trimmed rows. This means the fine tuned model will have lower accuracy, hence it should not be put to real-world use.
The download-dataset.py is used to download the ultrachat_200k dataset and transform the dataset into finetune pipeline component consumable format. Also as the dataset is large, hence we here have only part of the dataset.

1. Running the below script only downloads 5% of the data. This can be increased by changing dataset_split_pc parameter to desired percenetage.

    > [!NOTE]
    > Some language models have different language codes and hence the column names in the dataset should reflect the same.

1. Here is an example of how the data should look like
The chat-completion dataset is stored in parquet format with each entry using the following schema:

    - This is a JSON (JavaScript Object Notation) document, which is a popular data interchange format. It's not executable code, but a way to store and transport data. Here's a breakdown of its structure:

    - "prompt": This key holds a string value that represents a task or question posed to an AI assistant.

    - "messages": This key holds an array of objects. Each object represents a message in a conversation between a user and an AI assistant. Each message object has two keys:

    - "content": This key holds a string value that represents the content of the message.
    - "role": This key holds a string value that represents the role of the entity that sent the message. It can be either "user" or "assistant".
    - "prompt_id": This key holds a string value that represents a unique identifier for the prompt.

1. In this specific JSON document, a conversation is represented where a user asks an AI assistant to create a protagonist for a dystopian story. The assistant responds, and the user then asks for more details. The assistant agrees to provide more details. The entire conversation is associated with a specific prompt id.

    ```python
    {
        // The task or question posed to an AI assistant
        "prompt": "Create a fully-developed protagonist who is challenged to survive within a dystopian society under the rule of a tyrant. ...",
        
        // An array of objects, each representing a message in a conversation between a user and an AI assistant
        "messages":[
            {
                // The content of the user's message
                "content": "Create a fully-developed protagonist who is challenged to survive within a dystopian society under the rule of a tyrant. ...",
                // The role of the entity that sent the message
                "role": "user"
            },
            {
                // The content of the assistant's message
                "content": "Name: Ava\n\n Ava was just 16 years old when the world as she knew it came crashing down. The government had collapsed, leaving behind a chaotic and lawless society. ...",
                // The role of the entity that sent the message
                "role": "assistant"
            },
            {
                // The content of the user's message
                "content": "Wow, Ava's story is so intense and inspiring! Can you provide me with more details.  ...",
                // The role of the entity that sent the message
                "role": "user"
            }, 
            {
                // The content of the assistant's message
                "content": "Certainly! ....",
                // The role of the entity that sent the message
                "role": "assistant"
            }
        ],
        
        // A unique identifier for the prompt
        "prompt_id": "d938b65dfe31f05f80eb8572964c6673eddbd68eff3db6bd234d7f1e3b86c2af"
    }
    ```

### Download Data

1. This Python script is used to download a dataset using a helper script named download-dataset.py. Here's a breakdown of what it does:

    - It imports the os module, which provides a portable way of using operating system dependent functionality.

    - It uses the os.system function to run the download-dataset.py script in the shell with specific command-line arguments. The arguments specify the dataset to download (HuggingFaceH4/ultrachat_200k), the directory to download it to (ultrachat_200k_dataset), and the percentage of the dataset to split (5). The os.system function returns the exit status of the command it executed; this status is stored in the exit_status variable.

    - It checks if exit_status is not 0. In Unix-like operating systems, an exit status of 0 usually indicates that a command has succeeded, while any other number indicates an error. If exit_status is not 0, it raises an Exception with a message indicating that there was an error downloading the dataset.

    - In summary, this script is running a command to download a dataset using a helper script, and it raises an exception if the command fails.
    
    ```python
    # Import the os module, which provides a way of using operating system dependent functionality
    import os
    
    # Use the os.system function to run the download-dataset.py script in the shell with specific command-line arguments
    # The arguments specify the dataset to download (HuggingFaceH4/ultrachat_200k), the directory to download it to (ultrachat_200k_dataset), and the percentage of the dataset to split (5)
    # The os.system function returns the exit status of the command it executed; this status is stored in the exit_status variable
    exit_status = os.system(
        "python ./download-dataset.py --dataset HuggingFaceH4/ultrachat_200k --download_dir ultrachat_200k_dataset --dataset_split_pc 5"
    )
    
    # Check if exit_status is not 0
    # In Unix-like operating systems, an exit status of 0 usually indicates that a command has succeeded, while any other number indicates an error
    # If exit_status is not 0, raise an Exception with a message indicating that there was an error downloading the dataset
    if exit_status != 0:
        raise Exception("Error downloading dataset")
    ```

### Loading Data into a DataFrame

1. This Python script is loading a JSON Lines file into a pandas DataFrame and displaying the first 5 rows. Here's a breakdown of what it does:

    - It imports the pandas library, which is a powerful data manipulation and analysis library.

    - It sets the maximum column width for pandas' display options to 0. This means that the full text of each column will be displayed without truncation when the DataFrame is printed.

    - It uses the pd.read_json function to load the train_sft.jsonl file from the ultrachat_200k_dataset directory into a DataFrame. The lines=True argument indicates that the file is in JSON Lines format, where each line is a separate JSON object.

    - It uses the head method to display the first 5 rows of the DataFrame. If the DataFrame has less than 5 rows, it will display all of them.

    - In summary, this script is loading a JSON Lines file into a DataFrame and displaying the first 5 rows with full column text.
    
    ```python
    # Import the pandas library, which is a powerful data manipulation and analysis library
    import pandas as pd
    
    # Set the maximum column width for pandas' display options to 0
    # This means that the full text of each column will be displayed without truncation when the DataFrame is printed
    pd.set_option("display.max_colwidth", 0)
    
    # Use the pd.read_json function to load the train_sft.jsonl file from the ultrachat_200k_dataset directory into a DataFrame
    # The lines=True argument indicates that the file is in JSON Lines format, where each line is a separate JSON object
    df = pd.read_json("./ultrachat_200k_dataset/train_sft.jsonl", lines=True)
    
    # Use the head method to display the first 5 rows of the DataFrame
    # If the DataFrame has less than 5 rows, it will display all of them
    df.head()
    ```

## 5. Submit the fine tuning job using the the model and data as inputs

Create the job that uses the chat-completion pipeline component. Learn more about all the parameters supported for fine tuning.

### Define finetune parameters

1. Finetune parameters can be grouped into 2 categories - training parameters, optimization parameters

1. Training parameters define the training aspects such as -

    - The optimizer, scheduler to use
    - The metric to optimize the finetune
    - Number of training steps and the batch size and so on
    - Optimization parameters help in optimizing the GPU memory and effectively using the compute resources. 

1. Below are few of the parameters that belong to this category. The optimization parameters differs for each model and are packaged with the model to handle these variations.

    - Enable the deepspeed and LoRA
    - Enable mixed precision training
    - Enable multi-node training

> [!NOTE]
> Supervised finetuning may result in loosing alignment or catastrophic forgetting. We recommend checking for this issue and running an alignment stage after you finetune.

### Fine Tuning Parameters

1. This Python script is setting up parameters for fine-tuning a machine learning model. Here's a breakdown of what it does:

    - It sets up default training parameters such as the number of training epochs, batch sizes for training and evaluation, learning rate, and learning rate scheduler type.

    - It sets up default optimization parameters such as whether to apply Layer-wise Relevance Propagation (LoRa) and DeepSpeed, and the DeepSpeed stage.

    - It combines the training and optimization parameters into a single dictionary called finetune_parameters.

    - It checks if the foundation_model has any model-specific default parameters. If it does, it prints a warning message and updates the finetune_parameters dictionary with these model-specific defaults. The ast.literal_eval function is used to convert the model-specific defaults from a string to a Python dictionary.

    - It prints the final set of fine-tuning parameters that will be used for the run.

    - In summary, this script is setting up and displaying the parameters for fine-tuning a machine learning model, with the ability to override the default parameters with model-specific ones.

    ```python
    # Set up default training parameters such as the number of training epochs, batch sizes for training and evaluation, learning rate, and learning rate scheduler type
    training_parameters = dict(
        num_train_epochs=3,
        per_device_train_batch_size=1,
        per_device_eval_batch_size=1,
        learning_rate=5e-6,
        lr_scheduler_type="cosine",
    )
    
    # Set up default optimization parameters such as whether to apply Layer-wise Relevance Propagation (LoRa) and DeepSpeed, and the DeepSpeed stage
    optimization_parameters = dict(
        apply_lora="true",
        apply_deepspeed="true",
        deepspeed_stage=2,
    )
    
    # Combine the training and optimization parameters into a single dictionary called finetune_parameters
    finetune_parameters = {**training_parameters, **optimization_parameters}
    
    # Check if the foundation_model has any model-specific default parameters
    # If it does, print a warning message and update the finetune_parameters dictionary with these model-specific defaults
    # The ast.literal_eval function is used to convert the model-specific defaults from a string to a Python dictionary
    if "model_specific_defaults" in foundation_model.tags:
        print("Warning! Model specific defaults exist. The defaults could be overridden.")
        finetune_parameters.update(
            ast.literal_eval(  # convert string to python dict
                foundation_model.tags["model_specific_defaults"]
            )
        )
    
    # Print the final set of fine-tuning parameters that will be used for the run
    print(
        f"The following finetune parameters are going to be set for the run: {finetune_parameters}"
    )
    ```

### Training Pipeline

1. This Python script is defining a function to generate a display name for a machine learning training pipeline, and then calling this function to generate and print the display name. Here's a breakdown of what it does:

1. The get_pipeline_display_name function is defined. This function generates a display name based on various parameters related to the training pipeline.

1. Inside the function, it calculates the total batch size by multiplying the per-device batch size, the number of gradient accumulation steps, the number of GPUs per node, and the number of nodes used for fine-tuning.

1. It retrieves various other parameters such as the learning rate scheduler type, whether DeepSpeed is applied, the DeepSpeed stage, whether Layer-wise Relevance Propagation (LoRa) is applied, the limit on the number of model checkpoints to keep, and the maximum sequence length.

1. It constructs a string that includes all these parameters, separated by hyphens. If DeepSpeed or LoRa is applied, the string includes "ds" followed by the DeepSpeed stage, or "lora", respectively. If not, it includes "nods" or "nolora", respectively.

1. The function returns this string, which serves as the display name for the training pipeline.

1. After the function is defined, it is called to generate the display name, which is then printed.

1. In summary, this script is generating a display name for a machine learning training pipeline based on various parameters, and then printing this display name.

    ```python
    # Define a function to generate a display name for the training pipeline
    def get_pipeline_display_name():
        # Calculate the total batch size by multiplying the per-device batch size, the number of gradient accumulation steps, the number of GPUs per node, and the number of nodes used for fine-tuning
        batch_size = (
            int(finetune_parameters.get("per_device_train_batch_size", 1))
            * int(finetune_parameters.get("gradient_accumulation_steps", 1))
            * int(gpus_per_node)
            * int(finetune_parameters.get("num_nodes_finetune", 1))
        )
        # Retrieve the learning rate scheduler type
        scheduler = finetune_parameters.get("lr_scheduler_type", "linear")
        # Retrieve whether DeepSpeed is applied
        deepspeed = finetune_parameters.get("apply_deepspeed", "false")
        # Retrieve the DeepSpeed stage
        ds_stage = finetune_parameters.get("deepspeed_stage", "2")
        # If DeepSpeed is applied, include "ds" followed by the DeepSpeed stage in the display name; if not, include "nods"
        if deepspeed == "true":
            ds_string = f"ds{ds_stage}"
        else:
            ds_string = "nods"
        # Retrieve whether Layer-wise Relevance Propagation (LoRa) is applied
        lora = finetune_parameters.get("apply_lora", "false")
        # If LoRa is applied, include "lora" in the display name; if not, include "nolora"
        if lora == "true":
            lora_string = "lora"
        else:
            lora_string = "nolora"
        # Retrieve the limit on the number of model checkpoints to keep
        save_limit = finetune_parameters.get("save_total_limit", -1)
        # Retrieve the maximum sequence length
        seq_len = finetune_parameters.get("max_seq_length", -1)
        # Construct the display name by concatenating all these parameters, separated by hyphens
        return (
            model_name
            + "-"
            + "ultrachat"
            + "-"
            + f"bs{batch_size}"
            + "-"
            + f"{scheduler}"
            + "-"
            + ds_string
            + "-"
            + lora_string
            + f"-save_limit{save_limit}"
            + f"-seqlen{seq_len}"
        )
    
    # Call the function to generate the display name
    pipeline_display_name = get_pipeline_display_name()
    # Print the display name
    print(f"Display name used for the run: {pipeline_display_name}")
    ```

### Configuring Pipeline

This Python script is defining and configuring a machine learning pipeline using the Azure Machine Learning SDK. Here's a breakdown of what it does:

1. It imports necessary modules from the Azure AI ML SDK.

1. It fetches a pipeline component named "chat_completion_pipeline" from the registry.

1. It defines a pipeline job using the `@pipeline` decorator and the function `create_pipeline`. The name of the pipeline is set to `pipeline_display_name`.

1. Inside the `create_pipeline` function, it initializes the fetched pipeline component with various parameters, including the model path, compute clusters for different stages, dataset splits for training and testing, the number of GPUs to use for fine-tuning, and other fine-tuning parameters.

1. It maps the output of the fine-tuning job to the output of the pipeline job. This is done so that the fine-tuned model can be easily registered, which is required to deploy the model to an online or batch endpoint.

1. It creates an instance of the pipeline by calling the `create_pipeline` function.

1. It sets the `force_rerun` setting of the pipeline to `True`, meaning that cached results from previous jobs will not be used.

1. It sets the `continue_on_step_failure` setting of the pipeline to `False`, meaning that the pipeline will stop if any step fails.

1. In summary, this script is defining and configuring a machine learning pipeline for a chat completion task using the Azure Machine Learning SDK.

    ```python
    # Import necessary modules from the Azure AI ML SDK
    from azure.ai.ml.dsl import pipeline
    from azure.ai.ml import Input
    
    # Fetch the pipeline component named "chat_completion_pipeline" from the registry
    pipeline_component_func = registry_ml_client.components.get(
        name="chat_completion_pipeline", label="latest"
    )
    
    # Define the pipeline job using the @pipeline decorator and the function create_pipeline
    # The name of the pipeline is set to pipeline_display_name
    @pipeline(name=pipeline_display_name)
    def create_pipeline():
        # Initialize the fetched pipeline component with various parameters
        # These include the model path, compute clusters for different stages, dataset splits for training and testing, the number of GPUs to use for fine-tuning, and other fine-tuning parameters
        chat_completion_pipeline = pipeline_component_func(
            mlflow_model_path=foundation_model.id,
            compute_model_import=compute_cluster,
            compute_preprocess=compute_cluster,
            compute_finetune=compute_cluster,
            compute_model_evaluation=compute_cluster,
            # Map the dataset splits to parameters
            train_file_path=Input(
                type="uri_file", path="./ultrachat_200k_dataset/train_sft.jsonl"
            ),
            test_file_path=Input(
                type="uri_file", path="./ultrachat_200k_dataset/test_sft.jsonl"
            ),
            # Training settings
            number_of_gpu_to_use_finetuning=gpus_per_node,  # Set to the number of GPUs available in the compute
            **finetune_parameters
        )
        return {
            # Map the output of the fine tuning job to the output of pipeline job
            # This is done so that we can easily register the fine tuned model
            # Registering the model is required to deploy the model to an online or batch endpoint
            "trained_model": chat_completion_pipeline.outputs.mlflow_model_folder
        }
    
    # Create an instance of the pipeline by calling the create_pipeline function
    pipeline_object = create_pipeline()
    
    # Don't use cached results from previous jobs
    pipeline_object.settings.force_rerun = True
    
    # Set continue on step failure to False
    # This means that the pipeline will stop if any step fails
    pipeline_object.settings.continue_on_step_failure = False
    ```

### Submit the Job

1. This Python script is submitting a machine learning pipeline job to an Azure Machine Learning workspace and then waiting for the job to complete. Here's a breakdown of what it does:

    - It calls the create_or_update method of the jobs object in the workspace_ml_client to submit the pipeline job. The pipeline to be run is specified by pipeline_object, and the experiment under which the job is run is specified by experiment_name.

    - It then calls the stream method of the jobs object in the workspace_ml_client to wait for the pipeline job to complete. The job to wait for is specified by the name attribute of the pipeline_job object.

    - In summary, this script is submitting a machine learning pipeline job to an Azure Machine Learning workspace, and then waiting for the job to complete.

    ```python
    # Submit the pipeline job to the Azure Machine Learning workspace
    # The pipeline to be run is specified by pipeline_object
    # The experiment under which the job is run is specified by experiment_name
    pipeline_job = workspace_ml_client.jobs.create_or_update(
        pipeline_object, experiment_name=experiment_name
    )
    
    # Wait for the pipeline job to complete
    # The job to wait for is specified by the name attribute of the pipeline_job object
    workspace_ml_client.jobs.stream(pipeline_job.name)
    ```

## 6. Register the fine tuned model with the workspace

We will register the model from the output of the fine tuning job. This will track lineage between the fine tuned model and the fine tuning job. The fine tuning job, further, tracks lineage to the foundation model, data and training code.

### Registering the ML Model

1. This Python script is registering a machine learning model that was trained in an Azure Machine Learning pipeline. Here's a breakdown of what it does:

    - It imports necessary modules from the Azure AI ML SDK.

    - It checks if the trained_model output is available from the pipeline job by calling the get method of the jobs object in the workspace_ml_client and accessing its outputs attribute.

    - It constructs a path to the trained model by formatting a string with the name of the pipeline job and the name of the output ("trained_model").

    - It defines a name for the fine-tuned model by appending "-ultrachat-200k" to the original model name and replacing any slashes with hyphens.

    - It prepares to register the model by creating a Model object with various parameters, including the path to the model, the type of the model (MLflow model), the name and version of the model, and a description of the model.

    - It registers the model by calling the create_or_update method of the models object in the workspace_ml_client with the Model object as the argument.

    - It prints the registered model.

1. In summary, this script is registering a machine learning model that was trained in an Azure Machine Learning pipeline.
    
    ```python
    # Import necessary modules from the Azure AI ML SDK
    from azure.ai.ml.entities import Model
    from azure.ai.ml.constants import AssetTypes
    
    # Check if the `trained_model` output is available from the pipeline job
    print("pipeline job outputs: ", workspace_ml_client.jobs.get(pipeline_job.name).outputs)
    
    # Construct a path to the trained model by formatting a string with the name of the pipeline job and the name of the output ("trained_model")
    model_path_from_job = "azureml://jobs/{0}/outputs/{1}".format(
        pipeline_job.name, "trained_model"
    )
    
    # Define a name for the fine-tuned model by appending "-ultrachat-200k" to the original model name and replacing any slashes with hyphens
    finetuned_model_name = model_name + "-ultrachat-200k"
    finetuned_model_name = finetuned_model_name.replace("/", "-")
    
    print("path to register model: ", model_path_from_job)
    
    # Prepare to register the model by creating a Model object with various parameters
    # These include the path to the model, the type of the model (MLflow model), the name and version of the model, and a description of the model
    prepare_to_register_model = Model(
        path=model_path_from_job,
        type=AssetTypes.MLFLOW_MODEL,
        name=finetuned_model_name,
        version=timestamp,  # Use timestamp as version to avoid version conflict
        description=model_name + " fine tuned model for ultrachat 200k chat-completion",
    )
    
    print("prepare to register model: \n", prepare_to_register_model)
    
    # Register the model by calling the create_or_update method of the models object in the workspace_ml_client with the Model object as the argument
    registered_model = workspace_ml_client.models.create_or_update(
        prepare_to_register_model
    )
    
    # Print the registered model
    print("registered model: \n", registered_model)
    ```

## 7. Deploy the fine tuned model to an online endpoint

Online endpoints give a durable REST API that can be used to integrate with applications that need to use the model.

### Manage Endpoint

1. This Python script is creating a managed online endpoint in Azure Machine Learning for a registered model. Here's a breakdown of what it does:

    - It imports necessary modules from the Azure AI ML SDK.

    - It defines a unique name for the online endpoint by appending a timestamp to the string "ultrachat-completion-".

    - It prepares to create the online endpoint by creating a ManagedOnlineEndpoint object with various parameters, including the name of the endpoint, a description of the endpoint, and the authentication mode ("key").

    - It creates the online endpoint by calling the begin_create_or_update method of the workspace_ml_client with the ManagedOnlineEndpoint object as the argument. It then waits for the creation operation to complete by calling the wait method.

1. In summary, this script is creating a managed online endpoint in Azure Machine Learning for a registered model.

    ```python
    # Import necessary modules from the Azure AI ML SDK
    from azure.ai.ml.entities import (
        ManagedOnlineEndpoint,
        ManagedOnlineDeployment,
        ProbeSettings,
        OnlineRequestSettings,
    )
    
    # Define a unique name for the online endpoint by appending a timestamp to the string "ultrachat-completion-"
    online_endpoint_name = "ultrachat-completion-" + timestamp
    
    # Prepare to create the online endpoint by creating a ManagedOnlineEndpoint object with various parameters
    # These include the name of the endpoint, a description of the endpoint, and the authentication mode ("key")
    endpoint = ManagedOnlineEndpoint(
        name=online_endpoint_name,
        description="Online endpoint for "
        + registered_model.name
        + ", fine tuned model for ultrachat-200k-chat-completion",
        auth_mode="key",
    )
    
    # Create the online endpoint by calling the begin_create_or_update method of the workspace_ml_client with the ManagedOnlineEndpoint object as the argument
    # Then wait for the creation operation to complete by calling the wait method
    workspace_ml_client.begin_create_or_update(endpoint).wait()
    ```

> [!NOTE]
> You can find here the list of SKU's supported for deployment - [Managed online endpoints SKU list](https://learn.microsoft.com/azure/machine-learning/reference-managed-online-endpoints-vm-sku-list)

### Deploying ML Model

1. This Python script is deploying a registered machine learning model to a managed online endpoint in Azure Machine Learning. Here's a breakdown of what it does:

    - It imports the ast module, which provides functions to process trees of the Python abstract syntax grammar.

    - It sets the instance type for the deployment to "Standard_NC6s_v3".

    - It checks if the inference_compute_allow_list tag is present in the foundation model. If it is, it converts the tag value from a string to a Python list and assigns it to inference_computes_allow_list. If it's not, it sets inference_computes_allow_list to None.

    - It checks if the specified instance type is in the allow list. If it's not, it prints a message asking the user to select an instance type from the allow list.

    - It prepares to create the deployment by creating a ManagedOnlineDeployment object with various parameters, including the name of the deployment, the name of the endpoint, the ID of the model, the instance type and count, the liveness probe settings, and the request settings.

    - It creates the deployment by calling the begin_create_or_update method of the workspace_ml_client with the ManagedOnlineDeployment object as the argument. It then waits for the creation operation to complete by calling the wait method.

    - It sets the traffic of the endpoint to direct 100% of the traffic to the "demo" deployment.

    - It updates the endpoint by calling the begin_create_or_update method of the workspace_ml_client with the endpoint object as the argument. It then waits for the update operation to complete by calling the result method.

1. In summary, this script is deploying a registered machine learning model to a managed online endpoint in Azure Machine Learning.

    ```python
    # Import the ast module, which provides functions to process trees of the Python abstract syntax grammar
    import ast
    
    # Set the instance type for the deployment
    instance_type = "Standard_NC6s_v3"
    
    # Check if the `inference_compute_allow_list` tag is present in the foundation model
    if "inference_compute_allow_list" in foundation_model.tags:
        # If it is, convert the tag value from a string to a Python list and assign it to `inference_computes_allow_list`
        inference_computes_allow_list = ast.literal_eval(
            foundation_model.tags["inference_compute_allow_list"]
        )
        print(f"Please create a compute from the above list - {computes_allow_list}")
    else:
        # If it's not, set `inference_computes_allow_list` to `None`
        inference_computes_allow_list = None
        print("`inference_compute_allow_list` is not part of model tags")
    
    # Check if the specified instance type is in the allow list
    if (
        inference_computes_allow_list is not None
        and instance_type not in inference_computes_allow_list
    ):
        print(
            f"`instance_type` is not in the allow listed compute. Please select a value from {inference_computes_allow_list}"
        )
    
    # Prepare to create the deployment by creating a `ManagedOnlineDeployment` object with various parameters
    demo_deployment = ManagedOnlineDeployment(
        name="demo",
        endpoint_name=online_endpoint_name,
        model=registered_model.id,
        instance_type=instance_type,
        instance_count=1,
        liveness_probe=ProbeSettings(initial_delay=600),
        request_settings=OnlineRequestSettings(request_timeout_ms=90000),
    )
    
    # Create the deployment by calling the `begin_create_or_update` method of the `workspace_ml_client` with the `ManagedOnlineDeployment` object as the argument
    # Then wait for the creation operation to complete by calling the `wait` method
    workspace_ml_client.online_deployments.begin_create_or_update(demo_deployment).wait()
    
    # Set the traffic of the endpoint to direct 100% of the traffic to the "demo" deployment
    endpoint.traffic = {"demo": 100}
    
    # Update the endpoint by calling the `begin_create_or_update` method of the `workspace_ml_client` with the `endpoint` object as the argument
    # Then wait for the update operation to complete by calling the `result` method
    workspace_ml_client.begin_create_or_update(endpoint).result()
    ```

## 8. Test the endpoint with sample data

We will fetch some sample data from the test dataset and submit to online endpoint for inference. We will then show the display the scored labels alongside the ground truth labels

### Reading the results

1. This Python script is reading a JSON Lines file into a pandas DataFrame, taking a random sample, and resetting the index. Here's a breakdown of what it does:

    - It reads the file ./ultrachat_200k_dataset/test_gen.jsonl into a pandas DataFrame. The read_json function is used with the lines=True argument because the file is in JSON Lines format, where each line is a separate JSON object.

    - It takes a random sample of 1 row from the DataFrame. The sample function is used with the n=1 argument to specify the number of random rows to select.

    - It resets the index of the DataFrame. The reset_index function is used with the drop=True argument to drop the original index and replace it with a new index of default integer values.

    - It displays the first 2 rows of the DataFrame using the head function with the argument 2. However, since the DataFrame only contains one row after the sampling, this will only display that one row.

1. In summary, this script is reading a JSON Lines file into a pandas DataFrame, taking a random sample of 1 row, resetting the index, and displaying the first row.
    
    ```python
    # Import pandas library
    import pandas as pd
    
    # Read the JSON Lines file './ultrachat_200k_dataset/test_gen.jsonl' into a pandas DataFrame
    # The 'lines=True' argument indicates that the file is in JSON Lines format, where each line is a separate JSON object
    test_df = pd.read_json("./ultrachat_200k_dataset/test_gen.jsonl", lines=True)
    
    # Take a random sample of 1 row from the DataFrame
    # The 'n=1' argument specifies the number of random rows to select
    test_df = test_df.sample(n=1)
    
    # Reset the index of the DataFrame
    # The 'drop=True' argument indicates that the original index should be dropped and replaced with a new index of default integer values
    # The 'inplace=True' argument indicates that the DataFrame should be modified in place (without creating a new object)
    test_df.reset_index(drop=True, inplace=True)
    
    # Display the first 2 rows of the DataFrame
    # However, since the DataFrame only contains one row after the sampling, this will only display that one row
    test_df.head(2)
    ```

### Create JSON Object

1. This Python script is creating a JSON object with specific parameters and saving it to a file. Here's a breakdown of what it does:

    - It imports the json module, which provides functions to work with JSON data.

    - It creates a dictionary parameters with keys and values that represent parameters for a machine learning model. The keys are "temperature", "top_p", "do_sample", and "max_new_tokens", and their corresponding values are 0.6, 0.9, True, and 200 respectively.

    - It creates another dictionary test_json with two keys: "input_data" and "params". The value of "input_data" is another dictionary with keys "input_string" and "parameters". The value of "input_string" is a list containing the first message from the test_df DataFrame. The value of "parameters" is the parameters dictionary created earlier. The value of "params" is an empty dictionary.

    - It opens a file named sample_score.json
    
    ```python
    # Import the json module, which provides functions to work with JSON data
    import json
    
    # Create a dictionary `parameters` with keys and values that represent parameters for a machine learning model
    # The keys are "temperature", "top_p", "do_sample", and "max_new_tokens", and their corresponding values are 0.6, 0.9, True, and 200 respectively
    parameters = {
        "temperature": 0.6,
        "top_p": 0.9,
        "do_sample": True,
        "max_new_tokens": 200,
    }
    
    # Create another dictionary `test_json` with two keys: "input_data" and "params"
    # The value of "input_data" is another dictionary with keys "input_string" and "parameters"
    # The value of "input_string" is a list containing the first message from the `test_df` DataFrame
    # The value of "parameters" is the `parameters` dictionary created earlier
    # The value of "params" is an empty dictionary
    test_json = {
        "input_data": {
            "input_string": [test_df["messages"][0]],
            "parameters": parameters,
        },
        "params": {},
    }
    
    # Open a file named `sample_score.json` in the `./ultrachat_200k_dataset` directory in write mode
    with open("./ultrachat_200k_dataset/sample_score.json", "w") as f:
        # Write the `test_json` dictionary to the file in JSON format using the `json.dump` function
        json.dump(test_json, f)
    ```

### Invoking Endpoint

1. This Python script is invoking an online endpoint in Azure Machine Learning to score a JSON file. Here's a breakdown of what it does:

    - It calls the invoke method of the online_endpoints property of the workspace_ml_client object. This method is used to send a request to an online endpoint and get a response.

    - It specifies the name of the endpoint and the deployment with the endpoint_name and deployment_name arguments. In this case, the endpoint name is stored in the online_endpoint_name variable and the deployment name is "demo".

    - It specifies the path to the JSON file to be scored with the request_file argument. In this case, the file is ./ultrachat_200k_dataset/sample_score.json.

    - It stores the response from the endpoint in the response variable.

    - It prints the raw response.

1. In summary, this script is invoking an online endpoint in Azure Machine Learning to score a JSON file and printing the response.

    ```python
    # Invoke the online endpoint in Azure Machine Learning to score the `sample_score.json` file
    # The `invoke` method of the `online_endpoints` property of the `workspace_ml_client` object is used to send a request to an online endpoint and get a response
    # The `endpoint_name` argument specifies the name of the endpoint, which is stored in the `online_endpoint_name` variable
    # The `deployment_name` argument specifies the name of the deployment, which is "demo"
    # The `request_file` argument specifies the path to the JSON file to be scored, which is `./ultrachat_200k_dataset/sample_score.json`
    response = workspace_ml_client.online_endpoints.invoke(
        endpoint_name=online_endpoint_name,
        deployment_name="demo",
        request_file="./ultrachat_200k_dataset/sample_score.json",
    )
    
    # Print the raw response from the endpoint
    print("raw response: \n", response, "\n")
    ```

## 9. Delete the online endpoint

1. Don't forget to delete the online endpoint, else you will leave the billing meter running for the compute used by the endpoint. This line of Python code is deleting an online endpoint in Azure Machine Learning. Here's a breakdown of what it does:

    - It calls the begin_delete method of the online_endpoints property of the workspace_ml_client object. This method is used to start the deletion of an online endpoint.

    - It specifies the name of the endpoint to be deleted with the name argument. In this case, the endpoint name is stored in the online_endpoint_name variable.

    - It calls the wait method to wait for the deletion operation to complete. This is a blocking operation, meaning that it will prevent the script from continuing until the deletion is finished.

    - In summary, this line of code is starting the deletion of an online endpoint in Azure Machine Learning and waiting for the operation to complete.

    ```python
    # Delete the online endpoint in Azure Machine Learning
    # The `begin_delete` method of the `online_endpoints` property of the `workspace_ml_client` object is used to start the deletion of an online endpoint
    # The `name` argument specifies the name of the endpoint to be deleted, which is stored in the `online_endpoint_name` variable
    # The `wait` method is called to wait for the deletion operation to complete. This is a blocking operation, meaning that it will prevent the script from continuing until the deletion is finished
    workspace_ml_client.online_endpoints.begin_delete(name=online_endpoint_name).wait()
    ```
