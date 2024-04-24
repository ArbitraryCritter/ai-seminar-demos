# LLM summarization demo

## Systemkrav

Se [Opsæt Python](../prepare-environment.md)

## summarize.py

Summariserings demoen bruger QWEN modellen udviklet af Alibaba i en meget kompakt udgave.
Modellen har meget begrænset dansk kundskaber i den kompakte udgave, så det er en fordel at bruge engelsk.

Modellen ekserkveres og loader, hvorefter den beder om input til summarisering.

```
python summarize.py
```

Modellen er hovedsageligt udvalgt pga. størrelse og performer godt for sin størrelse, med Engelsk og Kinesisk som primære sprog fokus områder.

## Køretid

Køretiden på en M1 Mac er under 6 sekunder for en summering. Performance på en GPU er mange gange højere.


## Leg med modellen

Prøv med forkellige tekster og sprog. Bemærk at den brugte model er meget begrænset pga. den lille størrelse.

Modellen indeholder en instruks, som er sat til "Please write a short summary of the text". Den kan selvfølgelig udskiftes med andre.

