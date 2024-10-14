from services import *
from services.criar_tabelas import criar_tabelas
from services.verificador import verificar_funcionario

criar_tabelas()

try:
    """if verificar_funcionario():
        while True:
            funcionario = login_page()
            if funcionario is not None:
                break
    else:
        cadastrar_funcionario()
        while True:
            funcionario = login_page()
            if funcionario is not None:
                break"""
    funcionario = 1
    inicial_page(funcionario)

except Exception as e:
    print(f"\033[91mErro inesperado: {e}\033[0m")
finally:
    print("Desligando...")
