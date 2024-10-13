from services.database import criar_conexao

def cadastrar_categoria(nome):
    conn = criar_conexao()
    if conn is None:
        print("\033[91mErro na conexão com o banco de dados.\033[0m")
        return
    
    try:
        cursor = conn.cursor()
        query = "INSERT INTO categorias(nome_Categoria) VALUES(%s);"
        cursor.execute(query, (nome,))
        conn.commit()
        print("\033[92mCategoria inserida com sucesso!\033[0m")
    except Exception as e:
        print(f"\033[91mErro ao inserir categoria: {e}\033[0m")
    finally:
        cursor.close()
        conn.close()

def listar_categorias():
    conn = criar_conexao()
    if conn is None:
        print("\033[91mErro na conexão com o banco de dados.\033[0m")
        return
    
    try:
        cursor = conn.cursor()
        query = "SELECT * FROM categorias;"
        cursor.execute(query)
        categorias = cursor.fetchall()
        
        if categorias:
            print("\033[96mCategorias cadastradas:\033[0m")
            print("\033[94mID\033[0m" + " " * 4 + "\033[94mNome da Categoria\033[0m")
            print("-" * 60)
            for categoria in categorias:
                # Formatação com espaçamento
                print(f"\033[92m{categoria[0]:<5}\033[0m" + f" {categoria[1]:<40}")
        else:
            print("\033[93mNenhuma categoria encontrada.\033[0m")
    except Exception as e:
        print(f"\033[91mErro ao listar categorias: {e}\033[0m")
    finally:
        cursor.close()
        conn.close()
