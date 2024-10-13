from pages.login_page import login
from pages.pagina_inicial import pagina_inicial

while True:
    id_funcionario = login()
    if id_funcionario is not None:
       break

pagina_inicial(id_funcionario)

print("Desligando...")