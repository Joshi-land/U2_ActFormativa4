print(""" 
<<< Factorial de un Número >>> 

- Dado un número calcular su factorial

""" )

num = int(input("Ingrese un número: \n"))
factorial= 1 

if num < 0:
    print ("\n #ERROR FACTORIAL NO DETERMINADO PARA NUM NEGATIVOS")
else:
    for i in range(1, num +1):
        factorial *= i
        print ("\n El factorial de ", num, " es ", factorial)
    