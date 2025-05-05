from datetime import date
from typing import Union 
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

series_db = [] #Lista que simula um banco de dados

class Serie(BaseModel):
    id: int
    titulo: str
    descricao: str

@app.post('/series/')
def cadastrar(serie: Serie):
    series_db.append(serie)
    return {"mensagem": "Série cadastrada com sucesso", "serie": serie}

