from services import *
from datetime import datetime
import time
import os
from services.database import criar_conexao
import re

def validar_email(email):
    padrão = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}(?:\.[a-zA-Z]{2,})?$"
    
    if not re.match(padrão, email):
        print("\033[91mErro: email inválido.\033[0m")
        return False
    else:
        return True
    

def validar_nome(nome):
    if re.search(r'\d', nome):
        print("\033[91mErro: O nome não deve conter números.\033[0m")
        return False
    return True


def validar_cpf(cpf):
    if not re.match(r'^\d{11}$', cpf):
        print("\033[91mErro: O CPF deve conter exatamente 11 dígitos numéricos.\033[0m")
        return False
    return True

def verificar_funcionario():
    conn = criar_conexao()
    if conn is None:
        print("\033[91mErro na conexão com o banco de dados.\033[0m")
        return
    try:
        cursor = conn.cursor()
        query = f"SELECT * FROM funcionarios"
        cursor.execute(query)
        funcionario = cursor.fetchall()
            
        if funcionario:
            return True
        else:
            return False
    except Exception as e:
        print(f"\033[91mErro ao listar funcionarios: {e}\033[0m")
    finally:
        cursor.close()
        conn.close()