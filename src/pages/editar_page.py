from pages import *
from services import *
import time
import os
from services.livros_services import *
from services.funcionarios_services import listar_funcionarios
from services.editar_services import editar
from services.categorias_services import *
from services.autores_services import *
from services.editoras_services import *
from services.pesquisar_elemento_one_services import pesquisar_elemento_one


def editar_page():
    try:
        while True:
            
            os.system("cls")
            print("\033[96mEditar\033[0m")
            print("\033[92m1 - Livro\033[0m")
            print("\033[92m2 - Autor\033[0m")
            print("\033[92m3 - Categoria\033[0m")
            print("\033[92m4 - Editora\033[0m")
            print("\033[92m5 - Funcionario\033[0m")
            print("\033[91m0 - Voltar\033[0m\n")

            escolha = int(input("Digite sua escolha: "))
            os.system("cls")

            if 0 <= escolha <= 5:
                if escolha == 0:
                    return
                elif escolha == 1:
                    listar_livros()
                    id = input("Selecione o livro que deseja editar(0 para cancelar):")
                    os.system("cls")
                    print("\033[96mO que deseja editar?\033[0m")
                    print("\033[92m1 - Nome\033[0m")
                    print("\033[92m2 - Categoria\033[0m")
                    print("\033[92m3 - Autor\033[0m")
                    print("\033[92m4 - Editora\033[0m")
                    print("\033[92m5 - Estoque\033[0m")
                    print("\033[92m6 - Preço\033[0m\n")
                    print("\033[91m0 - Voltar\033[0m\n")

                    escolha = int(input("Digite sua escolha: "))
                    os.system("cls")

                    if 0 <= escolha <= 6:
                        if escolha == 0:
                            return
                        
                        elif escolha == 1:
                            novo = input("Digite o novo nome do livro:")
                            editar(id,"id_livro","livros","nome_livro",novo)
                        
                        elif escolha == 2:
                            listar_categorias()
                            novo = int(input("Escolha a categoria (ou digite 0 para cadastrar uma nova): "))
                            if novo == 0:
                                os.system("cls")
                                categoria = input("Digite o nome da categoria: ")
                                cadastrar_categoria(categoria)
                                os.system("cls")
                                listar_categorias()
                                novo = int(input("Escolha uma categoria: "))
                            editar(id,"id_livro","livros","id_categoria",novo)

                        elif escolha == 3:
                            listar_autores()
                            novo = int(input("Escolha o autor (ou digite 0 para cadastrar um novo): "))
                            if novo == 0:
                                os.system("cls")
                                autor = input("Digite o nome do autor: ")
                                cadastrar_autor(autor)
                                os.system("cls")
                                listar_autores()
                                novo = int(input("Escolha um autor: "))  
                            editar(id,"id_livro","livros","id_autor",novo)

                        elif escolha == 4:
                            listar_editoras()
                            novo = int(input("Escolha a editora (ou digite 0 para cadastrar um novo): "))
                            if novo == 0:
                                os.system("cls")
                                nome = input("Digite o nome da editora: ")
                                os.system("cls")
                                endereco = input("Digite o endereço da editora: ")
                                cadastrar_editora(nome, endereco)
                                os.system("cls")
                                listar_editoras()
                                novo = int(input("Escolha uma editora: "))  
                            editar(id,"id_livro","livros","id_editora",novo)

                        elif escolha == 5:
                            
                            escolha = int(input("1 - Adicionar\n2 - alterar\nDigite sua escolha: "))
                            os.system("cls")
                            
                            if escolha == 1:
                                valor = pesquisar_elemento_one(id, "estoque", "livros", "id_livro")
                                print(f"Estoque atual = {valor}")
                                novo = int(input("Digite o valor a acrescentar: "))+valor
                                os.system("cls")
                                editar(id,"id_livro","livros","estoque",novo)
                                print(f"Estoque atualizado = {novo}")
                                time.sleep(2)

                            elif escolha == 2:
                                valor = pesquisar_elemento_one(id, "estoque", "livros", "id_livro")
                                print(f"Estoque atual = {valor}")
                                novo = int(input("Digite o novo valor: "))
                                os.system("cls")
                                editar(id,"id_livro","livros","estoque",novo)
                                print(f"Estoque atualizado = {novo}")
                                time.sleep(2)
                            else:
                                return
                        elif escolha == 6:
                            valor = pesquisar_elemento_one(id, "preco", "livros", "id_livro")
                            print(f"Preço atual = R${valor}")
                            novo = int(input("Digite o novo preço do livro:"))
                            os.system("cls")
                            editar(id,"id_livro","livros","preco",novo)
                            print(f"Preço atualizado = R${valor}")
                            time.sleep(2)

    except ValueError:
        print("\033[91mPor favor, digite um número válido.\033[0m")
        time.sleep(2)