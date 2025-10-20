
from fastapi import FastAPI

import funcao

app = FastAPI(title="Controle de Produtos e Estoque")

# GET > Pegar/Listar
# POST > Enviar/Cadastrar
# PUT > Atualizar
# Delete > Deletar

# API sempre retorna dados em JSON (chave:valor)
@app.get("/")
def home():
    return {
        "mensagem": "Bem-Vindo nosso programa de Controle de Produtos e Estoque!"
    }