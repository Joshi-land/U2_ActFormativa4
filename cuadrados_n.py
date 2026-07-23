print ("""
--- CUADRADOS HASTA N ---

> Dado un número se daran los cuadrados desde 1 hasta N

 """)
num = int(input("\n > Ingrese un número: "))
i=1
if num < 0:
    num = abs(num)

while True:
    print ("\n",i**2)
    i+= 1
    if i > num:
        break
print("\n > FIN")
print("\n > Se han mostrado todos los cuadrados hasta ", num)

