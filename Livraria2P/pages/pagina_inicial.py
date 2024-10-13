import os
from pages.procurar_livro_page import procurar_livro
from pages.gerenciar_page import gerenciar

def pagina_inicial(funcionario):
    while True:
        try:
            os.system("cls")
            print(funcionario)
            print("Livraria2P")
            print("1 - Procurar Livro")
            print("2 - Gerenciar Livraria2P")
            print("0 - Sair\n")
            
            escolha = int(input("Digite sua escolha: "))

            if 0 <= escolha <= 2:
                if escolha == 0:
                    return()
                elif escolha == 1:
                    procurar_livro(funcionario)
                elif escolha == 2:
                    gerenciar()
            else:
                print("\033[93mErro: Digite um número entre 0 e 2!\033[0m")
        except ValueError:
            print("\033[91mErro: Entrada inválida! Por favor, digite um número.\033[0m")
