from tensorflow import keras
from sklearn.metrics.pairwise import cosine_similarity
from helpers.model import model
from numpy import argmax

def Interprete (data_base, data_com ):
  frases=[]
  frases.append(data_base)
  for item in data_com :
    frases.append(item)
  frases_embeddings = model.encode(frases)
  a=cosine_similarity(
    [frases_embeddings[0]],
    frases_embeddings[1:]
    )  
  return f"{frases[argmax(a)+1]}" if max(a[0]) >= 0.9 else "Sin equivalencia"
  