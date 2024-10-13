from services import *

try:
    while True:
        funcionario = login_page()
        if funcionario is not None:
            break

    inicial_page(funcionario)

except Exception as e:
    print(f"\033[91mErro inesperado: {e}\033[0m")
finally:
    print("Desligando...")
