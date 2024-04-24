# Embedding demo

## Systemkrav

Se [Opsæt Python](../prepare-environment.md)

## semantic_search.py

Eksemplet implementerer en fuld demonstration af "semantic search" vha. embeddings.

Eksemplet anvender "documents.txt" filen, der også findes i repositoriet.

I eksemplet loades modellen (downloades hvis nødvendigt), hvorefter der genereres embeddings for alle linjer i documents.txt.
Derefter laves der en søgning på den første parameter skriptet har fået.

```
python semantic_search.py "Hvad er PtX?"
```

## Køretid

Skriptet kan tage lidt tid om at ekserkvere. Bemærk at det meste af tyden typisk bruges på at forberede modellen.
Selve genereringen af embeddings er relativt hurtig og sammenligningen af embeddings er hurtig.

## Leg med modellen

Udskift/supler gerne indholdet i documents.txt med eget indhold. En linje per "dokument".

Den anvendte model er en såkaldt "instruct" model dvs. den anvender en instruktion der kan bruges til at ændre fokus på outputtet.
Demo'en bruger som udgangspunkt "Given a web search query, retrieve relevant passages that answer the query", prøv at udskifte den med en anden instruktion,
det kunne f.eks. være "Given a question, retrieve questions that are semantically equivalent to the given question".
