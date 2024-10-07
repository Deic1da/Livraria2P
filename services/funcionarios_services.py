from services.database import criar_conexao

def cadastrar_funcionario(nome,email,senha):
    conn = criar_conexao()
    if conn is None:
        print("Erro na conexão com o banco de dados.")
        return
    
    try:
        cursor = conn.cursor()
        query = "INSERT INTO funcionarios(nome,email,senha) VALUES(%s,%s,%s);"
        cursor.execute(query, (nome,email,senha))
        conn.commit()
        print("Funcionario inserido com sucesso!")
    except Exception as e:
        print(f"Erro ao inserir funcionario: {e}")
    finally:
        cursor.close()
        conn.close()