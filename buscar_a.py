print ("""
<< Contador de letras A >>

- Dada una palabra se determina cuantas letras "a" cotiene

""")

contador = 0
word = input("Ingrese una palabra: \n").lower()

for letra in word:
    if letra == "a":
        contador += 1
print ("Letra A encontrada ", contador, "veces")