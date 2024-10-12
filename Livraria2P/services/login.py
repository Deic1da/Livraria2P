from services.database import criar_conexao

def tentativa_login():
    conn = criar_conexao()
    if conn is None:
        print("\033[91mErro na conexão com o banco de dados!\033[0m")
        return False
    
    try:
        email = input("Digite o email: ")

        cursor = conn.cursor()
        query = "SELECT senha FROM funcionarios WHERE email = %s;"
        cursor.execute(query, (email,))
        funcionario = cursor.fetchone()
        
        if funcionario is None:
            print("\033[91mEmail não encontrado!\033[0m")
            return False

        senha = input("Digite a senha: ")
        
        senha_armazenada = funcionario[0]
        if senha_armazenada == senha:
            print(f"\033[92mLogin realizado com sucesso!\033[0m")
            return True
        else:
            print("\033[91mSenha incorreta!\033[0m")
            return False
    
    except Exception as e:
        print(f"\033[91mErro ao tentar logar: {e}\033[0m")
        return False
    
    finally:
        cursor.close()
        conn.close()
