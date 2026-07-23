import random

intentos = 0
num_secreto = random.randint(1,100)
print("""
<<<<<<< ADIVINE EL NUMERO>>>>>>>
""")
while True:
    num_intento = int(input("Ingrese su intento: "))

    if num_intento > num_secreto:
        print("Demasiado alto, intente otra vez")
        intentos += 1
    elif num_intento < num_secreto:
        print("Demasiado bajo, intente otra vez")
        intentos += 1
    else:
        intentos +=1
        print("¡¡BIEN HECHO HA ADIVINADO CORRECTAMENTE !!")
        break

print ("<<<<<<< JUEGO TERMINADO >>>>>>>")
print ("Número: ", num_secreto)
print ("Número de intentos: ", intentos)
