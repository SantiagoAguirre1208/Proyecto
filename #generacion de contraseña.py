#generacion de contraseña

import random
import string

def contraseña_nueva(X=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range (X))


contraseña_final = contraseña_nueva (X=12)

print ("Tu contraseña segura es: " , contraseña_final)