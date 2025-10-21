# 📦 Sistema de Gerenciamento de Estoque (Fullstack Python)

Este é um sistema completo para gerenciamento de estoque, composto por uma interface gráfica intuitiva construída com **Streamlit** e um backend robusto baseado em **FastAPI** e **PostgreSQL**.

A aplicação permite a listagem, adição, atualização de preço e remoção de produtos do estoque.

## 🛠️ Tecnologias Utilizadas

* **Python:** Linguagem principal do projeto.
* **Streamlit:** Utilizado para criar a interface gráfica (frontend) (`app.py`).
* **FastAPI:** Framework para criação da API que serve como intermediário entre o frontend e o banco de dados (`api.py`).
* **PostgreSQL:** Sistema de Gerenciamento de Banco de Dados (SGBD) para armazenamento dos produtos.
* **psycopg2:** Driver Python para conexão com o PostgreSQL.
* **python-dotenv:** Para gerenciar variáveis de ambiente e a conexão segura com o DB.

## 🚀 Como Rodar o Projeto

Para colocar o projeto no ar, você precisará de dois processos rodando: o servidor da API (FastAPI) e a interface gráfica (Streamlit).

### 1. Pré-requisitos

* **Python 3.x** instalado.
* Um servidor **PostgreSQL** rodando (localmente ou em nuvem).

### 2. Configuração do Ambiente

#### 2.1. Variáveis de Ambiente (`.env`)

Crie um arquivo na raiz do projeto chamado `.env` e configure os dados de acesso ao seu banco de dados PostgreSQL:

DB_NAME=seu_bancoDB_USER=seu_usuarioDB_PASSWORD=sua_senhaDB_HOST=localhostDB_PORT=5432
#### 2.2. Instalação de Dependências

Instale todas as bibliotecas Python necessárias. Você precisará de `streamlit`, `requests`, `psycopg2-binary`, `python-dotenv`, `fastapi` e o pacote `uvicorn[standard]` (para rodar a API).

```bash
pip install streamlit requests psycopg2-binary python-dotenv fastapi uvicorn[standard]
# Se você tiver um arquivo requirements.txt, use:
# pip install -r requirements.txt
3. ExecuçãoPasso A: Iniciar o Servidor da API (Backend)Na pasta do projeto, inicie a API:Bashpython -m uvicorn api:app --reload
Passo B: Iniciar a Interface Gráfica (Frontend)Abra um novo terminal e, na pasta do projeto, inicie o Streamlit:Bashstreamlit run app.py
O sistema será aberto automaticamente no seu navegador.⚙️ FuncionalidadesA interface Streamlit oferece as seguintes opções através do menu lateral:Listar Produtos: Exibe todos os itens cadastrados na tabela estoque do PostgreSQL.Adicionar Produto: Formulário para inserção de um novo produto (nome, categoria, preço e quantidade).Atualizar Preço do Produto: Permite alterar o preço de um produto existente usando seu ID.Deletar Produto: Remove um produto do banco de dados utilizando seu ID.💾 Estrutura do Banco de DadosA tabela estoque é criada automaticamente pelo script funcao.py e possui a seguinte estrutura:ColunaTipoDescriçãoidSERIAL (PK)Chave primária, auto-incrementável.nomeVARCHAR(100)Nome do produto.categoriaVARCHAR(50)Categoria do produto.precoDECIMAL(10,2)Preço do produto.quantidadeINTQuantidade em estoque.