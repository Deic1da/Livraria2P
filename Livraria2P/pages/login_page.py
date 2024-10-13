from services.login import *
import os
import time

def login():
        os.system('cls')
        print("Livraria2P")
        tentativa = tentativa_login()
        if tentativa is not None:
                return tentativa
        else:
                return None
        time.sleep (2)
        
        