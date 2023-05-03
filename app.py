from fastapi import FastAPI
from routes.red import red
from docs.docs import tags_metadata
from os import environ as env
from notigram import ping

ping(env['TOKEN'], 'Aquí APIPara Sstemas encendidos!')
app = FastAPI(
    title= "Someone title :v/ vrgs",
    description= "Someone description :v/ prrna",
    version= "1.1.0",
    openapi_tags= tags_metadata
)

app.include_router(red)