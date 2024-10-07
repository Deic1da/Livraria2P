from services.database import criar_conexao

def cadastrar_cliente(nome, email, endereco, cpf, data_Nascimento):
    conn = criar_conexao()
    if conn is None:
        print("Erro na conexão com o banco de dados.")
        return
    
    try:
        cursor = conn.cursor()
        query = "INSERT INTO clientes(nome, email, endereco, cpf, data_Nascimento) VALUES(%s, %s, %s, %s, %s);"
        cursor.execute(query, (nome, email, endereco, cpf, data_Nascimento,))
        conn.commit()
        print("Cliente inserido com sucesso!")
    except Exception as e:
        print(f"Erro ao inserir cliente: {e}")
    finally:
        cursor.close()
        conn.close()
    

def listar_clientes():
    conn = criar_conexao()
    if conn is None:
        print("Erro na conexão com o banco de dados.")
        return
    
    try:
        cursor = conn.cursor()
        query = "SELECT * FROM clientes;"
        cursor.execute(query)
        clientes = cursor.fetchall()
        
        if clientes:
            print("clientes cadastrados:")
            for cliente in clientes:
                print(f"{cliente[0]} = {cliente[1]} | {cliente[4]}")
        else:
            print("Nenhum cliente encontrado.")
    except Exception as e:
        print(f"Erro ao listar clientes: {e}")
    finally:
        cursor.close()
        conn.close()
