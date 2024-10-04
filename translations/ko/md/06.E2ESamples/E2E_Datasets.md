# **업계 데이터를 준비하세요**

우리는 [TruthfulQA의 데이터](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv)에 Phi-3-mini를 주입하려고 합니다. 첫 번째 단계는 TruthfulQA의 데이터를 가져오는 것입니다.

### **1. 데이터를 csv로 불러와 json으로 저장하기**

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

### **2. 데이터를 Azure ML 데이터스토어에 업로드하기**

![amldata](../../../../translated_images/azureml_data.0f744f2ec5ea3cac9cbaa3cf7051235bb5b575de80e40a97619ae6f86d696c8f.ko.png)

### **축하합니다!**

데이터가 성공적으로 로드되었습니다. 다음으로는 Microsoft Olive [E2E_LoRA&QLoRA_Config_With_Olive.md](./E2E_LoRA&QLoRA_Config_With_Olive.md)를 통해 데이터와 관련 알고리즘을 구성해야 합니다.

**면책 조항**:
이 문서는 기계 기반 AI 번역 서비스를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있지만 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서의 원어가 권위 있는 출처로 간주되어야 합니다. 중요한 정보에 대해서는 전문 인간 번역을 권장합니다. 이 번역을 사용함으로써 발생하는 오해나 오역에 대해 우리는 책임을 지지 않습니다.