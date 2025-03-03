# Kuchangia

Mradi huu unakaribisha michango na mapendekezo. Michango mingi inahitaji ukubaliane na Mkataba wa Leseni ya Mchangiaji (CLA) unaothibitisha kuwa una haki ya, na kweli unatoa, haki kwetu kutumia mchango wako. Kwa maelezo zaidi, tembelea [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com)

Unapowasilisha ombi la kuvuta (pull request), roboti ya CLA itaamua moja kwa moja kama unahitaji kutoa CLA na kuweka alama kwenye PR ipasavyo (mfano, ukaguzi wa hali, maoni). Fuata tu maagizo yaliyotolewa na roboti. Utahitaji kufanya hivi mara moja tu kwa hazina zote zinazotumia CLA yetu.

## Kanuni za Maadili

Mradi huu umechukua [Kanuni za Maadili za Microsoft Open Source](https://opensource.microsoft.com/codeofconduct/). 
Kwa maelezo zaidi soma [Maswali Yanayoulizwa Mara kwa Mara ya Kanuni za Maadili](https://opensource.microsoft.com/codeofconduct/faq/) au wasiliana na [opencode@microsoft.com](mailto:opencode@microsoft.com) kwa maswali au maoni ya ziada.

## Tahadhari kwa Kufungua Masuala

Tafadhali usifungue masuala ya GitHub kwa maswali ya msaada wa jumla kwani orodha ya GitHub inapaswa kutumiwa kwa maombi ya vipengele na ripoti za hitilafu. Hii inatufanya tuweze kufuatilia masuala halisi au hitilafu kutoka kwenye msimbo na kutenganisha majadiliano ya jumla na msimbo halisi.

## Jinsi ya Kuchangia

### Miongozo ya Ombi la Kuvuta (Pull Request)

Unapowasilisha ombi la kuvuta (PR) kwenye hazina ya Phi-3 CookBook, tafadhali fuata miongozo ifuatayo:

- **Fanya Fork ya Hazina**: Daima fanya fork ya hazina kwenye akaunti yako mwenyewe kabla ya kufanya mabadiliko yako.

- **Tenganisha maombi ya kuvuta (PR)**:
  - Wasilisha kila aina ya mabadiliko katika ombi lake la kuvuta. Kwa mfano, marekebisho ya hitilafu na masasisho ya nyaraka yanapaswa kuwasilishwa katika PR tofauti.
  - Marekebisho ya makosa ya herufi na masasisho madogo ya nyaraka yanaweza kuunganishwa katika PR moja inapofaa.

- **Shughulikia migogoro ya muunganiko**: Ikiwa ombi lako la kuvuta linaonyesha migogoro ya muunganiko, sasisha tawi lako la ndani la `main` kulinganisha na hazina kuu kabla ya kufanya mabadiliko yako.

- **Maoni ya tafsiri**: Unapowasilisha PR ya tafsiri, hakikisha kwamba folda ya tafsiri inajumuisha tafsiri za faili zote katika folda ya asili.

### Miongozo ya Tafsiri

> [!IMPORTANT]
>
> Unapofanya tafsiri ya maandishi katika hazina hii, usitumie tafsiri ya mashine. Jitolee tu kwa tafsiri katika lugha ambazo unazifahamu vizuri.

Ikiwa unafahamu lugha isiyo ya Kiingereza, unaweza kusaidia kutafsiri maudhui. Fuata hatua hizi kuhakikisha michango yako ya tafsiri imeunganishwa ipasavyo, tafadhali tumia miongozo ifuatayo:

- **Unda folda ya tafsiri**: Nenda kwenye folda ya sehemu husika na uunde folda ya tafsiri kwa lugha unayochangia. Kwa mfano:
  - Kwa sehemu ya utangulizi: `PhiCookBook/md/01.Introduce/translations/<language_code>/`
  - Kwa sehemu ya kuanza haraka: `PhiCookBook/md/02.QuickStart/translations/<language_code>/`
  - Endelea na muundo huu kwa sehemu nyingine (03.Inference, 04.Finetuning, nk.)

- **Sasisha njia za jamaa**: Unapofanya tafsiri, rekebisha muundo wa folda kwa kuongeza `../../` mwanzoni mwa njia za jamaa ndani ya faili za markdown ili kuhakikisha viungo vinafanya kazi ipasavyo. Kwa mfano, badilisha kama ifuatavyo:
  - Badilisha `(../../imgs/01/phi3aisafety.png)` kuwa `(../../../../imgs/01/phi3aisafety.png)`

- **Panga tafsiri zako**: Kila faili iliyotafsiriwa inapaswa kuwekwa katika folda ya tafsiri ya sehemu husika. Kwa mfano, ikiwa unatafsiri sehemu ya utangulizi kwa Kihispania, ungeunda kama ifuatavyo:
  - `PhiCookBook/md/01.Introduce/translations/es/`

- **Wasilisha PR kamili**: Hakikisha faili zote zilizotafsiriwa kwa sehemu moja zimejumuishwa katika PR moja. Hatukubali tafsiri za sehemu kwa sehemu. Unapowasilisha PR ya tafsiri, hakikisha kwamba folda ya tafsiri inajumuisha tafsiri za faili zote katika folda ya asili.

### Miongozo ya Uandishi

Ili kuhakikisha uthabiti katika nyaraka zote, tafadhali tumia miongozo ifuatayo:

- **Muundo wa URL**: Weka URL zote kwenye mabano ya mraba ikifuatiwa na mabano ya kawaida, bila nafasi za ziada ndani au nje. Kwa mfano: `[example](https://www.microsoft.com)`.

- **Viungo vya jamaa**: Tumia `./` kwa viungo vya jamaa vinavyoelekeza kwenye faili au folda katika saraka ya sasa, na `../` kwa zile zilizo kwenye saraka ya mzazi. Kwa mfano: `[example](../../path/to/file)` au `[example](../../../path/to/file)`.

- **Locales zisizo za Nchi Maalum**: Hakikisha viungo vyako havijumuishi locales za nchi maalum. Kwa mfano, epuka `/en-us/` au `/en/`.

- **Uhifadhi wa picha**: Hifadhi picha zote kwenye folda ya `./imgs`.

- **Majina ya picha yenye maelezo**: Peana majina ya picha kwa maelezo kwa kutumia herufi za Kiingereza, nambari, na mistari ya kati. Kwa mfano: `example-image.jpg`.

## Michakato ya Kazi ya GitHub

Unapowasilisha ombi la kuvuta, michakato ya kazi ifuatayo itazinduliwa ili kuthibitisha mabadiliko. Fuata maagizo hapa chini kuhakikisha ombi lako la kuvuta linapita ukaguzi wa michakato ya kazi:

- [Angalia Njia za Jamaa Zilizovunjika](../..)
- [Angalia URLs Zisizo na Locale](../..)

### Angalia Njia za Jamaa Zilizovunjika

Mchakato huu unahakikisha kuwa njia zote za jamaa katika faili zako ziko sahihi.

1. Ili kuhakikisha viungo vyako vinafanya kazi ipasavyo, fanya kazi zifuatazo ukitumia VS Code:
    - Peleka mshale juu ya kiungo chochote katika faili zako.
    - Bonyeza **Ctrl + Click** ili kwenda kwenye kiungo.
    - Ikiwa utabonyeza kiungo na hakifanyi kazi kwa ndani, kitaanzisha mchakato na hakitafanya kazi kwenye GitHub.

1. Ili kurekebisha suala hili, fanya kazi zifuatazo ukitumia mapendekezo ya njia yanayotolewa na VS Code:
    - Andika `./` au `../`.
    - VS Code itakupa chaguo kulingana na ulichotaja.
    - Fuata njia kwa kubonyeza faili au folda unayotaka kuhakikisha njia yako ni sahihi.

Baada ya kuongeza njia sahihi ya jamaa, hifadhi na sukuma mabadiliko yako.

### Angalia URLs Zisizo na Locale

Mchakato huu unahakikisha kwamba URL yoyote ya wavuti haina locale ya nchi maalum. Kwa kuwa hazina hii inapatikana kimataifa, ni muhimu kuhakikisha kwamba URL hazijumuishi locale ya nchi yako.

1. Ili kuthibitisha kwamba URL zako hazina locales za nchi, fanya kazi zifuatazo:

    - Angalia maandishi kama `/en-us/`, `/en/`, au locale nyingine yoyote ya lugha kwenye URL.

    - Ikiwa haya hayapo kwenye URL zako, basi utapita ukaguzi huu.

1. Ili kurekebisha suala hili, fanya kazi zifuatazo:
    - Fungua njia ya faili iliyoangaziwa na mchakato.
    - Ondoa locale ya nchi kutoka kwa URL.

Baada ya kuondoa locale ya nchi, hifadhi na sukuma mabadiliko yako.

### Angalia URLs Zilizovunjika

Mchakato huu unahakikisha kwamba URL yoyote ya wavuti katika faili zako inafanya kazi na inarudisha msimbo wa hali ya 200.

1. Ili kuthibitisha kwamba URL zako zinafanya kazi ipasavyo, fanya kazi zifuatazo:
    - Angalia hali ya URL katika faili zako.

2. Ili kurekebisha URL zozote zilizovunjika, fanya kazi zifuatazo:
    - Fungua faili yenye URL iliyovunjika.
    - Sasisha URL kwa ile sahihi.

Baada ya kurekebisha URL, hifadhi na sukuma mabadiliko yako.

> [!NOTE]
>
> Kunaweza kuwa na hali ambapo ukaguzi wa URL unashindwa hata kama kiungo kinaweza kufikiwa. Hii inaweza kutokea kwa sababu kadhaa, ikiwa ni pamoja na:
>
> - **Vizuizi vya mtandao:** Seva za GitHub actions zinaweza kuwa na vizuizi vya mtandao vinavyokataza ufikiaji wa URL fulani.
> - **Masuala ya muda wa kusubiri:** URL zinazochukua muda mrefu kujibu zinaweza kusababisha hitilafu ya muda wa kusubiri kwenye mchakato.
> - **Masuala ya muda mfupi ya seva:** Wakati mwingine matatizo ya seva au matengenezo yanaweza kufanya URL isiweze kupatikana kwa muda wakati wa uthibitishaji.

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma za tafsiri za AI zinazotegemea mashine. Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati asilia katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha kuaminika. Kwa taarifa muhimu, inashauriwa kutumia tafsiri ya kitaalamu ya binadamu. Hatutawajibika kwa kutokuelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.