print (" B I E N V E N I D O")
print ("""
-- Dada una cantidad de números se determinara si estos son:
  > Mayores a 0
  > Menores a 0
  > Iguales a 0
""")
cantidad = int(input("Ingrese la cantidad de números a analizar: "))
mayores = 0 
menores = 0
iguales = 0

for i in range(cantidad):
    num = int(input("Número: "))
    if num > 0:
        mayores += 1
    elif num < 0:
        menores += 1
    else:
        iguales +=1

print("> Mayores a 0: ",mayores)
print("> Menores a 0: ", menores)
print("> Iguales a 0: ", iguales)