from services import *
import time
import os
from pages.deletar_page import deletar_page

def gerenciar_page():
    while True:
        try:
            os.system("cls")
            print("\033[94mGerenciar Livraria2P\033[0m")
            print("\033[92m1 - Cadastrar Livro\033[0m")
            print("\033[92m2 - Cadastrar Cliente\033[0m")
            print("\033[92m3 - Cadastrar Funcionario\033[0m")
            print("\033[92m4 - Deletar\033[0m")
            print("\033[91m0 - Voltar\033[0m\n")
            
            escolha = int(input("Digite sua escolha: "))
            os.system("cls")

            if 0 <= escolha <= 4:
                if escolha == 0:
                    return
                elif escolha == 1:
                    cadastrar_livro()
                elif escolha == 2:
                    cadastrar_cliente()
                elif escolha == 3:
                    cadastrar_funcionario()
                elif escolha == 4:
                    deletar_page()
            else:
                print("\033[93mErro: Digite um número entre 0 e 3!\033[0m")
        except ValueError:
            print("\033[91mErro: Entrada inválida! Por favor, digite um número.\033[0m")
