from services import *
import time
import os
from services.database import criar_conexao
from services.verificador import *

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
        query = "SELECT * FROM clientes ORDER BY id_cliente ASC;"
        cursor.execute(query)
        clientes = cursor.fetchall()
        
        if clientes:
            print("\033[96mClientes cadastrados:\033[0m")
            print("\033[94mID\033[0m" + " " * 4 + "\033[94mNome\033[0m" + " " * 22 + "\033[94mCPF\033[0m")
            print("-" * 60)
            for cliente in clientes:
                # Formatação com espaçamento
                print(f"\033[92m{cliente[0]:<5}\033[0m" + f" {cliente[1]:<25} {cliente[4]}")
        else:
            print("\033[93mNenhum cliente encontrado.\033[0m")
    except Exception as e:
        print(f"\033[91mErro ao listar clientes: {e}\033[0m")
    finally:
        cursor.close()
        conn.close()


def procurar_clientes(comparador,dado):
    conn = criar_conexao()
    if conn is None:
        print("\033[91mErro na conexão com o banco de dados.\033[0m")
        return
    
    try:
        cursor = conn.cursor()
        query = f"SELECT * FROM clientes c where c.{comparador} like %s;"
        cursor.execute(query, (dado,))
        clientes = cursor.fetchone()
        
        if clientes:
            print("\033[96mClientes cadastrados:\033[0m")
            print("\033[94mID\033[0m" + " " * 4 + "\033[94mNome\033[0m" + " " * 22 + "\033[94mCPF\033[0m")
            print("-" * 60)
            print(f"\033[92m{clientes[0]:<5}\033[0m" + f" {clientes[1]:<25} {clientes[4]}")
        else:
            print("\033[93mNenhum cliente encontrado.\033[0m")
    except Exception as e:
        print(f"\033[91mErro ao listar clientes: {e}\033[0m")
    finally:
        cursor.close()
        conn.close()