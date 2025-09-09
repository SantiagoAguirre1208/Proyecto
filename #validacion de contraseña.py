#validacion de contraseña

import string
import random


def validacion(password):
    condiciones = { 
        "longitud": len(password) >= 8,
        "Mayus": any(letra.isupper() for letra in password),
        "minus": any(letra.islower() for letra in password),
        "numero": any(num.isdigit() for num in password),
        "signo" : any( sign in string.punctuation for sign in password)
    }
    return condiciones


contraseña_dada = input("pon tu contraseña")
verificacion = validacion(contraseña_dada)
for condiciones, valido in verificacion.items():
    print (f"- {condiciones}: {'mantener' if valido else 'Cambiar'}") 
  

                