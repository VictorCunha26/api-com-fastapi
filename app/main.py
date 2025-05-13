
from fastapi import FastAPI
from pydantic import BaseModel
from data.database import Database
from model.models import Serie

db = Database()
app = FastAPI()

series_db = [] #Lista que simula um banco de dados

@app.post('/serie/')
def cadastrar(serie: Serie):
    db.conectar()
    sql = "INSERT INTO serie (titulo, descricao, ano_lancamento, id_categoria) VALUES (%s, %s,%s,%s)"
    db.executar(sql,(serie.titulo, serie.descricao,serie.ano_lancamento, serie.id_categoria))
    db.desconectar()
    return {"mensagem": "Série cadastrada com sucesso", "serie": serie}

@app.get("/series/")
def listar_series():
    db.conectar()
    sql = "SELECT * FROM serie"
    serie = db.executar(sql)  
    db.desconectar()
    return serie
    


