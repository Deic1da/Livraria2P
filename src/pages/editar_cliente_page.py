from services.database import criar_conexao
from services.clientes_services import *
from services.editar_services import editar
import time
import os
from services.verificador import validar_email, validar_cpf, validar_nome

def editar_cliente():
    try:
        listar_clientes()
        id = int(input("\033[94mSelecione o cliente que deseja editar (0 para cancelar): \033[0m"))
        while True:
            os.system("cls")
            print("\033[96mEditar\033[0m")
            print("\033[92m1 - Nome\033[0m")
            print("\033[92m2 - Email\033[0m")
            print("\033[92m3 - Endereço\033[0m")
            print("\033[92m4 - CPF\033[0m")
            print("\033[91m0 - Voltar\033[0m\n")

            escolha = int(input("\033[94mDigite sua escolha: \033[0m"))
            os.system("cls")

            if 0 <= escolha <= 4:
                if escolha == 0:
                    return
                
                elif escolha == 1:
                    novo = input("\033[94mDigite o novo nome do livro: \033[0m")
                    editar(id, "id_cliente", "clientes", "nome", novo)
                    print("\033[92mNome do livro atualizado com sucesso!\033[0m")

                elif escolha == 2:
                    while (True):
                        os.system("cls")
                        novo = input("\033[94mDigite o novo email : \033[0m")
                        if validar_email(novo):
                            editar(id, "id_cliente", "clientes", "email", novo)
                            os.system("cls")
                            print("\033[92mCliente alterado com sucesso!\033[0m")
                            time.sleep(2)
                            break
                        else:
                            print("Algo deu errado")
                            time.sleep(2)
                            break

                elif escolha == 3:
                    os.system("cls")
                    novo = input("\033[94mDigite o novo endereço: \033[0m")
                    editar(id, "id_cliente", "clientes", "endereco", novo)
                    os.system("cls")
                    print("\033[92mCliente alterado com sucesso!\033[0m")
                    time.sleep(2)

                elif escolha == 4:
                    while(True):
                        os.system("cls")
                        novo = input("\033[94mDigite o novo CPF(somente números, 11 dígitos): \033[0m")
                        if validar_cpf(novo):
                            editar(id, "id_cliente", "clientes", "cpf", novo)
                            os.system("cls")
                            print("\033[92mCliente alterado com sucesso!\033[0m")
                            time.sleep(2)
                            break
                        else:
                            print("Algo deu errado")
                            time.sleep(2)
                            break
    except ValueError:
        print("\033[91mPor favor, digite um número válido.\033[0m")
        time.sleep(2)