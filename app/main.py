
from fastapi import FastAPI
from pydantic import BaseModel
from data.database import Database
from model.models import Serie, Ator, Categoria, Motivo, Avaliacao

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

@app.post("/ator/")
def cadastrar_ator(ator: Ator):
    db.conectar()
    sql = "INSERT INTO ator (nome) VALUES (%s)"
    db.executar(sql, (ator.nome,))
    db.desconectar()
    return {"message": "Ator cadastrado com sucesso"}

@app.post("/categorias/")
def adicionar_categoria(categoria: Categoria):
    db.conectar()
    sql = "INSERT INTO categoria (nome) VALUES (%s)"
    db.executar(sql, (categoria.nome,))
    db.desconectar()
    return {"message": "Categoria adicionada com sucesso"}

@app.post("/atores/{id_ator}/series/{id_serie}")
def associar_ator_serie(id_ator: int, id_serie: int, personagem: str):
    db.conectar()
    sql = "INSERT INTO ator_serie (id_ator, id_serie, personagem) VALUES (%s, %s, %s)"
    db.executar(sql, (id_ator, id_serie, personagem))
    db.desconectar()
    return {"message": "Ator associado à série com sucesso"}

@app.post("/motivos/")
def incluir_motivo(motivo: Motivo):
    db.conectar()
    sql = "INSERT INTO motivo_assistir (id_serie, motivo) VALUES (%s, %s)"
    db.executar(sql, (motivo.id_serie, motivo.motivo))
    db.desconectar()
    return {"message": "Motivo incluído com sucesso"}

@app.post("/avaliacoes/")
def avaliar_serie(avaliacao: Avaliacao):
    db.conectar()
    sql = "INSERT INTO avaliacao_serie (id_serie, nota, comentario) VALUES (%s, %s, %s)"
    db.executar(sql, (avaliacao.id_serie, avaliacao.nota, avaliacao.comentario))
    db.desconectar()
    return {"message": "Avaliação registrada com sucesso"}

@app.get("/series/")
def listar_series():
    db.conectar()
    sql = "SELECT * FROM serie"
    serie = db.executar(sql)  
    db.desconectar()
    return serie

@app.get("/atores/")
def listar_autores():
    db.conectar()
    sql = "SELECT * FROM autor"
    autores = db.executar_comando(sql)
    db.desconectar()
    return autores

# Rotas para categorias
@app.get("/categorias/")
def listar_categorias():
    db.conectar()
    sql = "SELECT * FROM categoria"
    categorias = db.executar_comando(sql)
    db.desconectar()
    return categorias


@app.get("/avaliacoes/")
def listar_avaliacoes():
    db.conectar()
    sql = "SELECT * FROM avaliacao_serie"
    avaliacoes = db.executar_comando(sql)
    db.desconectar()
    return avaliacoes
    


