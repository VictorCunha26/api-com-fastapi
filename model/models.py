from typing import Optional
from pydantic import BaseModel

class Serie(BaseModel):
    id_serie: str
    titulo: str
    descricao: str
    ano_lancamento: int
    id_categoria: int