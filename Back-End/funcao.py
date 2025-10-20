
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


def adicionar_produto(nome, categoria, preco, quantidade):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "INSERT INTO estoque (nome, categoria, preco, quantidade) VALUES (%s, %s, %s, %s)",
                (nome, categoria, preco, quantidade)
            )
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao inserir um produto: {erro}")
        finally:
            cursor.close()
            conexao.close()


def deletar_produto(id):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                'DELETE FROM estoque WHERE id = %s', (id,)
            )
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao deletar um produto: {erro}")
        finally:
            cursor.close()
            conexao.close()


def listar_produtos():
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
            """
            SELECT * FROM estoque ORDER BY id 
            """
            )
            return cursor.fetchall()
        except Exception as erro:
            print(f"Erro ao listar os produtos: {erro}")
            return [

            ]
        finally:
            cursor.close()
            conexao.close()