from services import *
import time
import os
from services.database import criar_conexao
from services.verificador import *

def cadastrar_funcionario():
    conn = criar_conexao()
    if conn is None:
        print("\033[91mErro na conexão com o banco de dados.\033[0m")
        return
    
    try:
        while True:
            os.system("cls")
            print("Cadastrar Funcionario")
            nome = input("Digite o nome: ").strip()
            if validar_nome(nome):
                break
        
        while True:
            os.system("cls")
            print("Cadastrar Funcionario")
            email = input("Digite o email: ").strip()
            if validar_email(email):
                break
        
        os.system("cls")
        print("Cadastrar Funcionario")
        senha = input("Digite a senha: ")

        cursor = conn.cursor()
        query = "INSERT INTO funcionarios(nome, email, senha) VALUES(%s, %s, %s);"
        cursor.execute(query, (nome, email, senha))
        conn.commit()
        os.system("cls")
        print("\033[92mFuncionário inserido com sucesso!\033[0m")
        time.sleep(2)
    except Exception as e:
        print(f"\033[91mErro ao inserir funcionário: {e}\033[0m")
        time.sleep(2)
    finally:
        cursor.close()
        conn.close()
