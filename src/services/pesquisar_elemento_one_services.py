from services import *
import time
import os
from services.database import criar_conexao

def pesquisar_elemento_one(id, filtro, tabela, coluna):
    conn = criar_conexao()
    if conn is None:
        print("\033[91mErro na conexão com o banco de dados.\033[0m")
        return
    
    try:
        cursor = conn.cursor()
        query = f"SELECT {filtro} FROM {tabela} WHERE {coluna} = %s;"
        cursor.execute(query, (id,))
        resultado = cursor.fetchone()[0]
        
        if resultado:
            return resultado
        else:
            print("\033[93mNenhum resultado encontrado.\033[0m")
            time.sleep(1)
    except Exception as e:
        print(f"\033[91mErro ao listar: {e}\033[0m")
        time.sleep(2)
    finally:
        cursor.close()
        conn.close()