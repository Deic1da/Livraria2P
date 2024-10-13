from services.database import criar_conexao
import time

def tentativa_login():
    conn = criar_conexao()
    if conn is None:
        print("\033[91mErro na conexão com o banco de dados!\033[0m")
        return None
    
    try:
        email = input("Digite o email: ")

        cursor = conn.cursor()
        query = "SELECT id_funcionario, senha FROM funcionarios WHERE email = %s;"
        cursor.execute(query, (email,))
        funcionario = cursor.fetchone()
        
        if funcionario is None:
            print("\033[91mEmail não encontrado!\033[0m")
            time.sleep(2)
            return None

        senha = input("Digite a senha: ")
        
        senha_armazenada = funcionario[1]
        id_funcionario = funcionario[0]
        if senha_armazenada == senha:
            print(f"\033[92mLogin realizado com sucesso!\033[0m")
            time.sleep(2)
            return str(id_funcionario)
        else:
            print("\033[91mSenha incorreta!\033[0m")
            time.sleep(2)
            return None
    
    except Exception as e:
        print(f"\033[91mErro ao tentar logar: {e}\033[0m")
        time.sleep(2)
        return None
    
    finally:
        cursor.close()
        conn.close()