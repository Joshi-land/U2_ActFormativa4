print(""" 
<<<< VOCALES O CONSONANTES >>>>

- Dadas las letras ingresadas por el usuario se determinara si es vocal o consonante

"""
)

contador_v = 0
contador_c = 0

while True:
    letra = input("Ingrese una letra (Espacio para salir): ")
    if  letra == " ":
        break
    if letra in "aeiou":
        print ("V O C A L")
        contador_v+=1
    else:
        print("C O N S O N A N T E")
        contador_c+=1
print("Vocales ingresadas: ", contador_v)
print("Consonantes ingresadas: ", contador_c)
print("<<< PROGRAMA FINALIZADO >>>")