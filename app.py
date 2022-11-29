from fastapi import FastAPI
from routes.red import red
from docs.docs import tags_metadata
from os import environ as env
from notigram import ping

ping('daa39d53-6283-47a1-b945-b7ee6528dde0', 'Servidor de código corriendo')
app = FastAPI(
    title= "Someone title :v/ vrgs",
    description= "Someone description :v/ prrna",
    version= "1.1.0",
    openapi_tags= tags_metadata
)

app.include_router(red)