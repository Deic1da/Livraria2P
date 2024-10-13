from pages.login_page import login
from pages.pagina_inicial import pagina_inicial

try:
    while True:
        id_funcionario = login()
        if id_funcionario is not None:
            break

    pagina_inicial(id_funcionario)

except Exception as e:
    print(f"\033[91mErro inesperado: {e}\033[0m")
finally:
    print("Desligando...")
