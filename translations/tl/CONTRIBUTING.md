# Pag-aambag

Tinatanggap ng proyektong ito ang mga kontribusyon at mungkahi. Karamihan sa mga kontribusyon ay nangangailangan ng iyong pagsang-ayon sa isang Contributor License Agreement (CLA) na nagsasaad na may karapatan kang ibigay sa amin ang mga karapatan upang gamitin ang iyong kontribusyon. Para sa mga detalye, bisitahin ang [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com)

Kapag nag-submit ka ng pull request, awtomatikong tutukuyin ng CLA bot kung kailangan mong magbigay ng CLA at lalagyan ng tamang dekorasyon ang PR (hal., status check, komento). Sundin lamang ang mga tagubilin na ibinigay ng bot. Isang beses mo lang itong kailangang gawin para sa lahat ng repos na gumagamit ng aming CLA.

## Code of Conduct

Inampon ng proyektong ito ang [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). Para sa karagdagang impormasyon, basahin ang [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) o makipag-ugnayan sa [opencode@microsoft.com](mailto:opencode@microsoft.com) para sa anumang karagdagang tanong o komento.

## Mga Paalala sa Paglikha ng Isyu

Huwag magbukas ng mga isyu sa GitHub para sa pangkalahatang tanong tungkol sa suporta dahil ang listahan ng GitHub ay dapat gamitin para sa mga mungkahi sa feature at ulat ng bug. Sa ganitong paraan, mas madali naming matutunton ang aktwal na mga isyu o bug mula sa code at maihiwalay ang pangkalahatang talakayan mula sa aktwal na code.

## Paano Mag-ambag

### Mga Alituntunin sa Pull Requests

Kapag nagsusumite ng pull request (PR) sa Phi-3 CookBook repository, gamitin ang sumusunod na mga alituntunin:

- **I-Fork ang Repository**: Laging i-fork ang repository sa iyong sariling account bago gumawa ng mga pagbabago.

- **Hiwalay na pull requests (PR)**:
  - Ihiwalay ang bawat uri ng pagbabago sa sariling pull request. Halimbawa, ang mga pag-aayos ng bug at mga update sa dokumentasyon ay dapat isumite sa magkahiwalay na PR.
  - Ang mga typo at menor de edad na update sa dokumentasyon ay maaaring pagsamahin sa isang PR kung naaangkop.

- **Pamamahala ng merge conflicts**: Kung ang iyong pull request ay may merge conflicts, i-update ang iyong lokal na `main` branch upang mag-mirror sa pangunahing repository bago gumawa ng mga pagbabago.

- **Mga Pagsusumite ng Pagsasalin**: Kapag nagsusumite ng translation PR, tiyaking ang translation folder ay naglalaman ng mga salin para sa lahat ng file sa orihinal na folder.

### Mga Alituntunin sa Pagsasalin

> [!IMPORTANT]
>
> Kapag nagsasalin ng teksto sa repositoryong ito, huwag gumamit ng machine translation. Mag-volunteer lamang para sa mga pagsasalin sa mga wika kung saan ikaw ay bihasa.

Kung ikaw ay bihasa sa isang wikang hindi Ingles, maaari kang tumulong sa pagsasalin ng nilalaman. Sundin ang mga hakbang na ito upang matiyak na maayos na maisasama ang iyong mga kontribusyon sa pagsasalin, gamitin ang sumusunod na mga alituntunin:

- **Lumikha ng translation folder**: Mag-navigate sa naaangkop na seksyon ng folder at lumikha ng translation folder para sa wikang iyong isinasalin. Halimbawa:
  - Para sa seksyong pambungad: `Phi-3CookBook/md/01.Introduce/translations/<language_code>/`
  - Para sa seksyong mabilisang pagsisimula: `Phi-3CookBook/md/02.QuickStart/translations/<language_code>/`
  - Ipagpatuloy ang pattern na ito para sa iba pang seksyon (03.Inference, 04.Finetuning, atbp.)

- **I-update ang mga relative path**: Kapag nagsasalin, ayusin ang istruktura ng folder sa pamamagitan ng pagdaragdag ng `../../` sa simula ng mga relative path sa loob ng markdown files upang matiyak na gumagana nang tama ang mga link. Halimbawa, baguhin tulad ng sumusunod:
  - Baguhin ang `(../../imgs/01/phi3aisafety.png)` sa `(../../../../imgs/01/phi3aisafety.png)`

- **Ayusin ang iyong mga pagsasalin**: Ang bawat naisalin na file ay dapat ilagay sa kaukulang translation folder ng seksyon. Halimbawa, kung isinasalin mo ang pambungad na seksyon sa Espanyol, gagawin mo ito tulad ng sumusunod:
  - `Phi-3CookBook/md/01.Introduce/translations/es/`

- **Mag-submit ng kumpletong PR**: Siguraduhing ang lahat ng naisalin na file para sa isang seksyon ay kasama sa isang PR. Hindi namin tinatanggap ang mga bahagyang pagsasalin para sa isang seksyon. Kapag nagsusumite ng translation PR, tiyaking ang translation folder ay naglalaman ng mga salin para sa lahat ng file sa orihinal na folder.

### Mga Alituntunin sa Pagsusulat

Upang matiyak ang pagkakapare-pareho sa lahat ng dokumento, mangyaring gamitin ang sumusunod na mga alituntunin:

- **Pag-format ng URL**: Balutin ang lahat ng URL sa mga bracket na sinusundan ng mga parentheses, nang walang anumang dagdag na espasyo sa paligid o sa loob nito. Halimbawa: `[example](https://example.com)`.

- **Mga relative link**: Gamitin ang `./` para sa mga relative link na tumuturo sa mga file o folder sa kasalukuyang direktoryo, at `../` para sa mga nasa parent directory. Halimbawa: `[example](../../path/to/file)` o `[example](../../../path/to/file)`.

- **Hindi Country-Specific na mga locale**: Tiyaking ang iyong mga link ay hindi naglalaman ng country-specific na mga locale. Halimbawa, iwasan ang `/en-us/` o `/en/`.

- **Pag-iimbak ng mga imahe**: Iimbak ang lahat ng imahe sa `./imgs` folder.

- **Descriptive na pangalan ng imahe**: Bigyan ng deskriptibong pangalan ang mga imahe gamit ang mga English na karakter, numero, at gitling. Halimbawa: `example-image.jpg`.

## Mga Workflow sa GitHub

Kapag nagsumite ka ng pull request, ang mga sumusunod na workflow ay ma-trigger upang ma-validate ang mga pagbabago. Sundin ang mga tagubilin sa ibaba upang matiyak na ang iyong pull request ay pumasa sa mga workflow check:

- [Suriin ang Broken Relative Paths](../..)
- [Suriin na Walang Locale ang mga URL](../..)

### Suriin ang Broken Relative Paths

Tinitiyak ng workflow na ito na ang lahat ng relative paths sa iyong mga file ay tama.

1. Upang matiyak na gumagana nang tama ang iyong mga link, gawin ang mga sumusunod na gawain gamit ang VS Code:
    - I-hover ang anumang link sa iyong mga file.
    - Pindutin ang **Ctrl + Click** upang pumunta sa link.
    - Kung nag-click ka sa isang link at hindi ito gumana nang lokal, ito ay magti-trigger ng workflow at hindi rin gagana sa GitHub.

1. Upang ayusin ang isyung ito, gawin ang mga sumusunod na gawain gamit ang mga mungkahi ng path na ibinigay ng VS Code:
    - I-type ang `./` o `../`.
    - Magpapakita ang VS Code ng mga opsyon batay sa iyong tinype.
    - Sundan ang path sa pamamagitan ng pag-click sa nais na file o folder upang matiyak na tama ang iyong path.

Kapag naidagdag mo na ang tamang relative path, i-save at i-push ang iyong mga pagbabago.

### Suriin na Walang Locale ang mga URL

Tinitiyak ng workflow na ito na ang anumang web URL ay hindi naglalaman ng country-specific na locale. Dahil ang repositoryong ito ay naa-access sa buong mundo, mahalagang tiyakin na ang mga URL ay walang country locale.

1. Upang matiyak na ang iyong mga URL ay walang country locales, gawin ang mga sumusunod na gawain:

    - Hanapin ang mga text tulad ng `/en-us/`, `/en/`, o anumang iba pang language locale sa mga URL.
    - Kung ang mga ito ay wala sa iyong mga URL, ikaw ay papasa sa check na ito.

1. Upang ayusin ang isyung ito, gawin ang mga sumusunod na gawain:
    - Buksan ang file path na itinuro ng workflow.
    - Alisin ang country locale mula sa mga URL.

Kapag naalis mo na ang country locale, i-save at i-push ang iyong mga pagbabago.

### Suriin ang Broken Urls

Tinitiyak ng workflow na ito na ang anumang web URL sa iyong mga file ay gumagana at nagbabalik ng 200 status code.

1. Upang matiyak na gumagana nang tama ang iyong mga URL, gawin ang mga sumusunod na gawain:
    - Suriin ang status ng mga URL sa iyong mga file.

2. Upang ayusin ang anumang sirang URL, gawin ang mga sumusunod na gawain:
    - Buksan ang file na naglalaman ng sirang URL.
    - I-update ang URL sa tamang isa.

Kapag naayos mo na ang mga URL, i-save at i-push ang iyong mga pagbabago.

> [!NOTE]
>
> Maaaring may mga pagkakataon na ang URL check ay mabigo kahit na ang link ay naa-access. Maaari itong mangyari dahil sa ilang mga dahilan, kabilang ang:
>
> - **Mga limitasyon sa network:** Maaaring may mga limitasyon sa network ang GitHub actions servers na pumipigil sa pag-access sa ilang mga URL.
> - **Mga isyu sa timeout:** Ang mga URL na masyadong matagal tumugon ay maaaring mag-trigger ng timeout error sa workflow.
> - **Mga pansamantalang isyu sa server:** Ang paminsan-minsang downtime ng server o maintenance ay maaaring magdulot ng pansamantalang hindi pag-access ng URL habang nagva-validate.

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang mga serbisyong AI na nakabatay sa makina. Bagamat sinisikap naming maging wasto, mangyaring tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o kamalian. Ang orihinal na dokumento sa sariling wika nito ang dapat ituring na opisyal na sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkaunawa o interpretasyon na dulot ng paggamit ng pagsasaling ito.