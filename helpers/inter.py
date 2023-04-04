from tensorflow import keras
from sklearn.metrics.pairwise import cosine_similarity
from helpers.model import model

def Interprete (data_base, data_com ):
  frases= [data_base] + data_com
  frases_embeddings = model.encode(frases)
  a= cosine_similarity( [frases_embeddings[0]], frases_embeddings[1:])[0]
  for i in range(0, len(a)):
    if a[i] >= 0.9 : return frases[i+1]
  return "Sin equivalencias semanticas"