from pages import *
from services import *
import time
import os
from services.livros_services import *
from services.editar_services import editar
from services.categorias_services import *
from services.autores_services import *
from services.editoras_services import *
from pages.editar_livro_page import editar_livro
from pages.editar_cliente_page import editar_cliente

def editar_page():
    try:
        while True:
            os.system("cls")
            print("\033[96mEditar\033[0m")
            print("\033[92m1 - Livro\033[0m")
            print("\033[92m2 - Autor\033[0m")
            print("\033[92m3 - Categoria\033[0m")
            print("\033[92m4 - Editora\033[0m")
            print("\033[92m5 - Cliente\033[0m")
            print("\033[91m0 - Voltar\033[0m\n")

            escolha = int(input("\033[94mDigite sua escolha: \033[0m"))
            os.system("cls")

            if 0 <= escolha <= 5:
                if escolha == 0:
                    return
                
                elif escolha == 1:
                    editar_livro()

                elif escolha == 2:
                    listar_autores()
                    id = int(input("\033[94mSelecione o autor que deseja editar (0 para cancelar): \033[0m"))
                    if id == 0:
                        return
                    else:
                        os.system("cls")
                        novo = input("\033[94mDigite o novo nome do autor: \033[0m")
                        editar(id, "id_autor", "autores", "nome_autor", novo)
                        os.system("cls")
                        print("\033[92mAutor alterado com sucesso!\033[0m")
                        time.sleep(2)

                elif escolha == 3:
                    listar_categorias()
                    id = int(input("\033[94mSelecione a categoria que deseja editar (0 para cancelar): \033[0m"))
                    if id == 0:
                        return
                    else:
                        os.system("cls")
                        novo = input("\033[94mDigite o novo nome da categoria: \033[0m")
                        editar(id, "id_categoria", "categorias", "nome_categoria", novo)
                        os.system("cls")
                        print("\033[92mCategoria alterada com sucesso!\033[0m")
                        time.sleep(2)

                elif escolha == 4:
                    listar_editoras()
                    id = int(input("\033[94mSelecione a editora que deseja editar (0 para cancelar): \033[0m"))
                    os.system("cls")
                    print("\033[96mO que deseja editar?\033[0m")
                    print("\033[92m1 - Nome\033[0m")
                    print("\033[92m2 - Endereço\033[0m")
                    print("\033[91m0 - Voltar\033[0m\n")

                    escolha = int(input("\033[94mDigite sua escolha: \033[0m"))
                    os.system("cls")

                    if 0 <= escolha <= 2:
                        if escolha == 0:
                            return
                        elif escolha == 1:
                            novo = input("\033[94mDigite o novo nome da editora: \033[0m")
                            editar(id, "id_editora", "editoras", "nome_editora", novo)
                            print("\033[92mNome da editora atualizado com sucesso!\033[0m")
                            time.sleep(2)
                        
                        elif escolha == 2:
                            novo = input("\033[94mDigite o novo endereço da editora: \033[0m")
                            editar(id, "id_editora", "editoras", "endereco", novo)
                            print("\033[92mEndereço da editora atualizado com sucesso!\033[0m")
                            time.sleep(2)

                elif escolha == 5:
                    editar_cliente()
                    
    except ValueError:
        print("\033[91mPor favor, digite um número válido.\033[0m")
        time.sleep(2)
