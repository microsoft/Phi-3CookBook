# Etäinferenssi hienosäädetyn mallin avulla

Kun adapterit on koulutettu etäympäristössä, voit käyttää yksinkertaista Gradio-sovellusta mallin kanssa vuorovaikutukseen.

![Hienosäätö valmis](../../../../../translated_images/log-finetuning-res.4b3ee593f24d3096742d09375adade22b217738cab93bc1139f224e5888a1cbf.fi.png)

### Azure-resurssien valmistelu
Sinun täytyy määrittää Azure-resurssit etäinferenssiä varten suorittamalla `AI Toolkit: Provision Azure Container Apps for inference` komentopalettia käyttäen. Tämän asennuksen aikana sinua pyydetään valitsemaan Azure-tilauksesi ja resurssiryhmäsi.  
![Inferenssiresurssin valmistelu](../../../../../translated_images/command-provision-inference.b294f3ae5764ab45b83246d464ad5329b0de20cf380f75a699b4cc6b5495ca11.fi.png)
   
Oletusarvoisesti inferenssiä varten käytettävän tilauksen ja resurssiryhmän tulisi olla samat kuin hienosäätöä varten. Inferenssi käyttää samaa Azure Container App -ympäristöä ja pääsee käsiksi Azure Files -tallennustilassa sijaitsevaan malliin ja adapteriin, jotka luotiin hienosäätövaiheessa.

## AI Toolkitin käyttö 

### Inferenssin käyttöönotto  
Jos haluat muokata inferenssikoodia tai ladata inferenssimallin uudelleen, suorita `AI Toolkit: Deploy for inference` komento. Tämä synkronoi uusimman koodisi ACA:n kanssa ja käynnistää replikan uudelleen.  

![Inferenssin käyttöönotto](../../../../../translated_images/command-deploy.cb6508c973d6257e649aa4f262d3c170a374da3e9810a4f3d9e03935408a592b.fi.png)

Kun käyttöönotto on onnistuneesti valmis, malli on valmis arvioitavaksi tämän päätepisteen avulla.

### Inferenssi-API:n käyttäminen

Pääset inferenssi-API:in napsauttamalla "*Go to Inference Endpoint*" -painiketta, joka näkyy VSCode-ilmoituksessa. Vaihtoehtoisesti verkkosovelluksen API-päätepiste löytyy kohdasta `ACA_APP_ENDPOINT` tiedostossa `./infra/inference.config.json` ja tulostepaneelista.

![Sovelluksen päätepiste](../../../../../translated_images/notification-deploy.00f4267b7aa6a18cfaaec83a7831b5d09311d5d96a70bb4c9d651ea4a41a8af7.fi.png)

> **Huom:** Inferenssipäätepisteen käyttöönotto voi kestää muutaman minuutin.

## Mallipohjaan sisältyvät inferenssikomponentit
 
| Kansio | Sisältö |
| ------ |--------- |
| `infra` | Sisältää kaikki tarvittavat määritykset etätoimintoja varten. |
| `infra/provision/inference.parameters.json` | Sisältää bicep-mallien parametrit, joita käytetään Azure-resurssien provisiointiin inferenssiä varten. |
| `infra/provision/inference.bicep` | Sisältää mallipohjat Azure-resurssien provisiointiin inferenssiä varten. |
| `infra/inference.config.json` | Määritystiedosto, jonka `AI Toolkit: Provision Azure Container Apps for inference` komento luo. Käytetään muiden etäkomentopalettien syötteenä. |

### AI Toolkitin käyttäminen Azure-resurssien provisioinnin määrittämiseen
Määritä [AI Toolkit](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

Provisionoi Azure Container Apps inferenssiä varten` command.

You can find configuration parameters in `./infra/provision/inference.parameters.json` file. Here are the details:
| Parameter | Description |
| --------- |------------ |
| `defaultCommands` | This is the commands to initiate a web API. |
| `maximumInstanceCount` | This parameter sets the maximum capacity of GPU instances. |
| `location` | This is the location where Azure resources are provisioned. The default value is the same as the chosen resource group's location. |
| `storageAccountName`, `fileShareName` `acaEnvironmentName`, `acaEnvironmentStorageName`, `acaAppName`,  `acaLogAnalyticsName` | These parameters are used to name the Azure resources for provision. By default, they will be same to the fine-tuning resource name. You can input a new, unused resource name to create your own custom-named resources, or you can input the name of an already existing Azure resource if you'd prefer to use that. For details, refer to the section [Using existing Azure Resources](../../../../../md/01.Introduction/03). |

### Using Existing Azure Resources

By default, the inference provision use the same Azure Container App Environment, Storage Account, Azure File Share, and Azure Log Analytics that were used for fine-tuning. A separate Azure Container App is created solely for the inference API. 

If you have customized the Azure resources during the fine-tuning step or want to use your own existing Azure resources for inference, specify their names in the `./infra/inference.parameters.json` tiedosto. Suorita sitten `AI Toolkit: Provision Azure Container Apps for inference` komento komentopalettia käyttäen. Tämä päivittää määritetyt resurssit ja luo puuttuvat.

Esimerkiksi, jos sinulla on olemassa oleva Azure Container -ympäristö, `./infra/finetuning.parameters.json` -tiedostosi tulisi näyttää tältä:

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

### Manuaalinen provisiointi  
Jos haluat määrittää Azure-resurssit manuaalisesti, voit käyttää mukana toimitettuja bicep-tiedostoja kansiossa `./infra/provision` folders. If you have already set up and configured all the Azure resources without using the AI Toolkit command palette, you can simply enter the resource names in the `inference.config.json`.

Esimerkiksi:

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

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty konepohjaisilla tekoälykäännöspalveluilla. Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittistä tietoa varten suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä johtuvista väärinkäsityksistä tai virhetulkinnoista.