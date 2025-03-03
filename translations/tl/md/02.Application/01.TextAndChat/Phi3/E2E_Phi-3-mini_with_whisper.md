# Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper

## Pangkalahatang-ideya

Ang Interactive Phi 3 Mini 4K Instruct Chatbot ay isang tool na nagbibigay-daan sa mga gumagamit na makipag-ugnayan sa Microsoft Phi 3 Mini 4K instruct demo gamit ang text o audio input. Ang chatbot ay maaaring gamitin para sa iba't ibang gawain tulad ng pagsasalin, pagkuha ng ulat ng panahon, at pangkalahatang impormasyon.

### Paano Magsimula

Para magamit ang chatbot na ito, sundin lamang ang mga sumusunod na hakbang:

1. Buksan ang [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb).
2. Sa pangunahing window ng notebook, makikita mo ang isang chatbox interface na may text input box at isang "Send" na button.
3. Para magamit ang text-based na chatbot, i-type lamang ang iyong mensahe sa text input box at i-click ang "Send" na button. Ang chatbot ay tutugon gamit ang isang audio file na maaaring i-play direkta mula sa loob ng notebook.

**Tandaan**: Ang tool na ito ay nangangailangan ng GPU at access sa Microsoft Phi-3 at OpenAI Whisper models, na ginagamit para sa speech recognition at pagsasalin.

### Mga Pangangailangan sa GPU

Upang magamit ang demo na ito, kailangan mo ng 12Gb na GPU memory.

Ang mga memory requirements para sa pagpapatakbo ng **Microsoft-Phi-3-Mini-4K instruct** demo sa isang GPU ay nakadepende sa ilang mga salik, tulad ng laki ng input data (audio o text), wika na ginagamit para sa pagsasalin, bilis ng modelo, at magagamit na memorya sa GPU.

Sa pangkalahatan, ang Whisper model ay idinisenyo upang tumakbo sa GPUs. Ang inirerekomendang minimum na GPU memory para sa pagpapatakbo ng Whisper model ay 8 GB, ngunit maaari itong magamit ng mas malaking memory kung kinakailangan.

Mahalagang tandaan na ang pagproseso ng malaking dami ng data o mataas na volume ng mga kahilingan sa modelo ay maaaring mangailangan ng mas malaking GPU memory at/o magdulot ng mga isyu sa performance. Inirerekomenda na subukan ang iyong use case gamit ang iba't ibang configuration at i-monitor ang memory usage upang matukoy ang pinakamainam na mga setting para sa iyong partikular na pangangailangan.

## E2E Halimbawa para sa Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper

Ang jupyter notebook na pinamagatang [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) ay nagpapakita kung paano gamitin ang Microsoft Phi 3 Mini 4K instruct Demo upang lumikha ng text mula sa audio o nakasulat na text input. Ang notebook ay naglalaman ng ilang mga function:

1. `tts_file_name(text)`: Ang function na ito ay lumilikha ng pangalan ng file batay sa input text para sa pag-save ng generated audio file.
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: Ang function na ito ay gumagamit ng Edge TTS API upang lumikha ng audio file mula sa listahan ng mga chunks ng input text. Ang mga input parameters ay ang listahan ng chunks, speech rate, voice name, at output path para sa pag-save ng generated audio file.
1. `talk(input_text)`: Ang function na ito ay lumilikha ng audio file gamit ang Edge TTS API at sine-save ito sa isang random na pangalan ng file sa /content/audio directory. Ang input parameter ay ang input text na iko-convert sa speech.
1. `run_text_prompt(message, chat_history)`: Ang function na ito ay gumagamit ng Microsoft Phi 3 Mini 4K instruct demo upang lumikha ng audio file mula sa message input at idinadagdag ito sa chat history.
1. `run_audio_prompt(audio, chat_history)`: Ang function na ito ay nagko-convert ng audio file sa text gamit ang Whisper model API at ipinapasa ito sa `run_text_prompt()` function.
1. Ang code ay naglulunsad ng Gradio app na nagbibigay-daan sa mga gumagamit na makipag-ugnayan sa Phi 3 Mini 4K instruct demo sa pamamagitan ng pag-type ng mga mensahe o pag-upload ng mga audio file. Ang output ay ipinapakita bilang text message sa loob ng app.

## Pagsusuri ng Problema

Pag-install ng Cuda GPU drivers

1. Siguraduhing up-to-date ang iyong Linux application

    ```bash
    sudo apt update
    ```

1. I-install ang Cuda Drivers

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. Irehistro ang lokasyon ng cuda driver

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. Suriin ang laki ng Nvidia GPU memory (Kinakailangan: 12GB ng GPU Memory)

    ```bash
    nvidia-smi
    ```

1. Empty Cache: Kung gumagamit ka ng PyTorch, maaari mong tawagan ang torch.cuda.empty_cache() upang i-release ang lahat ng hindi ginagamit na cached memory upang magamit ito ng iba pang GPU applications.

    ```python
    torch.cuda.empty_cache() 
    ```

1. Suriin ang Nvidia Cuda

    ```bash
    nvcc --version
    ```

1. Gawin ang mga sumusunod na hakbang upang lumikha ng Hugging Face token.

    - Pumunta sa [Hugging Face Token Settings page](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo).
    - Piliin ang **New token**.
    - Ilagay ang **Pangalan** ng proyekto na nais mong gamitin.
    - Piliin ang **Uri** na **Write**.

> **Tandaan**
>
> Kung makaranas ka ng sumusunod na error:
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> Upang maayos ito, i-type ang sumusunod na command sa iyong terminal.
>
> ```bash
> sudo ldconfig
> ```

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang mga serbisyong AI na nakabatay sa makina. Bagama't pinagsusumikapan namin ang katumpakan, mangyaring tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi tumpak na impormasyon. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na mapagkakatiwalaang sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.