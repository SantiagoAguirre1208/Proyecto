#PRUEBA DE VALIDAR CONTRASEÑA CORRECTA



import random
import string
#MENU + BUCLE 
Opcion = 0
while Opcion <= 3:
    print("Opcion 1: GENERADOR DE CONTRASEÑAS SEGURAS")
    print("Opcion 2: VALIDADOR DE CONTRASEÑAS")
    print("Opcion 3: SALIR")
    Opcion = int(input("¿OPCION? "))


#FUNCION DE VALIDACION DE CONTRASEÑAS
    def validacion(password):
        condiciones = { 
            "longitud": len(password) >= 8,
            "Mayus": any(letra.isupper() for letra in password),
            "minus": any(letra.islower() for letra in password),
            "numero": any(num.isdigit() for num in password),
            "signo": any(sign in string.punctuation for sign in password)
        }
        return condiciones



#FUNCION DE CONTRASEÑAS NUEVAS
    def contraseña_nueva(X=12):
        caracteres = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(caracteres) for _ in range(X))



#IF DONDE SE LLAMAN LAS FUNCIONES
    if Opcion == 1:
        contraseña_final = contraseña_nueva(12)
        print("TU CONTRASEÑA ES: ", contraseña_final)

    elif Opcion == 2:
        contraseña_dada = input("PON TU CONTRASEÑA: ")
        verificacion = validacion(contraseña_dada)
        for condiciones, valido in verificacion.items():
            print(f"- {condiciones}: {'mantener' if valido else 'Cambiar'}") 
            if all(verificacion.values()) == True:
                print("TU CONTRASEÑA ES SEGURA")
            else:
                print("TU CONTRASEÑA NO ES SEGURA")

    elif Opcion == 3:
        print("SALISTE DEL PROGRAMA")
        break

    else:
        print("OPCION INVALIDA")
        Opcion = 0