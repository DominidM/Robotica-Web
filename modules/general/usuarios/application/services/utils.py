import random
import string

def generar_registro_key():
    grupos = []
    for _ in range(3):
        grupo = ''.join(random.choices(string.ascii_uppercase + string.digits, k=3))
        grupos.append(grupo)
    return "-".join(grupos)