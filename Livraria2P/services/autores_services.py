from services.database import criar_conexao

def cadastrar_autor(nome):
    conn = criar_conexao()
    if conn is None:
        print("\033[91mErro na conexão com o banco de dados.\033[0m")
        return
    
    try:
        cursor = conn.cursor()
        query = "INSERT INTO autores(nome_Autor) VALUES(%s);"
        cursor.execute(query, (nome,))
        conn.commit()
        print("\033[92mAutor inserido com sucesso!\033[0m")
    except Exception as e:
        print(f"\033[91mErro ao inserir autor: {e}\033[0m")
    finally:
        cursor.close()
        conn.close()

def listar_autores():
    conn = criar_conexao()
    if conn is None:
        print("\033[91mErro na conexão com o banco de dados.\033[0m")
        return
    
    try:
        cursor = conn.cursor()
        query = "SELECT * FROM autores;"
        cursor.execute(query)
        autores = cursor.fetchall()
        
        if autores:
            print("Autores cadastrados:")
            for autor in autores:
                print(f"{autor[0]} = {autor[1]}")
        else:
            print("\033[93mNenhum autor encontrado.\033[0m")
    except Exception as e:
        print(f"\033[91mErro ao listar autores: {e}\033[0m")
    finally:
        cursor.close()
        conn.close()
