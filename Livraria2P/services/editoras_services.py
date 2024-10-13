from services.database import criar_conexao

def cadastrar_editora(nome, endereco):
    conn = criar_conexao()
    if conn is None:
        print("\033[91mErro na conexão com o banco de dados.\033[0m")
        return
    
    try:
        cursor = conn.cursor()
        query = "INSERT INTO editoras(nome_Editora, endereco) VALUES(%s, %s);"
        cursor.execute(query, (nome, endereco,))
        conn.commit()
        print("\033[92mEditora inserida com sucesso!\033[0m")
    except Exception as e:
        print(f"\033[91mErro ao inserir editora: {e}\033[0m")
    finally:
        cursor.close()
        conn.close()


def listar_editoras():
    conn = criar_conexao()
    if conn is None:
        print("\033[91mErro na conexão com o banco de dados.\033[0m")
        return
    
    try:
        cursor = conn.cursor()
        query = "SELECT * FROM editoras;"
        cursor.execute(query)
        editoras = cursor.fetchall()
        
        if editoras:
            print("Editoras cadastradas:")
            for editora in editoras:
                print(f"{editora[0]} = {editora[1]} | {editora[2]}")
        else:
            print("\033[93mNenhuma editora encontrada.\033[0m")
    except Exception as e:
        print(f"\033[91mErro ao listar editoras: {e}\033[0m")
    finally:
        cursor.close()
        conn.close()
