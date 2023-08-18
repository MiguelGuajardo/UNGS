#Le pido al usuario dos valores para establecer el signo
num1 = int(input("Por favor ingrese el primer valor "))
num2 = int(input("Por favor ingrese el segundo valor "))

if(num1 == 0 or num2 == 0):
    #Imprimo un mensaje si alguno de los valores es cero
    print("Al cero no se le puede asignar signo")
else:
    if((num1 > 0 and num2 > 0) or (num1 < 0 and num2 < 0)):
        #Imprimo un mensaje en el caso que ambos sean positivo o negativos
        print("El signo de la multiplicación es positivo")
    else:
        #Imprimo un mensaje en el caso que ambos valores tenga signos contrarios
        print("El signo de la multiplicación es negativo")
