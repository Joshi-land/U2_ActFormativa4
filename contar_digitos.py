print ("""
<<< CONTADOR DE DIGITOS >>>

- Dado un número se determinara la cantidad de digitos de este

""")
num = int(input(" -- Ingrese un número: "))
num_orig= num

if num == 0:
    digit = 1
else:
    digit = 0
    if num < 0:
        num = abs(num)
        num_orig =num

while num > 0:
     num //= 10
     digit +=1
print("\n > El número: ", num_orig, " tiene ", digit, "dígitos")


