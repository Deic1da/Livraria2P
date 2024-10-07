from services.database import criar_conexao

def cadastrar_categoria(nome):
    conn = criar_conexao()
    if conn is None:
        print("Erro na conexão com o banco de dados.")
        return
    
    try:
        cursor = conn.cursor()
        query = "INSERT INTO categorias(nome_Categoria) VALUES(%s);"
        cursor.execute(query, (nome,))
        conn.commit()
        print("Categoria inserida com sucesso!")
    except Exception as e:
        print(f"Erro ao inserir categoria: {e}")
    finally:
        cursor.close()
        conn.close()

def listar_categorias():
    conn = criar_conexao()
    if conn is None:
        print("Erro na conexão com o banco de dados.")
        return
    
    try:
        cursor = conn.cursor()
        query = "SELECT * FROM categorias;"
        cursor.execute(query)
        categorias = cursor.fetchall()
        
        if categorias:
            print("Categorias cadastradas:")
            for categoria in categorias:
                print(f"{categoria[0]} = {categoria[1]}")
        else:
            print("Nenhuma categoria encontrada.")
    except Exception as e:
        print(f"Erro ao listar categorias: {e}")
    finally:
        cursor.close()
        conn.close()