from services.database import criar_conexao
from services.editoras_services import listar_editoras
from services.categorias_services import listar_categorias
from services.autores_services import listar_autores


def cadastrar_livro():
    conn = criar_conexao()
    if conn is None:
        print("Erro na conexão com o banco de dados.")
        return
    
    try:
        nome_Livro = input("Digite o nome do livro: ")

        listar_categorias()
        id_Categoria = int(input("Escolha a categoria: "))

        listar_autores()
        id_Autor = int(input("Escolha o autor: "))

        listar_editoras()
        id_Editora = int(input("Escolha a editora: "))

        estoque = int(input("Digite a quantidade de livros: "))

        preco = float(input("Digite o preço: "))


        cursor = conn.cursor()
        query = "INSERT INTO livros(nome_Livro, id_Categoria, id_Autor, id_Editora, estoque, preco) VALUES(%s, %s, %s, %s, %s, %s);"
        cursor.execute(query, (nome_Livro, id_Categoria, id_Autor, id_Editora, estoque, preco,))
        conn.commit()
        print("Livro inserido com sucesso!")
    except Exception as e:
        print(f"Erro ao inserir livro: {e}")
    finally:
        cursor.close()
        conn.close()


def listar_livros():
    conn = criar_conexao()
    if conn is None:
        print("Erro na conexão com o banco de dados.")
        return
    
    try:
        cursor = conn.cursor()
        query = "SELECT * FROM livros;"
        cursor.execute(query)
        livros = cursor.fetchall()
        
        if livros:
            print("clientes cadastrados:")
            for livro in livros:

                query_categoria = "SELECT nome_Categoria FROM categorias WHERE id_Categoria = %s;"
                cursor.execute(query_categoria, (livro[2],))
                categoria = cursor.fetchone()[0]

                query_autor = "SELECT nome_Autor FROM autores WHERE id_Autor = %s;"
                cursor.execute(query_autor, (livro[3],))
                autor = cursor.fetchone()[0]

                query_editora = "SELECT nome_Editora FROM editoras WHERE id_Editora = %s;"
                cursor.execute(query_editora, (livro[4],))
                editora = cursor.fetchone()[0]

                print(f"{livro[0]} = {livro[1]} | {categoria} | {autor} | {editora} | {livro[5]} | R${livro[6]}")
        else:
            print("Nenhum livro encontrado.")
    except Exception as e:
        print(f"Erro ao listar livros: {e}")
    finally:
        cursor.close()
        conn.close()