# Large language models

Large language models er modeller med et bredt anvendelsesfelt indenfor tekst processering.
De kan bruges til at summere tekst, svare på spørgsmål og til forskellige typer klassificerings opgaver.

Deres primære svaghed er at det typisk er meget tunge modeller, der kræver betydelig processeringskraft, derudover er de tilbøjelige til hallucinere og derved mindre pålidelige end andre typer modeller.

Der er ofte nødvendige at fine-tune LLM modeller til et specifikt formål, for at få pålidelig performance ud af dem.

## Spændende modeller i det her felt.

Starling LM 7b beta er en afart af Mistral 7B v.0.1, med forbedret performance på Dansk.
- https://huggingface.co/Nexusflow/Starling-LM-7B-beta

Mistral 7B v.0.2 - En af de få rent Europæisk udviklede modeller og fundament for mange åbne modeller.
- https://huggingface.co/mistral-community/Mistral-7B-v0.2

Dansk videre udviklet afart af mistral.
- https://huggingface.co/Mabeck/Heidrun-Mistral-7B-chat

Metas nyeste Llama model, med fornuftig performance på dansk. Bemærk den mindre åben end de fleste andre modeller her.
- https://huggingface.co/meta-llama/Meta-Llama-3-8B

## Model Benchmarks

Scandeval er et dansk benchmark projekt, der evaluerer modeller til brug på de Skandinaviske sprog, inklusiv Dansk.
- https://scandeval.com/danish-nlg/

LMSYS Chatbot Arena Leaderboard er en anden tilgang til benchmarks, der virker ved at brugere kan evaluere svarene fra to anonyme modeller og derudfra identificerer den bedste.
- https://chat.lmsys.org/?leaderboard


## Online demoer

https://playground.ai.cloudflare.com/?model=@hf/nexusflow/starling-lm-7b-beta
https://playground.ai.cloudflare.com/?model=@cf/meta/llama-3-8b-instruct
https://playground.ai.cloudflare.com/?model=@hf/mistralai/mistral-7b-instruct-v0.2

## Kode demoer

[Summarize demo](summarize/README.md)

## Generelle anvendelser:

LLM kan anvendes til et væld af NLP opgaver, tekst summarisering, kategorisering, oversættelse, evaluering af logik og meget andet.

LLM kan bruges til at konstruere chat flows. Udvalget af modeller der performer godt på dansk er dog begrænset.

## Ideer til anvendelse i Gyldendal Uddannelse

### Summarisering til søge visning i Internetbøger

Når man foretager en søgning på Gymnasie internetbøgerne idag, viser vi et udsnit at resultatet for de matchede resultater. Man kunne istedetfor tilbyde at vise en summarisering af resultatet.
