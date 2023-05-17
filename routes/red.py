from fastapi import APIRouter
from helpers.model import model
from helpers.inter import Interprete
from models.red import Red
from notigram import ping

TOKEN='daa39d53-6283-47a1-b945-b7ee6528dde0'
red = APIRouter()

sentences = [
      "El perro juega en el parque .",
      "Mi pastel se quemó",
      "El niño no hizo el examen ",
      "En el parque hay un perro jugando"
  ]

@red.post('/test', tags=["Cod"])
def postText(red: Red):
    ping(TOKEN, 'Iniciando análisis de Texto')
    mod = model.encode(sentences)
    a = red.parrafo.texto1
    b = red.parrafo.texto2[:]
    ping(TOKEN, 'Análisis de Texto lista')
    return Interprete(a,b)

"""
Las sentencias se deben mandar a traer directo de la DB en pymongo
"""