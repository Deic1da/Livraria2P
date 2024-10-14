import time
import os
from services.database import criar_conexao

def editar(id,id_nome,tabela,coluna,novo):
    conn = criar_conexao()
    if conn is None:
        print("\033[91mErro na conexão com o banco de dados.\033[0m")
        return
    
    try:
        cursor = conn.cursor()
        query = f"UPDATE {tabela} SET {coluna} = %s WHERE {id_nome} = %s;"
        cursor.execute(query, (novo,id,))
        conn.commit()
        os.system("cls")
        print("\033[92mDados editados com sucesso!\033[0m")
        time.sleep(2)
    except Exception as e:
        print(f"\033[91mErro ao editar dados: {e}\033[0m")
        time.sleep(5)
    finally:
        cursor.close()
        conn.close()