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


