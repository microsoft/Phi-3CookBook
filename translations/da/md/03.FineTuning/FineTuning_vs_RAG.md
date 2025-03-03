## Finetuning vs RAG

## Retrieval Augmented Generation

RAG er datahentning + tekstgenerering. Virksomhedens strukturerede og ustrukturerede data lagres i vektordatabasen. Når man søger efter relevant indhold, findes den relevante opsummering og indhold for at danne en kontekst, og tekstgenereringskapaciteten fra LLM/SLM kombineres for at generere indhold.

## RAG Process
![FinetuningvsRAG](../../../../translated_images/rag.36e7cb856f120334d577fde60c6a5d7c5eecae255dac387669303d30b4b3efa4.da.png)

## Fine-tuning
Fine-tuning er baseret på forbedring af en bestemt model. Det er ikke nødvendigt at starte fra bunden med modelalgoritmen, men der skal løbende akkumuleres data. Hvis du ønsker mere præcis terminologi og sproglig udtryksform i industrielle anvendelser, er fine-tuning det bedre valg. Men hvis dine data ofte ændrer sig, kan fine-tuning blive komplekst.

## Hvordan vælger man
Hvis vores svar kræver introduktion af eksterne data, er RAG det bedste valg.

Hvis du har brug for at levere stabil og præcis industrividen, vil fine-tuning være et godt valg. RAG prioriterer at hente relevant indhold, men rammer måske ikke altid de specialiserede nuancer.

Fine-tuning kræver et datasæt af høj kvalitet, og hvis det kun er et lille omfang af data, vil det ikke gøre den store forskel. RAG er mere fleksibelt.  
Fine-tuning er en sort boks, en slags metafysik, og det er svært at forstå den interne mekanisme. Men RAG gør det lettere at finde kilden til dataene, hvilket gør det muligt effektivt at justere hallucinationer eller fejl i indholdet og giver bedre gennemsigtighed.

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af maskinbaserede AI-oversættelsestjenester. Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi er ikke ansvarlige for misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.