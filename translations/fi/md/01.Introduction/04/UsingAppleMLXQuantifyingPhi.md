# **Phi-3.5:n kvantisointi Apple MLX -kehyksen avulla**

MLX on Apple Siliconille kehitetty koneoppimisen tutkimuskehys, jonka on luonut Applen koneoppimisen tutkimustiimi.

MLX on suunniteltu koneoppimisen tutkijoilta koneoppimisen tutkijoille. Kehys on suunniteltu käyttäjäystävälliseksi, mutta samalla tehokkaaksi mallien kouluttamiseen ja käyttöönottoon. Kehyksen rakenne on myös ajatuksellisesti yksinkertainen. Tarkoituksena on helpottaa tutkijoiden mahdollisuuksia laajentaa ja parantaa MLX:ää uusien ideoiden nopeaa tutkimista varten.

LLM-mallit voivat toimia nopeammin Apple Silicon -laitteilla MLX:n avulla, ja malleja voidaan ajaa paikallisesti erittäin kätevästi.

Apple MLX -kehys tukee nyt Phi-3.5-Instruct (**Apple MLX Framework tuki**), Phi-3.5-Vision (**MLX-VLM Framework tuki**) ja Phi-3.5-MoE (**Apple MLX Framework tuki**) kvantisointimuunnosta. Kokeillaan seuraavaksi:

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

### **🤖 Esimerkkejä Phi-3.5:stä Apple MLX:n avulla**

| Laboratoriot | Kuvaus | Siirry |
| -------- | ------- |  ------- |
| 🚀 Lab-Esittely Phi-3.5 Instruct  | Opi käyttämään Phi-3.5 Instruct -mallia Apple MLX -kehyksellä   |  [Siirry](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Lab-Esittely Phi-3.5 Vision (kuva) | Opi käyttämään Phi-3.5 Vision -mallia kuvien analysointiin Apple MLX -kehyksellä     |  [Siirry](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Lab-Esittely Phi-3.5 Vision (moE)   | Opi käyttämään Phi-3.5 MoE -mallia Apple MLX -kehyksellä  |  [Siirry](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **Resurssit**

1. Tutustu Apple MLX -kehykseen [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Apple MLX GitHub Repo [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. MLX-VLM GitHub Repo [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty konepohjaisilla tekoälykäännöspalveluilla. Pyrimme tarkkuuteen, mutta huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä johtuvista väärinkäsityksistä tai virhetulkinnoista.