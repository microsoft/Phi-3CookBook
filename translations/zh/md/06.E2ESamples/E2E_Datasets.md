# **准备您的行业数据**

我们希望将 Phi-3-mini 注入到 [TruthfulQA 的数据](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv) 中。第一步是导入 TruthfulQA 的数据。

### **1. 将数据加载到 csv 并保存为 json**

```python

import csv
import json

csvfile = open('./datasets/TruthfulQA.csv', 'r')
jsonfile = open('./output/TruthfulQA.json', 'w')

fieldnames = ("Type","Category","Question","Best Answer","Correct Answers","Incorrect Answers","Source")

reader = csv.DictReader(csvfile, fieldnames)

for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')

i = 1
data = []
with open('./output/TruthfulQA.json', 'r') as file:
    for line in file:
        print(line)
        data.append(json.loads(line))
        print(str(i))
        i+=1

```

### **2. 将数据上传到 Azure ML 数据存储**

![amldata](../../../../translated_images/azureml_data.0f744f2ec5ea3cac9cbaa3cf7051235bb5b575de80e40a97619ae6f86d696c8f.zh.png)

### **恭喜！**

您的数据已成功加载。接下来，您需要通过 Microsoft Olive 配置您的数据和相关算法 [E2E_LoRA&QLoRA_Config_With_Olive.md](./E2E_LoRA&QLoRA_Config_With_Olive.md)

免责声明：此翻译由AI模型从原文翻译而来，可能并不完美。请审阅输出内容并进行必要的修改。