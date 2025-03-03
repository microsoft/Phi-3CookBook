Ang demo na ito ay nagpapakita kung paano gamitin ang isang pretrained na modelo upang makabuo ng Python code batay sa isang imahe at isang text prompt.

[Sample Code](../../../../../../code/06.E2E/E2E_OpenVino_Phi3-vision.ipynb)

Narito ang isang hakbang-hakbang na paliwanag:

1. **Imports at Setup**:
   - Ang mga kinakailangang library at module ay ini-import, kabilang ang `requests`, `PIL` para sa pagpoproseso ng imahe, at `transformers` para sa paghawak ng modelo at pagpoproseso.

2. **Pag-load at Pagpapakita ng Imahe**:
   - Ang isang file ng imahe (`demo.png`) ay binubuksan gamit ang library na `PIL` at ipinapakita.

3. **Pagde-define ng Prompt**:
   - Isang mensahe ang nilikha na kinabibilangan ng imahe at isang kahilingan na gumawa ng Python code upang iproseso ang imahe at i-save ito gamit ang `plt` (matplotlib).

4. **Pag-load ng Processor**:
   - Ang `AutoProcessor` ay niloload mula sa isang pretrained na modelo na tinukoy ng `out_dir` na direktoryo. Ang processor na ito ang maghahandle ng text at image inputs.

5. **Paglikha ng Prompt**:
   - Ang method na `apply_chat_template` ay ginagamit upang i-format ang mensahe sa isang prompt na angkop para sa modelo.

6. **Pagpoproseso ng Inputs**:
   - Ang prompt at imahe ay pinoproseso sa mga tensor na maiintindihan ng modelo.

7. **Pag-set ng Generation Arguments**:
   - Ang mga argumento para sa proseso ng generation ng modelo ay tinutukoy, kabilang ang maximum na bilang ng mga bagong token na kailangang mabuo at kung gagamit ng sampling para sa output.

8. **Pagbuo ng Code**:
   - Ang modelo ay bumubuo ng Python code batay sa mga input at generation arguments. Ang `TextStreamer` ay ginagamit upang i-handle ang output, iniiwasan ang prompt at mga special token.

9. **Output**:
   - Ang nabuo na code ay ipiniprinta, na dapat ay naglalaman ng Python code upang iproseso ang imahe at i-save ito ayon sa prompt.

Ang demo na ito ay nagpapakita kung paano magamit ang isang pretrained na modelo gamit ang OpenVino upang dynamic na makabuo ng code batay sa input ng user at mga imahe.

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang mga serbisyo ng AI-based na pagsasalin. Bagama't sinisikap naming maging tumpak, mangyaring tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi tumpak na impormasyon. Ang orihinal na dokumento sa sariling wika nito ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.