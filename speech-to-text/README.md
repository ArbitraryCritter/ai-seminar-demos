# ASR demo

## Systemkrav

Se [Opsæt Python](../prepare-environment.md)

## asr.py

ASR demoen bruger den nyeste åbne OpenAI - Whisper model, til at transkribere en mp3 fil. Den understøtter ca. 100 sprog inklusiv dansk.
Dens performance på Engelsk er "state of the art" og performancen på Dansk er også ganske imponerende.

Eksemplet inkluderer en eksempel .mp3 fil , der er genereret med Polly. Teksten er taget fra "naturgeografiportalen.systime.dk".

Teksten er:

"Når vi taler om vejret, beskriver vi temperatur, tryk, nedbør og vind på et givent tidspunkt og sted på Jordens overflade. Med begrebet klima beskriver og forklarer vi disse forhold for Jorden og dens atmosfære som helhed og over længere tid. Klimatologien lærer os om Solens indstråling som den bagvedliggende drivkraft i dannelsen af forskelle i temperaturer og atmosfærisk tryk og dermed cirkulation. Og den lærer os, hvordan disse forskelle igen skaber forskelle i vind og nedbør og dermed livsvilkår forskellige steder på Jorden og på forskellige årstider."

Modellen kan køres sådan her:
```
python asr.py speech_20240424084126714.mp3
```

## Køretid

På en M1 Mac afviklet på CPU, tager modellen ca. 2 sekunder for hvert 1 sekund lyd der processeres. Intel køretid bør være tilsvarende.
Afviklet på dedikeret Nvidia hardware kan modellen køre ca. 13:1, dvs. 1 sekund for hver 13 sekunder lyd.

Alt tider er vejledende.


## Leg med modellen

Sammenlign eksempel filen med teksten. Bemærk at det der er mindre fejl i transkriberingen.
Prøv med andre MP3 filer der indeholder stemmer.
