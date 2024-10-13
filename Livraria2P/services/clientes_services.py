from services.database import criar_conexao
from services.verificador import validar_cpf, validar_email, validar_nome
import os
import time

def cadastrar_cliente():
    conn = criar_conexao()
    if conn is None:
        print("\033[91mErro na conexão com o banco de dados.\033[0m")
        return
    
    try:
        while True:
            os.system("cls")
            nome = input("Digite o nome: ").strip()
            if validar_nome(nome):
                break
        
        while True:
            os.system("cls")
            email = input("Digite o email: ").strip()
            if validar_email(email):
                break

        os.system("cls")
        endereco = input("Digite o endereço: ").strip()
        
        while True:
            os.system("cls")
            cpf = input("Digite o CPF (somente números, 11 dígitos): ").strip()
            if validar_cpf(cpf):
                break

        os.system("cls")
        cursor = conn.cursor()
        query = "INSERT INTO clientes(nome, email, endereco, cpf) VALUES(%s, %s, %s, %s);"
        cursor.execute(query, (nome, email, endereco, cpf))
        conn.commit()
        print("\033[92mCliente inserido com sucesso!\033[0m")
        time.sleep(2)
    except Exception as e:
        print(f"\033[91mErro ao inserir cliente: {e}\033[0m")
        time.sleep(2)
    finally:
        cursor.close()
        conn.close()

def listar_clientes():
    conn = criar_conexao()
    if conn is None:
        print("\033[91mErro na conexão com o banco de dados.\033[0m")
        return
    
    try:
        cursor = conn.cursor()
        query = "SELECT * FROM clientes;"
        cursor.execute(query)
        clientes = cursor.fetchall()
        
        if clientes:
            print("Clientes cadastrados:")
            for cliente in clientes:
                print(f"{cliente[0]} = {cliente[1]} | {cliente[4]}")
        else:
            print("\033[93mNenhum cliente encontrado.\033[0m")
    except Exception as e:
        print(f"\033[91mErro ao listar clientes: {e}\033[0m")
    finally:
        cursor.close()
        conn.close()
