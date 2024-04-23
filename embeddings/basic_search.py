#!/usr/bin/env python3

import torch.nn.functional as F
import argparse
from pprint import pprint

from torch import Tensor
from transformers import AutoTokenizer, AutoModel

parser = argparse.ArgumentParser(description='Search the documents.txt file using vector search.')
parser.add_argument('search_query', help='Search Query')
parser.add_argument('--apple_hardware', help='Execute model on Apple Neural Chip', action="store_true", required=False)
args = vars(parser.parse_args())

device = "cpu"

if args['apple_hardware']:
  device = "mps"

def average_pool(last_hidden_states: Tensor,
                 attention_mask: Tensor) -> Tensor:
    last_hidden = last_hidden_states.masked_fill(~attention_mask[..., None].bool(), 0.0)
    return last_hidden.sum(dim=1) / attention_mask.sum(dim=1)[..., None]

def get_detailed_instruct(task_description: str, query: str) -> str:
    return f'Instruct: {task_description}\nQuery: {query}'


# Each query must come with a one-sentence instruction that describes the task
task = 'Given a web search query, retrieve relevant passages that answer the query'
queries = [
    get_detailed_instruct(task, args['search_query']),
]

documents = []
documentFile = open('documents.txt', 'r')
lines = documentFile.readlines()

for line in lines:
  documents.append(line.strip())

input_texts = queries + documents

# The start of the AI model part #

tokenizer = AutoTokenizer.from_pretrained('intfloat/multilingual-e5-large-instruct')
model = AutoModel.from_pretrained('intfloat/multilingual-e5-large-instruct', device_map=device)

# Tokenize the input texts
batch_dict = tokenizer(input_texts, max_length=512, padding=True, truncation=True, return_tensors='pt').to(device)

outputs = model(**batch_dict)
embeddings = average_pool(outputs.last_hidden_state, batch_dict['attention_mask'])

# End of the AI model part #

# normalize embeddings
embeddings = F.normalize(embeddings, p=2, dim=1)
scores = (embeddings[:1] @ embeddings[1:].T) * 100
score_list = scores.tolist()[0]

highest_scoring_element = 0
highest_scoring_element_id = None

for idx, score in enumerate(score_list):
  if score > highest_scoring_element:
    highest_scoring_element = score
    highest_scoring_element_id = idx

print(f"Best match {highest_scoring_element}: \"{documents[highest_scoring_element_id]}\"")
