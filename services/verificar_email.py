import re

def verificador(email):
    padrão = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}(?:\.[a-zA-Z]{2,})?$"
    
    if re.match(padrão, email):
        return True
    else:
        return False
