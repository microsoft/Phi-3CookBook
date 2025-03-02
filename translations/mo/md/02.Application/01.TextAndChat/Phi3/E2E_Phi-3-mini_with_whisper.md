# Phi 3 Mini 4K Instruct Chatbot ma Whisper Chatbot

## Koondhiga

Phi 3 Mini 4K Instruct Chatbot waa aalad u oggolaanaysa isticmaalayaasha inay ku falgalaan demo-ga Microsoft Phi 3 Mini 4K Instruct iyaga oo adeegsanaya qoraal ama cod. Chatbot-kan waxaa loo isticmaali karaa hawlo kala duwan, sida tarjumaadda, helitaanka warbixin ku saabsan cimilada, iyo xog-ururin guud.

### Sida Loo Bilaabo

Si aad u isticmaasho chatbot-kan, raac tilmaamahan:

1. Fur [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. Daaqadda ugu weyn ee notebook-ka, waxaad arki doontaa sanduuqa sheekaysiga oo leh meel qoraalka lagu geliyo iyo badhanka "Send".
3. Si aad u isticmaasho chatbot-ka ku saleysan qoraalka, ku qor fariintaada sanduuqa qoraalka oo guji badhanka "Send". Chatbot-ku wuxuu ku siin doonaa fayl cod ah oo si toos ah uga ciyaari kara gudaha notebook-ka.

**Ogsoonow**: Aaladdan waxay u baahan tahay GPU iyo marin u helidda moodooyinka Microsoft Phi-3 iyo OpenAI Whisper, kuwaas oo loo isticmaalo aqoonsiga hadalka iyo tarjumaadda.

### Shuruudaha GPU-ga

Si aad u maamusho demo-gan, waxaad u baahan tahay 12GB oo xasuusta GPU ah.

Shuruudaha xasuusta GPU-ga ee loogu baahan yahay demo-ga **Microsoft-Phi-3-Mini-4K instruct** waxay ku xirnaan doonaan dhowr arrimood, sida cabbirka xogta la geliyo (cod ama qoraal), luqadda loo adeegsado tarjumaadda, xawaaraha moodelka, iyo xasuusta GPU-ga ee la heli karo.

Guud ahaan, moodelka Whisper waxaa loogu talagalay inuu ku shaqeeyo GPU-yada. Xaddiga ugu yar ee xasuusta GPU-ga ee lagu taliyay si loo maamulo moodelka Whisper waa 8 GB, laakiin wuxuu awood u leeyahay inuu maareeyo xasuus ka badan haddii loo baahdo.

Waa muhiim in la ogaado in maareynta xog badan ama codsiyo fara badan oo ku socda moodelka laga yaabo inay u baahan tahay xasuus badan oo GPU ah iyo/ama inay keento dhibaatooyin waxqabad. Waxaa lagula talinayaa inaad tijaabiso xaaladdaada isticmaale iyadoo la adeegsanayo qaabeymo kala duwan oo aad la socoto isticmaalka xasuusta si aad u go'aamiso qaabeynta ugu habboon ee baahiyahaaga gaarka ah.

## Tusaale E2E ah oo loogu talagalay Phi 3 Mini 4K Instruct Chatbot ma Whisper

Notebook-ka jupyter ee cinwaankiisu yahay [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) wuxuu muujinayaa sida loo isticmaalo Demo-ga Microsoft Phi 3 Mini 4K Instruct si loo abuuro qoraal laga soo saaray cod ama qoraal la geliyo. Notebook-ka wuxuu qeexayaa dhowr hawlood:

1. `tts_file_name(text)`: Hawshan waxay soo saartaa magaca faylka iyadoo ku saleysan qoraalka la geliyay si loogu keydiyo faylka codka la abuuray.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Hawshan waxay adeegsataa Edge TTS API si ay u abuurto fayl cod ah oo ka kooban qaybo qoraal ah oo la geliyay. Halbeegyada gelinta waa liiska qaybo, heerka codka, magaca codka, iyo meesha loo keydiyo faylka codka la abuuray.
1. `talk(input_text)`: Hawshan waxay soo saartaa fayl cod ah iyadoo la adeegsanayo Edge TTS API oo lagu keydiyo magac fayl random ah gudaha galka /content/audio. Halbeegga gelinta waa qoraalka loo beddelayo cod.
1. `run_text_prompt(message, chat_history)`: Hawshan waxay isticmaashaa demo-ga Microsoft Phi 3 Mini 4K instruct si ay u abuurto fayl cod ah oo laga soo saaray fariin la geliyay oo ay ku darto taariikhda sheekaysiga.
1. `run_audio_prompt(audio, chat_history)`: Hawshan waxay u beddeshaa fayl cod ah qoraal iyadoo la adeegsanayo Whisper model API oo ay u gudbisaa `run_text_prompt()`.
1. Koodhka wuxuu bilaabayaa Gradio app oo u oggolaanaya isticmaalayaasha inay ku falgalaan demo-ga Phi 3 Mini 4K instruct iyaga oo gelinaya fariimo qoraal ah ama soo gelinaya faylasha codka. Natiijada waxaa lagu soo bandhigaa sida fariin qoraal ah gudaha app-ka.

## Xallinta Dhibaatooyinka

Ku rakibidda darawallada Cuda GPU

1. Hubi in barnaamijyada Linux-kaaga ay cusboon yihiin

    ```bash
    sudo apt update
    ```

1. Ku rakib darawallada Cuda

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. Diiwaangeli meesha darawalka cuda

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. Hubi cabbirka xasuusta Nvidia GPU (Waxaa loo baahan yahay 12GB oo xasuusta GPU ah)

    ```bash
    nvidia-smi
    ```

1. Nadiifi Cache: Haddii aad isticmaalayso PyTorch, waad wici kartaa torch.cuda.empty_cache() si aad u sii dayso dhammaan xasuusta aan la isticmaalin si ay ugu adeegto barnaamijyada kale ee GPU.

    ```python
    torch.cuda.empty_cache() 
    ```

1. Hubinta Nvidia Cuda

    ```bash
    nvcc --version
    ```

1. Samee hawlahan si aad u abuurto token Hugging Face.

    - U gudub [Bogga Dejinta Token-ka Hugging Face](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
    - Xulo **New token**.
    - Geli magaca mashruuca **Name** ee aad rabto inaad isticmaasho.
    - Xulo nooca **Type** inuu noqdo **Write**.

> **Ogsoonow**
>
> Haddii aad la kulanto qaladka soo socda:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> Si aad tan u xalliso, geli amarkan hoosta terminal-kaaga.
>
> ```bash
> sudo ldconfig
> ```

It seems like "mo" might refer to a specific language or abbreviation, but it is unclear which language you're referring to. Could you please clarify or specify the target language you'd like the text translated into? For example, "mo" could potentially stand for Maori, Mongolian, or another language.