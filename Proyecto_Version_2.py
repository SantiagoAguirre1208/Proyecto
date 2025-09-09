#Menu 
import random
import string
while
print ("Bienvenido a el gestor de contraseñas ¿que te gustaria hacer?")
print ("Opcion 1: GENERADOR DE CONTRASEÑAS SEGURAS")
print ("Opcion 2: VALIDADOR DE CONTRASEÑAS")
Opcion = int(input ("¿OPCION?"))


def validacion(password):
    condiciones = { 
        "longitud": len(password) >= 8,
        "Mayus": any(letra.isupper() for letra in password),
        "minus": any(letra.islower() for letra in password),
        "numero": any(num.isdigit() for num in password),
        "signo" : any( sign in string.punctuation for sign in password)
    }
    return condiciones




def contraseña_nueva (X=12):
        caracteres = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(caracteres) for _ in range (X))

if Opcion == 1:
   
    
    contraseña_final = contraseña_nueva (X=12)

    print ("Tu contraseña segura es: " , contraseña_final)

elif Opcion == 2:
     
    contraseña_dada = input("pon tu contraseña: ")
    verificacion = validacion(contraseña_dada)
    for condiciones, valido in verificacion.items():
        print (f"- {condiciones}: {'mantener' if valido else 'Cambiar'}") 
      



