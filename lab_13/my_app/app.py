from textblob import TextBlob
from typing import List

def hello(name):
    output = f'Hello {name}'
    return output

def extract_sentiment(text):
    text = TextBlob(text)
    return text.sentiment.polarity

def text_contain_word(word: str, text: str):
    return word in text

def bubble_sort(lista:List):
    for j in range(len(lista)):
        for i in range(len(lista)-j-1):
            if lista[i] > lista[i+1]:
                lista[i],lista[i+1] = lista[i+1],lista[i]
    return lista
