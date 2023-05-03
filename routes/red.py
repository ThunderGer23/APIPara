from fastapi import APIRouter
from helpers.model import model
from helpers.inter import Interprete
from models.red import Red
from os import environ as env
from notigram import ping
from tensorflow import keras

red = APIRouter()

sentences = [
      "El perro juega en el parque .",
      "Mi pastel se quemó",
      "El niño no hizo el examen ",
      "En el parque hay un perro jugando"
  ]

@red.post('/test', response_model= str, tags=["Cod"])
def postText(red: Red):
    ping(env['TOKEN'], 'Iniciando analisis de texto')
    mod = model.encode(sentences)
    a = red.parrafo.texto1
    b = red.parrafo.texto2[:]
    ping(env['TOKEN'], 'Interpretación lista')
    return Interprete(a,b)

"""
Las sentencias se deben mandar a traer directo de la DB en pymongo
"""