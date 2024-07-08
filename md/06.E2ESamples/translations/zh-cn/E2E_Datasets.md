# 准备你的行业数据

我们希望将[TruthfulQA的数据](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv)注入到 Phi-3-mini 中。第一步是导入 TruthfulQA 的数据。

## 1. 将数据加载到CSV并保存为JSON

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
        i += 1
```

## 2. 将数据上传到Azure ML数据存储

![amldata](../../imgs/06/e2e/azureml_data.png)

## 恭喜！

你的数据已成功加载。接下来，你需要通过 Microsoft Olive 配置你的数据和相关算法：[E2E_LoRA&QLoRA_Config_With_Olive.md](./E2E_LoRA&QLoRA_Config_With_Olive.md)