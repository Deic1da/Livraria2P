from services import *
import time
import os

def login_page():
    os.system('cls')
    print("\033[94mLivraria2P\033[0m")
    tentativa = tentativa_login()
    
    if tentativa is not None:
        time.sleep(1)
        return tentativa
    else:
        print("\033[91mErro: Login falhou. Tente novamente.\033[0m")
        time.sleep(1)
        return None
