from services import *
from pages import *
from pages.inicial_page import inicial_page
from services.criar_tabelas import criar_tabelas
from services.verificador import verificar_funcionario
import time
import os

criar_tabelas()

try:
    if verificar_funcionario():
        while True:
            funcionario = login_page()
            if funcionario is not None:
                break
    else:
        cadastrar_funcionario()
        while True:
            funcionario = login_page()
            if funcionario is not None:
                break
    
    inicial_page(funcionario)

except Exception as e:
    print(f"\n\033[91mErro inesperado: {e}\033[0m")
    time.sleep(2)
    inicial_page()
finally:
    os.system("cls")
    print("\033[93mDesligando[10%]... Preparando para desligar\033[0m")
    time.sleep(0.5)
    print("\033[93mDesligando[30%]... Salvando progresso\033[0m")
    time.sleep(0.8)
    print("\033[93mDesligando[50%]... Finalizando processos\033[0m")
    time.sleep(1)
    print("\033[93mDesligando[80%]... Limpando memória\033[0m")
    time.sleep(1.2)
    print("\033[93mDesligando[100%]... Sistema desligado com sucesso!\033[0m")
    time.sleep(2)