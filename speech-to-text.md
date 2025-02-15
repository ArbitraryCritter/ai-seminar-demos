# Speech to text

Speech to text modeller konverterer, som navnet siger, tale til tekst. De findes i mange varianter, nogen fokuseret på enkelte sprog og andre med bred sprog håndtering.
Nogen modeller trækker en tekst strøm ud af en talestrøm, andre kan kende forskel på stemmer og laver en fuld diarisering (transkribering af de enkelte talere).

## Spændende modeller i det her felt.

### OpenAI whisper - Åben ASR model
https://huggingface.co/openai/whisper-large-v3

### Center for Humanities Aarhus/Alvenir - Dansk specifik model
https://huggingface.co/chcaa/xls-r-300m-danish-nst-cv9

## Model Benchmarks

https://huggingface.co/spaces/hf-audio/open_asr_leaderboard
https://picovoice.ai/docs/benchmark/stt/ 
https://huggingface.co/spaces/esb/leaderboard
https://paperswithcode.com/sota/speech-recognition-on-librispeech-test-clean

## Online demoer

# The online demo is slightly tricky to use.
# Press the "Record from browser" button and record some speech with the microphone.
# When you are done, press the "Click to stop recording" button (the same button you use to start recording).
# Finally press the "Compute" button to transcribe the audio.
https://huggingface.co/openai/whisper-large-v3

## Kode demoer

[automatic speech recognition demo](speech-to-text/README.md)

## Generelle anvendelser:

### Speech to text

Helt grundlæggende speech to text, forstå et lydspor og konverter det til tekst.

### Diarisering

Fuld transkribering med separation af talere og understøttelse af overlappende tale.

## Ideer til anvendelse i Gyldendal Uddanelse

### Søgning i lyd/lydspor i video.

Kør ASR på en lydfil og gem den som metadata til filen eller i et søge indeks, således at man kan søge på indholdet.

### 