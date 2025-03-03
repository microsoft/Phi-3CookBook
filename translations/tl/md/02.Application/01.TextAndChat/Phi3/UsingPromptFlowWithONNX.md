# Paggamit ng Windows GPU para gumawa ng Prompt Flow solution gamit ang Phi-3.5-Instruct ONNX

Ang dokumentong ito ay isang halimbawa kung paano gamitin ang PromptFlow kasama ang ONNX (Open Neural Network Exchange) para sa pag-develop ng mga AI application batay sa Phi-3 models.

Ang PromptFlow ay isang hanay ng mga development tools na idinisenyo upang gawing mas madali ang buong development cycle ng LLM-based (Large Language Model) AI applications, mula sa ideation at prototyping hanggang sa testing at evaluation.

Sa pamamagitan ng pagsasama ng PromptFlow at ONNX, maaaring:

- **I-optimize ang Performance ng Modelo**: Gamitin ang ONNX para sa mas mabilis at mahusay na inference at deployment ng modelo.
- **Pinasimpleng Development**: Gamitin ang PromptFlow upang pamahalaan ang workflow at i-automate ang mga paulit-ulit na gawain.
- **Pahusayin ang Kolaborasyon**: Hikayatin ang mas mahusay na pagtutulungan sa mga miyembro ng team sa pamamagitan ng pagbibigay ng iisang development environment.

Ang **Prompt flow** ay isang hanay ng mga development tools na idinisenyo upang gawing mas madali ang buong proseso ng pag-develop ng LLM-based AI applications, mula sa ideation, prototyping, testing, evaluation hanggang sa production deployment at monitoring. Ginagawa nitong mas madali ang prompt engineering at nagbibigay-daan sa iyo na bumuo ng mga LLM apps na may kalidad para sa production.

Ang Prompt flow ay maaaring kumonekta sa OpenAI, Azure OpenAI Service, at mga customizable na modelo (Huggingface, local LLM/SLM). Layunin naming i-deploy ang quantized ONNX model ng Phi-3.5 sa mga lokal na application. Ang Prompt flow ay makakatulong sa atin na mas mahusay na magplano ng ating negosyo at makumpleto ang mga lokal na solusyon batay sa Phi-3.5. Sa halimbawang ito, pagsasamahin natin ang ONNX Runtime GenAI Library upang makumpleto ang Prompt flow solution batay sa Windows GPU.

## **Pag-install**

### **ONNX Runtime GenAI para sa Windows GPU**

Basahin ang gabay na ito upang i-set up ang ONNX Runtime GenAI para sa Windows GPU [click here](./ORTWindowGPUGuideline.md)

### **Pag-set up ng Prompt flow sa VSCode**

1. I-install ang Prompt flow VS Code Extension

![pfvscode](../../../../../../translated_images/pfvscode.79f42ae5dd93ed35c19d6d978ae75831fef40e0b8440ee48b893b5a0597d2260.tl.png)

2. Matapos i-install ang Prompt flow VS Code Extension, i-click ang extension, at piliin ang **Installation dependencies** at sundin ang gabay upang i-install ang Prompt flow SDK sa iyong environment.

![pfsetup](../../../../../../translated_images/pfsetup.0c82d99c7760aac29833b37faf4329e67e22279b1c5f37a73724dfa9ebaa32ee.tl.png)

3. I-download ang [Sample Code](../../../../../../code/09.UpdateSamples/Aug/pf/onnx_inference_pf) at gamitin ang VS Code upang buksan ang sample na ito.

![pfsample](../../../../../../translated_images/pfsample.7bf40b133a558d86356dd6bc0e480bad2659d9c5364823dae9b3e6784e6f2d25.tl.png)

4. Buksan ang **flow.dag.yaml** upang piliin ang iyong Python environment.

![pfdag](../../../../../../translated_images/pfdag.c5eb356fa3a96178cd594de9a5da921c4bbe646a9946f32aa20d344ccbeb51a0.tl.png)

   Buksan ang **chat_phi3_ort.py** upang baguhin ang lokasyon ng iyong Phi-3.5-instruct ONNX Model.

![pfphi](../../../../../../translated_images/pfphi.fff4b0afea47c92c8481174dbf3092823906fca5b717fc642f78947c3e5bbb39.tl.png)

5. Patakbuhin ang iyong prompt flow para sa testing.

Buksan ang **flow.dag.yaml** at i-click ang visual editor.

![pfv](../../../../../../translated_images/pfv.7af6ecd65784a98558b344ba69b5ba6233876823fb435f163e916a632394fc1e.tl.png)

Pagkatapos i-click ito, patakbuhin ito para sa testing.

![pfflow](../../../../../../translated_images/pfflow.9697e0fda67794bb0cf4b78d52e6f5a42002eec935bc2519933064afbbdd34f0.tl.png)

1. Maaari mong patakbuhin ang batch sa terminal upang tingnan ang mas maraming resulta.

```bash

pf run create --file batch_run.yaml --stream --name 'Your eval qa name'    

```

Maaari mong tingnan ang mga resulta sa iyong default na browser.

![pfresult](../../../../../../translated_images/pfresult.972eb57dd5bec646e1aa01148991ba8959897efea396e42cf9d7df259444878d.tl.png)

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang mga serbisyo ng AI na nakabatay sa makina. Bagama't sinisikap naming maging wasto, pakitandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na mapagkakatiwalaang sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.