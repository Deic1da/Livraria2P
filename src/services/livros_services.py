from services import *
import time
import os
from services.database import criar_conexao

def cadastrar_livro():
    conn = criar_conexao()
    if conn is None:
        print("\033[91mErro na conexão com o banco de dados.\033[0m")
        return
    
    try:
        os.system("cls")
        nome_Livro = input("Digite o nome do livro: ").strip()
        
        os.system("cls")
        listar_categorias()
        id_Categoria = int(input("Escolha a categoria (ou digite 0 para cadastrar uma nova): "))
        if id_Categoria == 0:
            os.system("cls")
            nome_categoria = input("Digite o nome da categoria: ")
            cadastrar_categoria(nome_categoria)
            os.system("cls")
            listar_categorias()
            id_Categoria = int(input("Escolha uma categoria: "))

        os.system("cls")
        listar_autores()
        id_Autor = int(input("Escolha o autor (ou digite 0 para cadastrar um novo): "))
        if id_Autor == 0:
            os.system("cls")
            nome_autor = input("Digite o nome do autor: ")
            cadastrar_autor(nome_autor)
            os.system("cls")
            listar_autores()
            id_Autor = int(input("Escolha um autor: "))  

        os.system("cls")
        listar_editoras()
        id_Editora = int(input("Escolha a editora (ou digite 0 para cadastrar uma nova): "))
        if id_Editora == 0:
            os.system("cls")
            nome_editora = input("Digite o nome da editora: ")
            endereco_editora = input("Digite o endereço da editora: ")
            cadastrar_editora(nome_editora, endereco_editora)
            os.system("cls")
            listar_editoras()
            id_Editora = int(input("Escolha a editora: "))

        while(True):
            os.system("cls")
            estoque = int(input("Digite a quantidade de livros(0 para sair): "))
            if estoque<0:
                print("\033[91mErro: A quantidade de livros não pode ser negativa.\033[0m")
            else:
                break
        while(True):
            os.system("cls")
            preco = float(input("Digite o preço(0 para sair): "))
            if preco<0:
                print("\033[91mErro: O preço não pode ser negativo.\033[0m")
            else:
                break
        cursor = conn.cursor()
        query = "INSERT INTO livros(nome_Livro, id_Categoria, id_Autor, id_Editora, estoque, preco) VALUES(%s, %s, %s, %s, %s, %s);"
        cursor.execute(query, (nome_Livro, id_Categoria, id_Autor, id_Editora, estoque, preco,))
        conn.commit()
        os.system("cls")
        print("\033[92mLivro inserido com sucesso!\033[0m")
        time.sleep(2)
    except Exception as e:
        os.system("cls")
        print(f"\033[91mErro ao inserir livro: {e}\033[0m")
        time.sleep(2)
    finally:
        cursor.close()
        conn.close()


def listar_livros():
    conn = criar_conexao()
    if conn is None:
        print("\033[91mErro na conexão com o banco de dados.\033[0m")
        return
    
    try:
        cursor = conn.cursor()
        query = """SELECT l.id_livro, l.nome_livro, c.nome_Categoria AS categoria, a.nome_Autor AS autor, e.nome_Editora AS editora, l.estoque, l.preco
        FROM livros l
        JOIN categorias c ON l.id_Categoria = c.id_Categoria
        JOIN autores a ON l.id_Autor = a.id_Autor
        JOIN editoras e ON l.id_Editora = e.id_Editora
        ORDER BY l.id_livro ASC;"""
        cursor.execute(query)
        livros = cursor.fetchall()
        
        if livros:
            print("\033[96mLivros cadastrados:\033[0m")
            print(f"{'ID':<5} | {'Título':<50} | {'Categoria':<30} | {'Autor':<30} | {'Editora':<30} | {'Estoque':<10} | {'Preço':<15}")
            print("-" * 180)
            for livro in livros:
                print(f"\033[92m{livro[0]:<5}\033[0m | {livro[1]:<50} | \033[93m{livro[2]:<30}\033[0m | \033[94m{livro[3]:<30}\033[0m | \033[95m{livro[4]:<30}\033[0m | {livro[5]:<10} | R${livro[6]:<15}")
        else:
            print("\033[93mNenhum livro encontrado.\033[0m")
    except Exception as e:
        print(f"\033[91mErro ao listar livros: {e}\033[0m")
    finally:
        cursor.close()
        conn.close()



def listar_livros_personalisado(autor2, pesquisa):
    conn = criar_conexao()
    if conn is None:
        print("\033[91mErro na conexão com o banco de dados.\033[0m")
        return
    
    try:
        cursor = conn.cursor()
        query = f"""SELECT l.id_livro, l.nome_livro, c.nome_Categoria AS categoria, a.nome_Autor AS autor, e.nome_Editora AS editora, l.estoque, l.preco
        FROM livros l
        JOIN categorias c ON l.id_Categoria = c.id_Categoria
        JOIN autores a ON l.id_Autor = a.id_Autor
        JOIN editoras e ON l.id_Editora = e.id_Editora
        WHERE l.{pesquisa} = %s
        ORDER BY l.id_livro ASC;"""
        cursor.execute(query, (autor2,))
        livros = cursor.fetchall()
        
        if livros:
            os.system("cls")
            print("\033[96mLivros cadastrados:\033[0m")
            print(f"{'ID':<5} | {'Título':<50} | {'Categoria':<30} | {'Autor':<30} | {'Editora':<30} | {'Estoque':<10} | {'Preço':<15}")
            print("-" * 180) 
            for livro in livros:
                print(f"\033[92m{livro[0]:<5}\033[0m | {livro[1]:<50} | \033[93m{livro[2]:<30}\033[0m | \033[94m{livro[3]:<30}\033[0m | \033[95m{livro[4]:<30}\033[0m | {livro[5]:<10} | R${livro[6]:<15}")
        else:
            print("\033[93mNenhum livro encontrado.\033[0m")
    except Exception as e:
        print(f"\033[91mErro ao listar livros: {e}\033[0m")
    finally:
        cursor.close()
        conn.close()


def procurar_por_nome(pesquisa):
    conn = criar_conexao()
    if conn is None:
        print("\033[91mErro na conexão com o banco de dados.\033[0m")
        return
    
    try:
        cursor = conn.cursor()
        query = """SELECT l.id_livro, l.nome_livro, c.nome_Categoria AS categoria, a.nome_Autor AS autor, e.nome_Editora AS editora, l.estoque, l.preco
        FROM livros l
        JOIN categorias c ON l.id_Categoria = c.id_Categoria
        JOIN autores a ON l.id_Autor = a.id_Autor
        JOIN editoras e ON l.id_Editora = e.id_Editora
        WHERE l.nome_livro ILIKE %s
        ORDER BY l.id_livro ASC;"""
        cursor.execute(query, ('%' + pesquisa + '%',))
        livros = cursor.fetchall()

        if livros:
            print("\033[96mResultados da pesquisa:\033[0m")
            print(f"{'ID':<5} | {'Título':<50} | {'Categoria':<30} | {'Autor':<30} | {'Editora':<30} | {'Estoque':<10} | {'Preço':<15}")
            print("-" * 180)
            for livro in livros:
                print(f"\033[92m{livro[0]:<5}\033[0m | {livro[1]:<50} | \033[93m{livro[2]:<30}\033[0m | \033[94m{livro[3]:<30}\033[0m | \033[95m{livro[4]:<30}\033[0m | {livro[5]:<10} | R${livro[6]:<15}")
        else:
            print("\033[93mNenhum livro encontrado com esse nome.\033[0m")
    except Exception as e:
        print(f"\033[91mErro ao listar: {e}\033[0m")
    finally:
        cursor.close()
        conn.close()
