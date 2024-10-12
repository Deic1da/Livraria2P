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
        #print(f"\033[92mBD Conectado!\033[0m")
        return conn

    except Exception as e:
        print(f"Erro ao conectar com o banco de dados: {e}")
        return None
