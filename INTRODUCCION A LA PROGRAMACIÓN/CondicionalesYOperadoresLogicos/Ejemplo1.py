#Le pido al usuario que ingrese un valor
valor = int(input("Por favor ingrese un valor "))
if(valor == 0):
    #Imprimo un mensaje si el valor es cero
    print("El valor no puede ser",valor)
else:
    #Realizo la operación para saber el resto
    restoValor = valor % 2
    if(restoValor == 0):
        #Imprimo un mensaje si el valor es PAR
        print("El valor",valor,"es PAR")
    else:
        #Imprimo un mensaje si el valor es IMPAR
        print("El valor",valor,"es IMPAR")