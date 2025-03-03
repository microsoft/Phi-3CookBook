# ریموٹ انفرینسنگ فائن ٹونڈ ماڈل کے ساتھ

جب ایڈاپٹرز کو ریموٹ ماحول میں ٹرین کیا جا چکا ہو، تو ماڈل کے ساتھ انٹریکٹ کرنے کے لیے ایک سادہ Gradio ایپلیکیشن استعمال کریں۔

![فائن ٹون مکمل](../../../../../translated_images/log-finetuning-res.4b3ee593f24d3096742d09375adade22b217738cab93bc1139f224e5888a1cbf.ur.png)

### Azure ریسورسز کی تیاری
ریموٹ انفرینسنگ کے لیے Azure ریسورسز کو سیٹ اپ کرنے کے لیے کمانڈ پیلیٹ سے `AI Toolkit: Provision Azure Container Apps for inference` چلائیں۔ اس سیٹ اپ کے دوران، آپ سے اپنی Azure سبسکرپشن اور ریسورس گروپ منتخب کرنے کے لیے کہا جائے گا۔  
![انفرینس ریسورس کی تیاری](../../../../../translated_images/command-provision-inference.b294f3ae5764ab45b83246d464ad5329b0de20cf380f75a699b4cc6b5495ca11.ur.png)

عام طور پر، انفرینسنگ کے لیے سبسکرپشن اور ریسورس گروپ وہی ہونے چاہئیں جو فائن ٹوننگ کے لیے استعمال کیے گئے تھے۔ انفرینسنگ اسی Azure Container App Environment کا استعمال کرے گا اور Azure Files میں محفوظ ماڈل اور ماڈل ایڈاپٹر تک رسائی حاصل کرے گا، جو فائن ٹوننگ کے مرحلے کے دوران تیار کیے گئے تھے۔

## AI ٹول کٹ کا استعمال

### انفرینسنگ کے لیے ڈپلائمنٹ  
اگر آپ انفرینسنگ کوڈ میں ترمیم کرنا چاہتے ہیں یا انفرینسنگ ماڈل کو دوبارہ لوڈ کرنا چاہتے ہیں، تو `AI Toolkit: Deploy for inference` کمانڈ چلائیں۔ یہ آپ کے تازہ ترین کوڈ کو ACA کے ساتھ ہم آہنگ کرے گا اور ریپلیکا کو دوبارہ شروع کرے گا۔

![انفرینسنگ کے لیے ڈپلائمنٹ](../../../../../translated_images/command-deploy.cb6508c973d6257e649aa4f262d3c170a374da3e9810a4f3d9e03935408a592b.ur.png)

ڈپلائمنٹ کامیابی سے مکمل ہونے کے بعد، ماڈل اب اس اینڈپوائنٹ کے ذریعے ایویلیوایشن کے لیے تیار ہے۔

### انفرینس API تک رسائی

آپ انفرینس API تک رسائی حاصل کرنے کے لیے VSCode نوٹیفکیشن میں ظاہر ہونے والے "*Go to Inference Endpoint*" بٹن پر کلک کر سکتے ہیں۔ متبادل کے طور پر، ویب API اینڈپوائنٹ `ACA_APP_ENDPOINT` میں `./infra/inference.config.json` اور آؤٹ پٹ پینل میں پایا جا سکتا ہے۔

![ایپ اینڈپوائنٹ](../../../../../translated_images/notification-deploy.00f4267b7aa6a18cfaaec83a7831b5d09311d5d96a70bb4c9d651ea4a41a8af7.ur.png)

> **نوٹ:** انفرینس اینڈپوائنٹ کو مکمل طور پر فعال ہونے میں چند منٹ لگ سکتے ہیں۔

## ٹیمپلیٹ میں شامل انفرینس کمپوننٹس
 
| فولڈر | مواد |
| ------ |--------- |
| `infra` | ریموٹ آپریشنز کے لیے تمام ضروری کنفیگریشنز پر مشتمل ہے۔ |
| `infra/provision/inference.parameters.json` | بائیسپ ٹیمپلیٹس کے پیرامیٹرز کو رکھتا ہے، جو Azure ریسورسز کی تیاری کے لیے استعمال ہوتے ہیں۔ |
| `infra/provision/inference.bicep` | Azure ریسورسز کی تیاری کے لیے ٹیمپلیٹس پر مشتمل ہے۔ |
| `infra/inference.config.json` | کنفیگریشن فائل، جو `AI Toolkit: Provision Azure Container Apps for inference` کمانڈ کے ذریعے تیار کی گئی ہے۔ یہ دیگر ریموٹ کمانڈ پیلیٹس کے لیے ان پٹ کے طور پر استعمال ہوتی ہے۔ |

### Azure ریسورس پروویژن کو کنفیگر کرنے کے لیے AI ٹول کٹ کا استعمال
[AI ٹول کٹ](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio) کو کنفیگر کریں۔

انفرینسنگ کے لیے Azure Container Apps پروویژن کریں ` command.

You can find configuration parameters in `./infra/provision/inference.parameters.json` file. Here are the details:
| Parameter | Description |
| --------- |------------ |
| `defaultCommands` | This is the commands to initiate a web API. |
| `maximumInstanceCount` | This parameter sets the maximum capacity of GPU instances. |
| `location` | This is the location where Azure resources are provisioned. The default value is the same as the chosen resource group's location. |
| `storageAccountName`, `fileShareName` `acaEnvironmentName`, `acaEnvironmentStorageName`, `acaAppName`,  `acaLogAnalyticsName` | These parameters are used to name the Azure resources for provision. By default, they will be same to the fine-tuning resource name. You can input a new, unused resource name to create your own custom-named resources, or you can input the name of an already existing Azure resource if you'd prefer to use that. For details, refer to the section [Using existing Azure Resources](../../../../../md/01.Introduction/03). |

### Using Existing Azure Resources

By default, the inference provision use the same Azure Container App Environment, Storage Account, Azure File Share, and Azure Log Analytics that were used for fine-tuning. A separate Azure Container App is created solely for the inference API. 

If you have customized the Azure resources during the fine-tuning step or want to use your own existing Azure resources for inference, specify their names in the `./infra/inference.parameters.json` فائل۔ پھر، کمانڈ پیلیٹ سے `AI Toolkit: Provision Azure Container Apps for inference` کمانڈ چلائیں۔ یہ کسی بھی مخصوص ریسورس کو اپڈیٹ کرے گا اور کسی بھی غیر موجود ریسورس کو تیار کرے گا۔

مثال کے طور پر، اگر آپ کے پاس ایک موجودہ Azure کنٹینر ماحول ہے، تو آپ کی `./infra/finetuning.parameters.json` فائل اس طرح نظر آنی چاہیے:

```json
{
    "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentParameters.json#",
    "contentVersion": "1.0.0.0",
    "parameters": {
      ...
      "acaEnvironmentName": {
        "value": "<your-aca-env-name>"
      },
      "acaEnvironmentStorageName": {
        "value": null
      },
      ...
    }
  }
```

### دستی تیاری  
اگر آپ Azure ریسورسز کو دستی طور پر کنفیگر کرنا پسند کرتے ہیں، تو آپ `./infra/provision` folders. If you have already set up and configured all the Azure resources without using the AI Toolkit command palette, you can simply enter the resource names in the `inference.config.json` فائل میں فراہم کردہ بائیسپ فائلز استعمال کر سکتے ہیں۔

مثال کے طور پر:

```json
{
  "SUBSCRIPTION_ID": "<your-subscription-id>",
  "RESOURCE_GROUP_NAME": "<your-resource-group-name>",
  "STORAGE_ACCOUNT_NAME": "<your-storage-account-name>",
  "FILE_SHARE_NAME": "<your-file-share-name>",
  "ACA_APP_NAME": "<your-aca-name>",
  "ACA_APP_ENDPOINT": "<your-aca-endpoint>"
}
```

**ڈسکلیمر**:  
یہ دستاویز مشین پر مبنی AI ترجمہ خدمات کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کی کوشش کرتے ہیں، براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا نقصانات ہو سکتے ہیں۔ اصل دستاویز کو اس کی مقامی زبان میں مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے لیے ہم ذمہ دار نہیں ہیں۔