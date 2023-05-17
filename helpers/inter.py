from tensorflow import keras
from sklearn.metrics.pairwise import cosine_similarity
from helpers.model import model

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
  r_f = a[0]
  count=0
  for item in r_f:
    count = count+1
    if item >= 0.7:
      return frases[count]
  return ["Sin equivalencias semanticas"]