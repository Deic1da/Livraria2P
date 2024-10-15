from services import *
import time
import os
from services.database import criar_conexao

def vender_livro(produto, funcionario):
    conn = criar_conexao()
    if conn is None:
        print("\033[91mErro na conexão com o banco de dados.\033[0m")
        return
    
    try:
        cursor = conn.cursor()

        query = "SELECT * FROM livros WHERE id_livro = %s;"
        cursor.execute(query, (produto,))
        livros = cursor.fetchall()
        
        if livros:
            print("\033[92mLivro encontrado:\033[0m")
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
                
                os.system("cls")
                print(f"\033[93mID:{livro[0]}\033[0m | Título: {livro[1]} | Categoria: {categoria} | Autor: {autor} | Editora: {editora} | Estoque: {livro[5]} | Preço: R${livro[6]:.2f}\n")  # Mensagem em amarelo
                
            quantidade_vendida = int(input("Digite a quantidade a ser vendida: "))
            
            if quantidade_vendida <= livro[5]:
                if quantidade_vendida >= 0:
                    listar_clientes()
                    id_cliente = int(input("Digite o ID do cliente: "))
                    
                    id_funcionario = funcionario
                    
                    preco_total = quantidade_vendida * livro[6]

                    data_pedido = time.strftime("%Y%m%d")
                    
                    query_pedido = """
                        INSERT INTO pedidos(id_cliente, id_livro, quantidade, preco_pedido, id_funcionario, data_pedido)
                        VALUES (%s, %s, %s, %s, %s, %s);
                    """
                    cursor.execute(query_pedido, (id_cliente, livro[0], quantidade_vendida, preco_total, id_funcionario, data_pedido))
                    conn.commit()

                    novo_estoque = livro[5] - quantidade_vendida
                    query_atualizar = "UPDATE livros SET estoque = %s WHERE id_livro = %s;"
                    cursor.execute(query_atualizar, (novo_estoque, livro[0]))
                    conn.commit()

                    print(f"\033[92mVenda realizada com sucesso!\033[0m Novo estoque: {novo_estoque}")
                    time.sleep(3)
                else:
                    print("\033[91mErro: Quantidade solicitada menor que 0.\033[0m") 
                    time.sleep(3)
            else:
                print("\033[91mErro: Quantidade solicitada excede o estoque disponível.\033[0m") 
                time.sleep(3)
        else:
            print("\033[91mNenhum livro encontrado.\033[0m")
            time.sleep(3)

    except Exception as e:
        print(f"\033[91mErro ao listar ou vender livro: {e}\033[0m") 
        time.sleep(3)

    finally:
        cursor.close()
        conn.close()



def listar_pedidos():
    conn = criar_conexao()
    if conn is None:
        print("\033[91mErro na conexão com o banco de dados.\033[0m")
        return
    
    try:
        cursor = conn.cursor()
        
        query = "SELECT * FROM pedidos;"
        cursor.execute(query)
        pedidos = cursor.fetchall()
        
        if pedidos:
            print("\033[92mPedidos cadastrados:\033[0m")
            print("\033[96mID do Pedido | Cliente              | Livro                    | Quantidade | Preço Total    | Funcionário          | Data\033[0m")
            print("-" * 170)

            for pedido in pedidos:
            
                query_cliente = "SELECT nome FROM clientes WHERE id_cliente = %s;"
                cursor.execute(query_cliente, (pedido[1],))
                cliente = cursor.fetchone()[0]

                query_livro = "SELECT nome_livro FROM livros WHERE id_livro = %s;"
                cursor.execute(query_livro, (pedido[2],))
                livro = cursor.fetchone()[0]
                
                query_funcionario = "SELECT nome FROM funcionarios WHERE id_funcionario = %s;"
                cursor.execute(query_funcionario, (pedido[5],))
                funcionario = cursor.fetchone()[0]

                
                print(f"\033[95m{pedido[0]:<12}\033[0m | \033[94m{cliente:<20}\033[0m | \033[93m{livro:<24}\033[0m | "
                      f"{pedido[3]:<10} | \033[92mR${pedido[4]:<12.2f}\033[0m | \033[96m{funcionario:<20}\033[0m | {pedido[6]}")
                
            input("Aperte qualquer botão para continuar...")
        else:
            print("\033[93mNenhum pedido encontrado.\033[0m")
            time.sleep(1)
        
    except Exception as e:
        print(f"\033[91mErro ao listar pedidos: {e}\033[0m")
        time.sleep(1)
    finally:
        cursor.close()
        conn.close()
