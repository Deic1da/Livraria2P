from services.database import criar_conexao

def cadastrar_editora(nome,endereco):
    conn = criar_conexao()
    if conn is None:
        print("Erro na conexão com o banco de dados.")
        return
    
    try:
        cursor = conn.cursor()
        query = "INSERT INTO editoras(nome_Editora, endereco) VALUES(%s, %s);"
        cursor.execute(query, (nome, endereco,))
        conn.commit()
        print("Editora inserida com sucesso!")
    except Exception as e:
        print(f"Erro ao inserir editora: {e}")
    finally:
        cursor.close()
        conn.close()


def listar_editoras():
    conn = criar_conexao()
    if conn is None:
        print("Erro na conexão com o banco de dados.")
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
            print("Nenhuma editora encontrada.")
    except Exception as e:
        print(f"Erro ao listar editoras: {e}")
    finally:
        cursor.close()
        conn.close()