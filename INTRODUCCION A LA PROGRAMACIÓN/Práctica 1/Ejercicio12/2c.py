#Pido un valor para x
x = int(input("Ingrese un valor para x "))
#Pido un valor para y
y = int(input("Ingrese un valor para y "))
#Pido un valor para z
z = int(input("Ingrese un valor para z "))
#Verifico que z sea distinto de 0
if z == 0:
    #Imprimo un mensaje en pantalla
    print("\n******************************\n*  Por favor elija otro para z   \n******************************")
else:
    #Numerador
    numerador = x+(y/z)
    #Denominador
    denominador = x-(y/z)
    if denominador == 0:
        #Imprimo un mensaje en pantalla
        print("\n******************************\n*  Por favor elija otros valores    \n******************************")
    else:
        #Realizo la operación
        resultado = numerador/denominador
        #Imprimo un mensaje en pantalla
        print("\n******************************\n*  El resultado es :", resultado,"    \n******************************")