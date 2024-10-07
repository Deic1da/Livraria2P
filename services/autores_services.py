from services.database import criar_conexao

def cadastrar_autor(nome):
    conn = criar_conexao()
    if conn is None:
        print("Erro na conexão com o banco de dados.")
        return
    
    try:
        cursor = conn.cursor()
        query = "INSERT INTO autores(nome_Autor) VALUES(%s);"
        cursor.execute(query, (nome,))
        conn.commit()
        print("Autor inserido com sucesso!")
    except Exception as e:
        print(f"Erro ao inserir autor: {e}")
    finally:
        cursor.close()
        conn.close()

def listar_autores():
    conn = criar_conexao()
    if conn is None:
        print("Erro na conexão com o banco de dados.")
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
            print("Nenhum autor encontrado.")
    except Exception as e:
        print(f"Erro ao listar autores: {e}")
    finally:
        cursor.close()
        conn.close()