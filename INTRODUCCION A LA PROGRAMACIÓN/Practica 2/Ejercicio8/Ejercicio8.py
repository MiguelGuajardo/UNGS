#Le pido al usuario un numero
num = int(input("Por favor ingrese un valor "))

#Verifico que el valor sea positivo
if(num < 0):
    print("Por favor ingrese un valor positivo")
elif(num == 0):
    print("Por favor ingrese un valor distinto cero")
else:
    if(num < 10):
        print("Usted ingresó un número de una sola cifra")
    else:
        print("Usted ingresó un número de más de una cifra")