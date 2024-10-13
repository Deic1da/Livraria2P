import os
from services.pedidos_services import vender_livro
from services.livros_services import listar_autores,listar_categorias,listar_editoras, listar_livros, listar_livros_personalisado

def procurar_livro(funcionario):
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
                if escolha == 0:
                    return
                
                elif escolha == 1:
                    listar_livros()
                    
                    produto = int(input("Escolha o livro: "))
                    os.system("cls")       

                    vender_livro(produto,funcionario)

                elif escolha == 2:
                    pesquisa = "id_Autor"
                    
                    os.system("cls")
                    listar_autores()
                    autor = input("Escolha o autor: ")
                    listar_livros_personalisado(autor,pesquisa)
                    
                    
                    produto = int(input("Escolha o livro: "))
                    os.system("cls")

                    vender_livro(produto,funcionario)

                elif escolha == 3:
                    pesquisa = "id_Categoria"
                    
                    os.system("cls")
                    listar_categorias()
                    categoria = input("Escolha o autor: ")
                    listar_livros_personalisado(categoria,pesquisa)
                    
                    
                    produto = int(input("Escolha o livro: "))
                    os.system("cls")

                    vender_livro(produto,funcionario)

                elif escolha == 4:
                    pesquisa = "id_Editora"

                    os.system("cls")
                    listar_editoras()
                    editora = input("Escolha o autor: ")
                    listar_livros_personalisado(editora,pesquisa)
                    
                    
                    produto = int(input("Escolha o livro: "))
                    os.system("cls")

                    vender_livro(produto,funcionario)

            else:
                print("\033[93mErro: Digite um número entre 0 e 4!\033[0m")
        except ValueError:
            print("\033[91mErro: Entrada inválida! Por favor, digite um número.\033[0m")
