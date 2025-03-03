# Hienosäädä Phi3 Olivea käyttäen

Tässä esimerkissä käytät Olivea:

1. Hienosäätääksesi LoRA-adapterin luokittelemaan lauseet kategorioihin Surullinen, Ilo, Pelko, Yllätys.
1. Yhdistääksesi adapterin painot perusmalliin.
1. Optimoidaksesi ja kvantisoidaksesi mallin muotoon `int4`.

Näytämme myös, kuinka voit tehdä päättelyä hienosäädetyllä mallilla ONNX Runtime (ORT) Generate API:n avulla.

> **⚠️ Hienosäätöä varten tarvitset sopivan GPU:n, kuten A10, V100, A100.**

## 💾 Asenna

Luo uusi Python-virtuaaliympäristö (esimerkiksi käyttäen `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Seuraavaksi asenna Olive ja hienosäätötyönkulun riippuvuudet:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Hienosäädä Phi3 Olivea käyttäen
[Olive-konfiguraatiotiedosto](../../../../../code/03.Finetuning/olive-ort-example/phrase-classification.json) sisältää *työnkulun*, jossa on seuraavat *vaiheet*:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

Korkean tason näkökulmasta tämä työnkulku tekee seuraavaa:

1. Hienosäätää Phi3:n (150 askelta, joita voit muokata) käyttäen [dataset/data-classification.json](../../../../../code/03.Finetuning/olive-ort-example/dataset/dataset-classification.json) -dataa.
1. Yhdistää LoRA-adapterin painot perusmalliin. Tämä tuottaa yhden mallin artefaktin ONNX-muodossa.
1. Model Builder optimoi mallin ONNX-runtimea varten *ja* kvantisoi mallin muotoon `int4`.

Suorita työnkulku komennolla:

```bash
olive run --config phrase-classification.json
```

Kun Olive on valmis, optimoitu `int4` hienosäädetty Phi3-malli löytyy sijainnista: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Integroi hienosäädetty Phi3 sovellukseesi 

Suorita sovellus:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

Vastaus tulisi olla yksittäinen sanaluokitus lauseelle (Surullinen/Ilo/Pelko/Yllätys).

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty konepohjaisilla tekoälykäännöspalveluilla. Pyrimme tarkkuuteen, mutta huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulee pitää ensisijaisena lähteenä. Kriittisen tiedon kohdalla suositellaan ammattimaista ihmisen tekemää käännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinkäsityksistä tai tulkintavirheistä.