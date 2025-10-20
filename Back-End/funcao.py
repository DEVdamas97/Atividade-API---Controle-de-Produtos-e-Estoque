
from conexao import conectar

def criar_tabela():
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(

            """
            CREATE TABLE IF NOT EXISTS estoque (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(100) NULL,
            categoria VARCHAR(50),
            preco DECIMAL (10,2) NOT NULL,
            quantidade INT
            )
            """
            )
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao inserir {erro}")
        finally:
            cursor.close()
            conexao.close()
criar_tabela()