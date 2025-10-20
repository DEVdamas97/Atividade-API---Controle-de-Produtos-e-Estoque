
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

#Listar
@app.get("/estoque")
def listar():
    listar = funcao.listar_produtos()
    lista = []
    for linha in listar:
        lista.append({
            "id": linha[0],
            "nome": linha[1],
            "categoria": linha[2],
            "preco": linha[3],
            "quantidade": linha[4]
        })
        
    return {
        "produtos": lista
    }


#Adicionar
@app.post("/estoque")
def adicionar_produto(nome: str, categoria: str, preco: float, quantidade: int):
    funcao.adicionar_produto(nome, categoria, preco, quantidade)
    return {"mensagem": "Produto adicionado com sucesso"}


#Deletar
@app.delete("/estoque/{id}")
def deletar_produto(id_produto:int):
    funcao.deletar_produto(id_produto)
    deletar = funcao.deletar_produto()
    if deletar:
        funcao.deletar(id_produto)
        return {"mensagem": "Produto deletado com sucesso"}
    

#Atualizar
@app.put("/estoque/{id_produto}")
def atualizar_produto(id_produto: int, novo_preco: float):
    funcao.atualizar_produto(id_produto, novo_preco)
    produto = funcao.buscar_produto()
    if produto:
        funcao.atualizar_produto(id_produto, novo_preco)
        return {"mensagem": "Produto atualizado com sucesso!"}
    return {"erro": "Produto não encontrado"}