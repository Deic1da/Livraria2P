from services import *
from pages import *
from services.livros_services import procurar_por_nome
import time
import os

def procurar_livro_page(funcionario):
    while True:
        try:
            os.system("cls")
            print("\033[96mProcurar Livro\033[0m")
            print("\033[92m1 - Todos os Livros\033[0m")
            print("\033[92m2 - Por Autor\033[0m")
            print("\033[92m3 - Por Categoria\033[0m")
            print("\033[92m4 - Por Editora\033[0m")
            print("\033[92m5 - Pesquisa por Nome do Livro\033[0m")
            print("\033[91m0 - Voltar\033[0m\n")

            escolha = int(input("Digite sua escolha: "))
            os.system("cls")

            if 0 <= escolha <= 5:
                if escolha == 0:
                    print("\033[92mSaindo do programa...\033[0m")
                    return
                
                elif escolha == 1:
                    listar_livros()
                    produto = int(input("Escolha o livro: "))
                    os.system("cls")
                    vender_livro(produto, funcionario)

                elif escolha == 2:
                    pesquisa = "id_Autor"
                    os.system("cls")
                    listar_autores()
                    autor = input("Escolha o autor: ")
                    listar_livros_personalisado(autor, pesquisa)
                    produto = int(input("Escolha o livro: "))
                    os.system("cls")
                    vender_livro(produto, funcionario)

                elif escolha == 3:
                    pesquisa = "id_Categoria"
                    os.system("cls")
                    listar_categorias()
                    categoria = input("Escolha a categoria: ")
                    listar_livros_personalisado(categoria, pesquisa)
                    produto = int(input("Escolha o livro: "))
                    os.system("cls")
                    vender_livro(produto, funcionario)

                elif escolha == 4:
                    pesquisa = "id_Editora"
                    os.system("cls")
                    listar_editoras()
                    editora = input("Escolha a editora: ")
                    listar_livros_personalisado(editora, pesquisa)
                    produto = int(input("Escolha o livro: "))
                    os.system("cls")
                    vender_livro(produto, funcionario)

                elif escolha == 5:
                    os.system("cls")
                    pesquisa = input("Digite o nome do livro: ")
                    procurar_por_nome(pesquisa)
                    produto = int(input("Escolha o livro: "))
                    os.system("cls")
                    vender_livro(produto, funcionario)

            else:
                print("\033[91mErro: Digite um número entre 0 e 4!\033[0m")
                time.sleep(2)
        except ValueError:
            print("\033[91mErro: Entrada inválida! Por favor, digite um número.\033[0m")
            time.sleep(2)
