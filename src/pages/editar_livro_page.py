import time
import os
from services.livros_services import *
from services.editar_services import editar
from services.categorias_services import *
from services.autores_services import *
from services.editoras_services import *
from services.pesquisar_elemento_one_services import pesquisar_elemento_one

def editar_livro():
    try:
        listar_livros()
        id = input("\033[94mSelecione o livro que deseja editar (0 para cancelar): \033[0m")
        os.system("cls")
        print("\033[96mO que deseja editar?\033[0m")
        print("\033[92m1 - Nome\033[0m")
        print("\033[92m2 - Categoria\033[0m")
        print("\033[92m3 - Autor\033[0m")
        print("\033[92m4 - Editora\033[0m")
        print("\033[92m5 - Estoque\033[0m")
        print("\033[92m6 - Preço\033[0m\n")
        print("\033[91m0 - Voltar\033[0m\n")

        escolha = int(input("\033[94mDigite sua escolha: \033[0m"))
        os.system("cls")

        if 0 <= escolha <= 6:
            if escolha == 0:
                return
            
            elif escolha == 1:
                novo = input("\033[94mDigite o novo nome do livro: \033[0m")
                editar(id, "id_livro", "livros", "nome_livro", novo)
                print("\033[92mNome do livro atualizado com sucesso!\033[0m")
            
            elif escolha == 2:
                listar_categorias()
                novo = int(input("\033[94mEscolha a categoria (ou digite 0 para cadastrar uma nova): \033[0m"))
                if novo == 0:
                    os.system("cls")
                    categoria = input("\033[94mDigite o nome da nova categoria: \033[0m")
                    cadastrar_categoria(categoria)
                    os.system("cls")
                    listar_categorias()
                    novo = int(input("\033[94mEscolha uma categoria: \033[0m"))
                editar(id, "id_livro", "livros", "id_categoria", novo)
                print("\033[92mCategoria atualizada com sucesso!\033[0m")

            elif escolha == 3:
                listar_autores()
                novo = int(input("\033[94mEscolha o autor (ou digite 0 para cadastrar um novo): \033[0m"))
                if novo == 0:
                    os.system("cls")
                    autor = input("\033[94mDigite o nome do novo autor: \033[0m")
                    cadastrar_autor(autor)
                    os.system("cls")
                    listar_autores()
                    novo = int(input("\033[94mEscolha um autor: \033[0m"))  
                editar(id, "id_livro", "livros", "id_autor", novo)
                print("\033[92mAutor atualizado com sucesso!\033[0m")

            elif escolha == 4:
                listar_editoras()
                novo = int(input("\033[94mEscolha a editora (ou digite 0 para cadastrar uma nova): \033[0m"))
                if novo == 0:
                    os.system("cls")
                    nome = input("\033[94mDigite o nome da nova editora: \033[0m")
                    endereco = input("\033[94mDigite o endereço da editora: \033[0m")
                    cadastrar_editora(nome, endereco)
                    os.system("cls")
                    listar_editoras()
                    novo = int(input("\033[94mEscolha uma editora: \033[0m"))  
                editar(id, "id_livro", "livros", "id_editora", novo)
                print("\033[92mEditora atualizada com sucesso!\033[0m")

            elif escolha == 5:
                escolha = int(input("\033[94m1 - Adicionar\n2 - Alterar\nDigite sua escolha: \033[0m"))
                os.system("cls")
                
                if escolha == 1:
                    valor = pesquisar_elemento_one(id, "estoque", "livros", "id_livro")
                    print(f"\033[93mEstoque atual: {valor}\033[0m")
                    novo = int(input("\033[94mDigite o valor a acrescentar: \033[0m")) + valor
                    os.system("cls")
                    editar(id, "id_livro", "livros", "estoque", novo)
                    print(f"\033[92mEstoque atualizado para {novo}!\033[0m")
                    time.sleep(2)

                elif escolha == 2:
                    valor = pesquisar_elemento_one(id, "estoque", "livros", "id_livro")
                    print(f"\033[93mEstoque atual: {valor}\033[0m")
                    novo = int(input("\033[94mDigite o novo valor: \033[0m"))
                    os.system("cls")
                    editar(id, "id_livro", "livros", "estoque", novo)
                    print(f"\033[92mEstoque atualizado para {novo}!\033[0m")
                    time.sleep(2)
                else:
                    return

            elif escolha == 6:
                valor = pesquisar_elemento_one(id, "preco", "livros", "id_livro")
                print(f"\033[93mPreço atual: R${valor}\033[0m")
                novo = float(input("\033[94mDigite o novo preço do livro: \033[0m"))
                os.system("cls")
                editar(id, "id_livro", "livros", "preco", novo)
                print(f"\033[92mPreço atualizado para R${novo}!\033[0m")
                time.sleep(2)

    except ValueError:
        print("\033[91mPor favor, digite um número válido.\033[0m")
        time.sleep(2)
