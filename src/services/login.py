from services import *
import time
import os
from services.database import criar_conexao
from services.Criptografia_services import checar_password
import pwinput

def tentativa_login():
    conn = criar_conexao()
    if conn is None:
        print("\033[91mErro na conexão com o banco de dados!\033[0m")
        return None
    
    try:
        email = input("Digite o email: ")

        cursor = conn.cursor()
        query = "SELECT id_funcionario, senha FROM funcionarios WHERE email = %s;"
        cursor.execute(query, (email,))
        funcionario = cursor.fetchone()
        
        if funcionario is None:
            print("\033[91mEmail não encontrado!\033[0m")
            time.sleep(1)
            return None

        senha = pwinput.pwinput("Digite a senha: ")
        
        senha_armazenada = funcionario[1]
        id_funcionario = funcionario[0]

        if checar_password(senha, senha_armazenada):
            print("\033[92mLogin realizado com sucesso!\033[0m")
            time.sleep(1)
            return str(id_funcionario)
        else:
            print("\033[91mSenha incorreta!\033[0m")
            time.sleep(1)
            return None
    
    except Exception as e:
        print(f"\033[91mErro ao tentar logar: {e}\033[0m")  
        time.sleep(1)
        return None
    
    finally:
        cursor.close()
        conn.close()
