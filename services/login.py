from services.database import criar_conexao

def tentativa_login(email, senha):
    conn = criar_conexao()
    if conn is None:
        print("Erro na conexão com o banco de dados.")
        return False
    
    try:
        cursor = conn.cursor()
        query = "SELECT senha FROM funcionarios WHERE email = %s;"
        cursor.execute(query, (email,))
        funcionario = cursor.fetchone()
        
        if funcionario is None:
            print("Email não encontrado!")
            return False
        
        senha_armazenada = funcionario[0]
        if senha_armazenada == senha:
            print("Login realizado com sucesso!")
            return True
        else:
            print("Senha incorreta!")
            return False
    
    except Exception as e:
        print(f"Erro ao tentar logar: {e}")
        return False
    
    finally:
        cursor.close()
        conn.close()
