import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Gerenciador de Estoques", page_icon="🗄")

st.header("**Gerenciador de Estoque 📦**")

st.subheader("Bem-vindo ao sistema de gerenciamento de Estoque!")

menu = st.sidebar.radio("Opções", ["Listar Produtos", "Adicionar Produto"])

if menu == "Listar Produtos":
    st.subheader("Todos Produtos do estoque")
    response = requests.get(f"{API_URL}/estoque")
    
    if response.status_code == 200:
        produtos = response.json().get("produtos", [])  
        
        if produtos:
            st.dataframe(produtos)
        else:
            st.info("Nenhum produto cadastrado")
    else:
        st.error("Erro ao conectar com a API")

elif menu == "Adicionar Produto":
    st.subheader("➕ Adicionar produto")

    nome = st.text_input("Digite o **Nome do Produto**: ")
    categoria = st.text_input("Digite a **Categoria do Produto**: ")
    preco = st.number_input("Digite o **Preço do Produto**: ", step=0.01)
    avaliacao = st.number_input("Digite a avaliação (1 a 10)", min_value=1, max_value=10, step=1)

    if st.button("Salvar Produto 📂"):
        params = {
            "nome": nome,
            "categoria": categoria,
            "preco": preco,
            "avaliacao": avaliacao
        }

        response = requests.post(f"{API_URL}/estoque", json=params)
        if response.status_code == 200:
            st.success("Produto Adicionado com Sucesso!")
        else:
            st.error("Erro ao Adicionar o Produto")