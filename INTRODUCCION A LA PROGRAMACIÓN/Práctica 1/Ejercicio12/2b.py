#Pido un valor para x
x = int(input("Ingrese un valor para x "))
#Pido un valor para y
y = int(input("Ingrese un valor para y "))
#Numerador
numerador = x+y
#Denominador
denominador = x-y
#Verifico que el resultado del denominador sea distinto de 0
if denominador == 0:
    #Imprimo un mensaje en pantalla
    print("\n******************************\n*  Por favor elija otros valores    \n******************************")
else:
    #Realizo la operación
    resultado = numerador/denominador
    #Imprimo un mensaje en pantalla
    print("\n******************************\n*  El resultado es :", resultado,"    \n******************************")
    