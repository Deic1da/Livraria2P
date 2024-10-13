from services import *
import time
import os


def deletar_page():
    while True:
        
        os.system("cls")
        print("\033[96mDeletar\033[0m")
        print("\033[92m1 - Livro\033[0m")
        print("\033[92m2 - Autor\033[0m")
        print("\033[92m3 - Categoria\033[0m")
        print("\033[92m4 - Editora\033[0m")
        print("\033[92m5 - Funcionario\033[0m")
        print("\033[91m0 - Voltar\033[0m\n")

        escolha = int(input("Digite sua escolha: "))

        if 0 <= escolha <= 5:
            if escolha == 0:
                return
            #elif escolha == 1:
                #   ()
            #elif escolha == 2:
                #   ()
            #elif escolha == 3:
                #   ()
            #elif escolha == 4:
                #   ()
            #elif escolha == 5:
                #   ()