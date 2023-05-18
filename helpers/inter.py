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
  max_value = max(a[0])
  max_index = a[0].index(max_value)

  return f"El valor máximo es {max_value} en la posición {max_index}" if max_value >= 0.7 else "Sin equivalencia"
  