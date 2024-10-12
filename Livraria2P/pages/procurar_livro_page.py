import os

def procurar_livro():
    while True:
        try:
            os.system("cls")
            print("Procurar Livro")
            print("1 - Todos os Livros")
            print("2 - Por Autor")
            print("3 - Por Categoria")
            print("4 - Por Editora")
            print("0 - Sair\n")

            escolha = int(input("Digite sua escolha: "))

            if 0 <= escolha <= 4:
                return escolha
            else:
                print("\033[93mErro: Digite um número entre 0 e 4!\033[0m")
        except ValueError:
            print("\033[91mErro: Entrada inválida! Por favor, digite um número.\033[0m")
