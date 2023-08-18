#Le pido al usuario que ingrese dos valores para realizar la division
num1 = int(input("Por favor ingrese el valor del dividendo "))
num2 = int(input("Por favor ingrese el valor del divisor "))

if(num2 == 0):
    #Imprimo un mensaje si el divisor es cero
    print("El divisor no puede ser CERO")
else:
    #Si un numero es divisible su resto es cero
    restoDivision = num1 % num2
    if(restoDivision == 0):
        #Imprimo un mensaje si el numero es divisible
        print("El valor",num1,"ES DIVISIBLE entre",num2)
    else:
        #Imprimo un mensaje si el numero es divisible
        print("El valor",num1," NO ES DIVISIBLE entre",num2)