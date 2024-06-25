# **準備您的行業數據**

我們希望將 Phi-3-mini 注入 [TruthfulQA 的資料](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv)。第一步是匯入 TruthfulQA 的資料。

### **1. 載入資料到 csv 並將其儲存為 json**

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

### **2. 上傳資料到 Azure ML 資料存儲區**

![amldata](../../../../imgs/06/e2e/azureml_data.png)

### **恭喜！**

您的資料已成功載入。接下來，您需要透過 Microsoft Olive 設定您的資料和相關算法 [E2E_LoRA&QLoRA_Config_With_Olive.md](./E2E_LoRA&QLoRA_Config_With_Olive.md)。

