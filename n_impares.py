print("""
---- N  Impares ----

 > Dado un número se determinara la cantidad de números
   impares que hay hasta ese número
""")
n_cantidad = int(input("> Ingrese un número: "))
i = 0

while True:
   if i % 2 != 0:
    print("\n",i, end="\n ")
   i += 1
   if i > n_cantidad:
    break
print("Se mostraron impares hasta ", n_cantidad)
print ("<<< PROGRAMA TERMINADO >>>")
