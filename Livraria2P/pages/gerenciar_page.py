import os
from services.livros_services import cadastrar_livro
from services.clientes_services import cadastrar_cliente
from services.funcionarios_services import cadastrar_funcionario

def gerenciar():
    while True:
        try:
            os.system("cls")
            print("Gerenciar Livraria2P")
            print("1 - Cadastrar Livro")
            print("2 - Cadastrar Cliente")
            print("3 - Cadastrar Funcionario")
            print("0 - Sair\n")
            
            escolha = int(input("Digite sua escolha: "))

            if 0 <= escolha <= 3:
                if escolha == 0:
                    return
                elif escolha == 1:
                    cadastrar_livro()
                elif escolha == 2:
                    cadastrar_cliente()
                elif escolha == 3:
                    cadastrar_funcionario()
            else:
                print("\033[93mErro: Digite um número entre 0 e 2!\033[0m")
        except ValueError:
            print("\033[91mErro: Entrada inválida! Por favor, digite um número.\033[0m")