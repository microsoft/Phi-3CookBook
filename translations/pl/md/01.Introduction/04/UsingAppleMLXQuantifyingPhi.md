# **Kwantyzacja Phi-3.5 przy użyciu Apple MLX Framework**

MLX to framework tablicowy przeznaczony do badań nad uczeniem maszynowym na urządzeniach z Apple Silicon, stworzony przez Apple Machine Learning Research.

MLX został zaprojektowany przez badaczy uczenia maszynowego dla badaczy uczenia maszynowego. Framework ma być przyjazny dla użytkownika, a jednocześnie wydajny w treningu i wdrażaniu modeli. Jego konstrukcja jest również koncepcyjnie prosta, co ma na celu ułatwienie badaczom rozszerzania i ulepszania MLX, aby szybko eksplorować nowe pomysły.

LLM mogą być przyspieszane na urządzeniach z Apple Silicon za pomocą MLX, a modele można uruchamiać lokalnie w bardzo wygodny sposób.

Obecnie Apple MLX Framework obsługuje konwersję kwantyzacji Phi-3.5-Instruct (**obsługa Apple MLX Framework**), Phi-3.5-Vision (**obsługa MLX-VLM Framework**) oraz Phi-3.5-MoE (**obsługa Apple MLX Framework**). Spróbujmy:

### **Phi-3.5-Instruct**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3.5-mini-instruct -q

```

### **Phi-3.5-Vision**

```bash

python -m mlxv_lm.convert --hf-path microsoft/Phi-3.5-vision-instruct -q

```

### **Phi-3.5-MoE**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3.5-MoE-instruct  -q

```

### **🤖 Przykłady dla Phi-3.5 z Apple MLX**

| Laboratoria | Opis | Przejdź |
| -------- | ------- |  ------- |
| 🚀 Lab-Introduce Phi-3.5 Instruct  | Dowiedz się, jak używać Phi-3.5 Instruct z frameworkiem Apple MLX   |  [Przejdź](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (image) | Dowiedz się, jak używać Phi-3.5 Vision do analizy obrazów za pomocą frameworka Apple MLX     |  [Przejdź](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (moE)   | Dowiedz się, jak używać Phi-3.5 MoE z frameworkiem Apple MLX  |  [Przejdź](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **Zasoby**

1. Dowiedz się więcej o Apple MLX Framework [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Repozytorium Apple MLX na GitHubie [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. Repozytorium MLX-VLM na GitHubie [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony za pomocą usług tłumaczenia maszynowego opartego na sztucznej inteligencji. Chociaż dokładamy wszelkich starań, aby tłumaczenie było precyzyjne, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za wiążące źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.