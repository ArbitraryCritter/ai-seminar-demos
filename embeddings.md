# Tekst embeddings

Embedding modeller tager komplekse egenskaber ved tekst og repræsenterer dem matematisk, f.eks. som vektorer. Disse modeller anvendes typisk til at repræsentere betydningen af teksten.
Når man har genereret embeddings fra et stykke tekst, kan man så bruge forskellige tilgange til at sammenligne tekst stykker.

Bemærk: En embedding vil som udgangspunkt være specifik til den model man bruger, sammenligning af to embeddings der er lavet af to forskellige modeller vil ikke give mening.

## Spændende modeller i det her felt.

### Multilingual-e5-large-instruct er en state-of-the-arti multilanguage instruct embedding model, dvs den kan producere formåls specifikke embeddings.
https://huggingface.co/intfloat/multilingual-e5-large-instruct

### Danish Foundation Models - Sentence encoder medium - En dansk fokuseret embedding model
https://huggingface.co/KennethEnevoldsen/dfm-sentence-encoder-medium-v1

### multilingual-e5-small - Lille men godt performende multilanguage model, der anvendes af Team TYPO3 til semantisk søgning
https://huggingface.co/intfloat/multilingual-e5-small

## Model Benchmarks

### Scandinavian Embedding Benchmark (Enevoldsen)
https://kennethenevoldsen.github.io/scandinavian-embedding-benchmark/

## Online demoer

Embedding modeller er svære at lave gode online demoer af.

http://vectors.nlpl.eu/explore/embeddings/en/#

## Kode demoer

TODO

## Generelle anvendelser:


### Semantisk søgning

Fungerer ved at man først genererer embeddings for alt det man gerne vil søge på. Derefter kan man søge, ved at generere en embedding ud af en søgeterm og sammenligne den med alle de øvrige embeddings.
Der findes såkaldte vektor database tilgange, der gør det muligt at sammenligne med mange millioner vektorer på milisekunder og derved finde de resultater der er tættest på søgningen.

### Kategorisering / Feature extraction / Clustering

Forskellige teknikker til at trække fællestræk ud, enten ved at gruppere sætninger der har embeddings der ligner hinanden (Clustering), ved at trække aspekter af embeddingen ud (feature extraction).
Der findes også såkaldte "instruct" embedding modeller der kan generere embeddings der fokuserer på visse aspekter, ved at man giver dem en sætning der fortæller hvilket aspekt man ønsker embeddingen skal dække.


## Ideer til anvendelse

### Semantisk søgning

Den mest åbenlyse anvendelse er at bruge embeddings som en komponent til at forbedre søgning.

### Skrive quizzer i sprog undervisning

Eftersom de her modeller kan finde ligheder imellem tekst, kan de bruges til at designe skrive øvelser.

- Man kunne f.eks. bede en elev om at summere en artikel og generere embeddings af artiklen og elevens summering og bruge den som en indikation på om det er en god summering.
- På Grundskole niveau kunne man lave synonym quizzer, enten på enkelte ord eller hele sætninger, hvor eleven får en sætning og skal skrive et par ord der har samme betydning.
- Til fremmed sprogs undervisning kunne man bruge embeddings til at lave oversættelses øvelser, hvor eleven skal oversætte en sætning og embeddingen fungerer som validering for om oversættelsen er betydningsmæssigt tæt nok på kildeteksten.
