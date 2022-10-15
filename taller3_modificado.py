#TALLER 3 PYTHON
#AUTOR(A): JUAN CAMILO PEREZ
#FECHA: 14-10-2022
from datetime import datetime
fechacompleta=datetime.now()	
fecha=fechacompleta.date()
nombre=input('Digite su nombre:')
print("Bienvenido",nombre.title())	
print("Hoy es el dia: ", fecha)
a=int(input("digite el valor de A: ")) 
b=int(input("digite el valor de B: ")) 
if a>b:
   print("A es mayor  B") 
if a==b:
    print("A  igual B") 
else:
   print("A es menor que B")
print()
curso1=input('Nombre de asignatura 1:')
curso2=input('Nombre de asignatura 2:')
if curso1 == "Requerimientos" and curso2 == "Algoritmos":
   print ("Usted estudia Programación de Software")
else:
   print ("Usted estudia otro programa diferente a Programación de Software") 
frase=input("digite una oracion:")
print("La frase en minuscula es: ", frase.lower())
longitud=len(frase)
print("La longitud de la frase es: ", len(frase), "caracteres")
if longitud>10:
   print ("La frase contiene mas de 10 caracteres")
else:
   print("La frase contiene menos de 11 caracteres")
print ("*** Script Python taller 3 modificado ***")  
print("FIN")
