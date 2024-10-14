from pages.procurar_livro_page import procurar_livro_page
from pages.gerenciar_page import gerenciar_page
import os
import time
from services import *

def inicial_page(funcionario):
    while True:
        try:
            os.system("cls")
            print(f"\033[94mFuncionário ID: {funcionario}\033[0m")
            print("\033[96mLivraria2P\033[0m")
            print("\033[92m1 - Procurar Livro\033[0m")
            print("\033[92m2 - Gerenciar Livraria2P\033[0m")
            print("\033[92m3 - Historico de vendas\033[0m")
            print("\033[91m0 - Sair\033[0m\n")
            
            escolha = int(input("Digite sua escolha: "))
            os.system("cls")

            if 0 <= escolha <= 3:
                if escolha == 0:
                    return
                elif escolha == 1:
                    procurar_livro_page(funcionario)
                elif escolha == 2:
                    gerenciar_page()
                elif escolha == 3:
                    listar_pedidos()
            else:
                print("\033[91mErro: Digite um número entre 0 e 2!\033[0m")
                time.sleep(1)
        except ValueError:
            print("\033[91mErro: Entrada inválida! Por favor, digite um número.\033[0m")
            time.sleep(1)
