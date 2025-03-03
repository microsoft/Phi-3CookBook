# Chatbot ya Kielekezi ya Phi 3 Mini 4K Inayoshirikiana na Whisper

## Muhtasari

Chatbot ya Kielekezi ya Phi 3 Mini 4K Inayoshirikiana ni zana inayowezesha watumiaji kuwasiliana na onyesho la Microsoft Phi 3 Mini 4K kupitia maandishi au sauti. Chatbot hii inaweza kutumika kwa kazi mbalimbali, kama vile tafsiri, taarifa za hali ya hewa, na ukusanyaji wa taarifa za jumla.

### Kuanzia

Ili kutumia chatbot hii, fuata maagizo haya:

1. Fungua faili mpya ya [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. Katika dirisha kuu la daftari, utaona kiolesura cha mazungumzo kilicho na kisanduku cha kuingiza maandishi na kitufe cha "Send".
3. Ili kutumia chatbot ya maandishi, andika ujumbe wako kwenye kisanduku cha kuingiza maandishi na bonyeza kitufe cha "Send". Chatbot itajibu kwa faili ya sauti ambayo inaweza kuchezwa moja kwa moja kutoka ndani ya daftari.

**Kumbuka**: Zana hii inahitaji GPU na ufikiaji wa mifano ya Microsoft Phi-3 na OpenAI Whisper, inayotumika kwa utambuzi wa sauti na tafsiri.

### Mahitaji ya GPU

Ili kuendesha onyesho hili unahitaji GPU yenye kumbukumbu ya 12Gb.

Mahitaji ya kumbukumbu ya GPU kwa kuendesha onyesho la **Microsoft-Phi-3-Mini-4K instruct** yatategemea mambo kadhaa, kama vile ukubwa wa data ya kuingiza (sauti au maandishi), lugha inayotumika kwa tafsiri, kasi ya mfano, na kumbukumbu inayopatikana kwenye GPU.

Kwa ujumla, mfano wa Whisper umeundwa kuendeshwa kwenye GPUs. Kiwango cha chini kilichopendekezwa cha kumbukumbu ya GPU kwa kuendesha mfano wa Whisper ni 8 GB, lakini unaweza kushughulikia kumbukumbu kubwa zaidi ikiwa inahitajika.

Ni muhimu kutambua kuwa kuendesha kiasi kikubwa cha data au maombi mengi kwa mfano kunaweza kuhitaji kumbukumbu zaidi ya GPU na/au kusababisha matatizo ya utendaji. Inapendekezwa kujaribu hali yako ya matumizi kwa usanidi tofauti na kufuatilia matumizi ya kumbukumbu ili kubaini mipangilio bora kwa mahitaji yako maalum.

## Mfano wa Mwisho kwa Chatbot ya Kielekezi ya Phi 3 Mini 4K Inayoshirikiana na Whisper

Daftari la Jupyter lenye kichwa [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) linaonyesha jinsi ya kutumia Onyesho la Microsoft Phi 3 Mini 4K ili kuzalisha maandishi kutoka sauti au maandishi yaliyoingizwa. Daftari linafafanua kazi kadhaa:

1. `tts_file_name(text)`: Kazi hii inazalisha jina la faili kulingana na maandishi yaliyoingizwa kwa ajili ya kuhifadhi faili ya sauti iliyotengenezwa.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Kazi hii hutumia API ya Edge TTS kuzalisha faili ya sauti kutoka kwenye orodha ya vipande vya maandishi yaliyoingizwa. Vigezo vya kuingiza ni orodha ya vipande, kiwango cha sauti, jina la sauti, na njia ya kuhifadhi faili ya sauti iliyotengenezwa.
1. `talk(input_text)`: Kazi hii inazalisha faili ya sauti kwa kutumia API ya Edge TTS na kuihifadhi kwa jina la faili la nasibu katika saraka ya /content/audio. Kigezo cha kuingiza ni maandishi ya kugeuzwa kuwa sauti.
1. `run_text_prompt(message, chat_history)`: Kazi hii hutumia onyesho la Microsoft Phi 3 Mini 4K kuzalisha faili ya sauti kutoka kwa ujumbe uliowekwa na kuuongeza kwenye historia ya mazungumzo.
1. `run_audio_prompt(audio, chat_history)`: Kazi hii hubadilisha faili ya sauti kuwa maandishi kwa kutumia API ya mfano wa Whisper na kuyapitisha kwa `run_text_prompt()`.
1. Msimbo huanzisha programu ya Gradio inayoruhusu watumiaji kuingiliana na onyesho la Phi 3 Mini 4K kwa kuandika ujumbe au kupakia faili za sauti. Matokeo yanaonyeshwa kama ujumbe wa maandishi ndani ya programu.

## Kutatua Tatizo

Kufunga madereva ya Cuda GPU

1. Hakikisha programu zako za Linux zimesasishwa

    ```bash
    sudo apt update
    ```

1. Funga Madereva ya Cuda

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. Sajili eneo la dereva la cuda

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. Kuangalia ukubwa wa kumbukumbu ya Nvidia GPU (Inahitajika 12GB ya Kumbukumbu ya GPU)

    ```bash
    nvidia-smi
    ```

1. Futa Akiba: Ikiwa unatumia PyTorch, unaweza kuita torch.cuda.empty_cache() ili kuachilia kumbukumbu zote ambazo hazitumiki ili zitumike na programu zingine za GPU.

    ```python
    torch.cuda.empty_cache() 
    ```

1. Kuangalia Nvidia Cuda

    ```bash
    nvcc --version
    ```

1. Fanya kazi zifuatazo ili kuunda tokeni ya Hugging Face.

    - Tembelea [Ukurasa wa Mipangilio ya Tokeni ya Hugging Face](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
    - Chagua **Tokeni Mpya**.
    - Weka **Jina** la mradi unaotaka kutumia.
    - Chagua **Aina** kuwa **Andika**.

> **Kumbuka**
>
> Ikiwa unakutana na kosa lifuatalo:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> Ili kutatua hili, andika amri ifuatayo ndani ya terminal yako.
>
> ```bash
> sudo ldconfig
> ```

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma za kutafsiri za AI zinazotegemea mashine. Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya asili inapaswa kuzingatiwa kama chanzo rasmi. Kwa taarifa muhimu, inashauriwa kutumia huduma za wataalamu wa tafsiri za kibinadamu. Hatutawajibika kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.