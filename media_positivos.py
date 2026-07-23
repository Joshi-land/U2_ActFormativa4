print ("""
<<< MEDIA DE NÚMEROS POSITIVOS >>>

- Se solicitara ingresar números enteros
- Al ingresar un número negativo se finaliza el programa
  se calcula y muestra la media de todos los números positivos

""")

suma = 0
contador = 0

while True:
    num = float(input(" Ingrese un número (Negativo para salir):   "))
    if num < 0: 
        break
    if num > 0:
        suma += num
        contador +=1
if contador > 0:
    media = suma / contador
    print("> Números ingresados: ", contador)
    print("> Media de los números: ", media)
else:
    print("No se han ingresado positivos")