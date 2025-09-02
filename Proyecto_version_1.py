#Codigo para un algoritmo que crea contraseñas seguras
import random
Pregunta_1 = input ("¿quieres revisar tu contraseña?") 
if Pregunta_1 == 'si':
    Contraseña_dada = input("Introduce tu contraseña")
       
else:
    Pregunta_2 = input ("¿quieres crear una contraseña segura?") 
    if Pregunta_2 =='si':
        print ("tu nueva contraseña segura es: ")