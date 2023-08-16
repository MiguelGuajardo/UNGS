#Pido un valor para x
x = int(input("Ingrese un valor para x "))
#Pido un valor para y
y = int(input("Ingrese un valor para y "))
#Verifico que el valor para y no sea 0
if y != 0:
    #Realizo la operación si y es distinto de 0
    resultado = (x/y) + 1
    #Imprimo en pantalla el resultado
    print("******************************\n*  El resultado es :", resultado,"    \n******************************")
else:
    #Imprimo un mensaje en pantalla
    print("\n******************************\n*  La division entre 0 no esta permitida!    \n******************************")