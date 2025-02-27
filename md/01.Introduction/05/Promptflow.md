# **Introduce Promptflow**

 [Microsoft Prompt Flow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=aiml-138114-kinfeylo) is a visual workflow automation tool that allows users to create automated workflows using pre-built templates and custom connectors. It is designed to enable developers and business analysts to quickly build automated processes for tasks such as data management, collaboration, and process optimization. With Prompt Flow, users can easily connect different services, applications, and systems, and automate complex business processes.

 Microsoft Prompt Flow is designed to streamline the end-to-end development cycle of AI applications powered by Large Language Models (LLMs). Whether you're ideating, prototyping, testing, evaluating, or deploying LLM-based applications, Prompt Flow simplifies the process and enables you to build LLM apps with production quality.

## Here are the key features and benefits of using Microsoft Prompt Flow:

**Interactive Authoring Experience**

Prompt Flow provides a visual representation of your flow's structure, making it easy to understand and navigate your projects.
It offers a notebook-like coding experience for efficient flow development and debugging.

**Prompt Variants and Tuning**

Create and compare multiple prompt variants to facilitate an iterative refinement process. Evaluate the performance of different prompts and choose the most effective ones.

**Built-in Evaluation Flows**
Assess the quality and effectiveness of your prompts and flows using built-in evaluation tools.
Understand how well your LLM-based applications are performing.

**Comprehensive Resources**

Prompt Flow includes a library of built-in tools, samples, and templates. These resources serve as a starting point for development, inspire creativity, and accelerate the process.

**Collaboration and Enterprise Readiness**

Support team collaboration by allowing multiple users to work together on prompt engineering projects.
Maintain version control and share knowledge effectively. Streamline the entire prompt engineering process, from development and evaluation to deployment and monitoring.

## Evaluation in Prompt Flow 

In Microsoft Prompt Flow, evaluation plays a crucial role in assessing how well your AI models perform. Let's explore how you can customize evaluation flows and metrics within Prompt Flow:

![PFVizualise](../../../imgs/01/05/PromptFlow/pfvisualize.png)

**Understanding Evaluation in Prompt Flow**

In Prompt Flow, a flow represents a sequence of nodes that process input and generate output. Evaluation flows are special types of flows designed to assess the performance of a run based on specific criteria and goals.

**Key features of evaluation flows**

They typically run after the flow being tested, using its outputs. They calculate scores or metrics to measure the performance of the tested flow. Metrics can include accuracy, relevance scores, or any other relevant measures.

### Customizing Evaluation Flows

**Defining Inputs**

Evaluation flows need to take in the outputs of the run being tested. Define inputs similarly to standard flows.
For example, if you're evaluating a QnA flow, name an input as "answer." If evaluating a classification flow, name an input as "category." Ground truth inputs (e.g., actual labels) may also be needed.

**Outputs and Metrics**

Evaluation flows produce results that measure the tested flow's performance. Metrics can be calculated using Python or LLM (Large Language Models). Use the log_metric() function to log relevant metrics.

**Using Customized Evaluation Flows**

Develop your own evaluation flow tailored to your specific tasks and objectives. Customize metrics based on your evaluation goals.
Apply this customized evaluation flow to batch runs for large-scale testing.

## Built-in Evaluation Methods

Prompt Flow also provides built-in evaluation methods.
You can submit batch runs and use these methods to evaluate how well your flow performs with large datasets.
View evaluation results, compare metrics, and iterate as needed.
Remember, evaluation is essential for ensuring your AI models meet desired criteria and goals. Explore the official documentation for detailed instructions on developing and using evaluation flows in Microsoft Prompt Flow.

In summary, Microsoft Prompt Flow empowers developers to create high-quality LLM applications by simplifying prompt engineering and providing a robust development environment. If you're working with LLMs, Prompt Flow is a valuable tool to explore. Explore the [Prompt Flow Evaluation Documents](https://learn.microsoft.com/azure/machine-learning/prompt-flow/how-to-develop-an-evaluation-flow?view=azureml-api-2?WT.mc_id=aiml-138114-kinfeylo) for detailed instructions on developing and using evaluation flows in Microsoft Prompt Flow.

