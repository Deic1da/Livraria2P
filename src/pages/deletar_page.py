import time
import os
from services.deletar_services import deletar
from services.livros_services import *
from services.funcionarios_services import listar_funcionarios

def deletar_page():
    try:
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
            os.system("cls")

            if 0 <= escolha <= 5:
                if escolha == 0:
                    return
                elif escolha == 1:
                    listar_livros()
                    id = input("Selecione o livro que deseja deletar(0 para cancelar):")
                    os.system("cls")
                    deletar(id,"livros","id_livro")
                
                elif escolha == 2:
                    listar_autores()
                    id = input("Selecione o autor que deseja deletar(0 para cancelar):")
                    os.system("cls")
                    deletar(id,"autores","id_autor")
                
                elif escolha == 3:
                    listar_categorias()
                    id = input("Selecione categoria que deseja deletar(0 para cancelar):")
                    os.system("cls")
                    deletar(id,"categorias","id_categoria")
                
                elif escolha == 4:
                    listar_editoras()
                    id = input("Selecione a editora que deseja deletar(0 para cancelar):")
                    os.system("cls")
                    deletar(id,"editoras","id_editora")
                
                elif escolha == 5:
                    listar_funcionarios()
                    id = input("Selecione o funcionario que deseja deletar(0 para cancelar):")
                    os.system("cls")
                    deletar(id,"funcionarios","id_funcionario")

    except ValueError:
        print("\033[91mPor favor, digite um número válido.\033[0m")
        time.sleep(2)