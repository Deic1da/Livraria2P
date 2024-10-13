import psycopg2

def criar_conexao():
    try:
        conn = psycopg2.connect(
            dbname='postgres',
            user='postgres',
            password='post',
            host='localhost',
            port='5432'
        )
        print("\033[92mBD Conectado com sucesso!\033[0m")
        return conn

    except Exception as e:
        print(f"\033[91mErro ao conectar com o banco de dados: {e}\033[0m")
        return None
