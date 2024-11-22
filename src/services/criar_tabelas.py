from services import *
import time
import os
from services.database import criar_conexao

def criar_tabelas():
    conn = criar_conexao()
    if conn is None:
        print("\033[91mErro na conexão com o banco de dados.\033[0m")
        return
    try:
        cursor = conn.cursor()
        query = """CREATE TABLE IF NOT EXISTS autores (
                    id_autor SERIAL PRIMARY KEY,
                    nome_autor VARCHAR(500) NOT NULL UNIQUE
                    );

                    CREATE TABLE IF NOT EXISTS editoras (
                    id_editora SERIAL PRIMARY KEY,
                    nome_editora VARCHAR(1000) NOT NULL UNIQUE,
                    endereco VARCHAR(2000) NOT NULL
                    );

                    CREATE TABLE IF NOT EXISTS categorias (
                    id_categoria SERIAL PRIMARY KEY,
                    nome_categoria VARCHAR(200) NOT NULL UNIQUE
                    );

                  CREATE TABLE IF NOT EXISTS clientes (
                    id_cliente SERIAL PRIMARY KEY,
                    nome VARCHAR(500) NOT NULL,
                    email VARCHAR(1000) NOT NULL UNIQUE,
                    endereco VARCHAR(2000) NOT NULL,
                    cpf CHAR(11) NOT NULL UNIQUE
                   );

                    CREATE TABLE IF NOT EXISTS funcionarios (
                    id_funcionario SERIAL PRIMARY KEY,
                    nome VARCHAR(500) NOT NULL,
                    email VARCHAR(1000) NOT NULL UNIQUE,
                    senha bytea NOT NULL
                   );

                    CREATE TABLE IF NOT EXISTS livros (
                    id_livro SERIAL PRIMARY KEY,
                    nome_livro VARCHAR(1000) NOT NULL,
                    id_categoria INT REFERENCES categorias(id_categoria),
                    id_autor INT REFERENCES autores(id_autor),
                    id_editora INT REFERENCES editoras(id_editora),
                    estoque INT NOT NULL,
                    preco NUMERIC(10, 2) NOT NULL
                    );

                    CREATE TABLE IF NOT EXISTS pedidos (
                    id_pedido SERIAL PRIMARY KEY,
                    id_cliente INT REFERENCES clientes(id_cliente),
                    id_livro INT REFERENCES livros(id_livro),
                    quantidade INT NOT NULL,
                    preco_pedido NUMERIC(10, 2) NOT NULL,
                    id_funcionario INT REFERENCES funcionarios(id_funcionario),
                    data_pedido DATE NULL
                    );
                    """
        cursor.execute(query)
        conn.commit()
        print("\033[92mCriando tabelas...!\033[0m")
        
    except Exception as e:
        print(f"\033[91mErro ao criar tabelas: {e}\033[0m")
    finally:
        cursor.close()
        conn.close()