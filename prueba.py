import tensorflow_hub as hub
import tensorflow_text as text
from tensorflow import keras
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

def Interprete (data_base, data_com ):
  frases=[]
  frases.append(data_base)
  for u in data_com :
    frases.append(u)
  print("frases a comparar:")
  print(frases[1:])
  print("\n")
  frases_embeddings = keras.model.encode(frases)
  a=cosine_similarity(
    [frases_embeddings[0]],
    frases_embeddings[1:]
    )
  print("con la siguiente oracion:\n")
  print(data_base)
  print("\n\n oracion con mas equivalencia semantica (parafraseo): \n")
  #print(len(a))
  #print(type(a))
  #print(a)
  r_f = a[0]
  #print(r_f)
  #print(r_f)
  count=0
  for q in r_f:
    count = count+1
    if q >= 0.9:
      print(frases[count])

def main ():
  sentences = [
      "El perro juega en el parque .",
      "Mi pastel se quemó",
      "El niño no hizo el examen ",
      "En el parque hay un perro jugando"
  ]

  a = sentences[0]
  b = sentences[1:]
  model = SentenceTransformer('bert-base-nli-mean-tokens')
  sentence_embeddings = keras.model.encode(sentences)
  Interprete(a,b)
