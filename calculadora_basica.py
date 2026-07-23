while True:

    print ("""
    <<< CALCULADORA >>>

    ¡Bienvenido!

    Menú:

    1.- Suma
    2.- Resta
    3.- Multiplicación
    4.- División
    5.- Salir
     """)

    opc = int(input("Seleccione una opción: "))
    if opc == 5:
        break
    
    match opc:
        case 1:
            num_a=float(input("Ingrese un primer número: "))
            num_b=float(input("Ingrese un segundo número: "))
            oper = "Suma"
            print("Operación: ", oper)
            print("Numeros a operar: ", num_a, num_b)
            print(num_a+num_b)
        case 2:
            num_a=float(input("Ingrese un primer número: "))
            num_b=float(input("Ingrese un segundo número: "))
            oper = "Resta"
            print("Operación: ", oper)
            print("Numeros a operar: ", num_a, num_b)
            print(num_a-num_b)
        case 3:
            num_a=float(input("Ingrese un primer número: "))
            num_b=float(input("Ingrese un segundo número: "))
            oper = "Multiplicación"
            print("Operación: ", oper)
            print("Numeros a operar: ", num_a, num_b)
            print(num_a*num_b)
        case 4:
            num_a=float(input("Ingrese un primer número: "))
            num_b=float(input("Ingrese un segundo número: "))
            oper = "División"
            if num_b!=0:
                print("Operación: ", oper)
                print("Numeros a operar: ", num_a, num_b)
                print (num_a / num_b)
            else:
                print (" <<< ERROR DIVISIÓN POR CERO >>> ")
        case _:
            print(" --- ERROR ---")
    
    respuesta = input("¿Desea continuar? (s/n): ").lower()
    if respuesta == "n":
        print ("<<< ADIOS >>>")
        break
   
            
            




