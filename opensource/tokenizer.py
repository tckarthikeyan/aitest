from transformers import BertModel, AutoTokenizer
import pandas as pd

model_name="bert-base-cased"

model = BertModel.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

sentence =  "When life gives you lemons, don't make lemanade"

tokens = tokenizer.tokenize(sentence)
print(tokens)

def predict(text) :
    encoded_inputs = tokenizer(text, return_tensors='pt')
    return model(**encoded_inputs)[0]

another_sentence1 = "There was a fly drinking from my coffee"
another_sentence2 = "To become a commercial piolt, he need to fly 1500 hours"

token1 = tokenizer.tokenize(another_sentence1)
token2 = tokenizer.tokenize(another_sentence2)

out1 = predict(another_sentence1)
out2 = predict(another_sentence2)
