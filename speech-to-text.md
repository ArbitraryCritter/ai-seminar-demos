# Speech to text

Speech to text modeller konverterer, som navnet siger, tale til tekst. De findes i mange varianter, nogen fokuseret på enkelte sprog.
Nogen modeller trækker en tekst strøm ud af en talestrøm, andre kan kende forskel på stemmer og laver en fuld diarisering (transkribering af de enkelte talere)..

## Spændende modeller i det her felt.

https://huggingface.co/pyannote/speaker-diarization-3.1
### OpenAI whisper - Åben ASR model
https://huggingface.co/openai/whisper-large-v3

## Model Benchmarks

# ASR benchmarks
https://picovoice.ai/docs/benchmark/stt/ 
https://huggingface.co/spaces/esb/leaderboard
https://paperswithcode.com/sota/speech-recognition-on-librispeech-test-clean

## Online demoer



## Kode demoer

[automatic speech recognition](speech-to-text/README.md)

## Generelle anvendelser:

### Speech to text

Helt grundlæggende speech to text, forstå et lydspor og konverter det til tekst.

### Diarisering

Fuld transkribering med separation af talere og understøttelse af overlappende tale.

## Ideer til anvendelse i Gyldendal Uddanelse

### Søgning i lyd/lydspor i video.

Kør ASR på en lydfil og gem den som metadata til filen eller i et søge indeks, således at man kan søge på indholdet.

### 