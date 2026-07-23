print("""
<<< SECUENCIA ARITMETICA >>>

- Dado un número se generara un sucesión hasta dicho número
- Se solicitara el número con el que iniciara la sucesión
- Así como la diferencia de la sucesión

 """)

limite = int(input("\n > Ingrese el límite de la sucesión: "))
inicio = int(input("> Ingrese el inicio de la sucesión: "))
diferencia = int(input("> Ingrese la diferencia: "))
num_sucesion = inicio

while True:
    print(num_sucesion," ")
    num_sucesion += diferencia
    if num_sucesion > limite:
        break
print("\n > Secuencia aritmética desde ", inicio, " hasta ", limite)
