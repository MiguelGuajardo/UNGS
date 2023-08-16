#Le pido al usuario que ingrese el capital a invertir
capInv = float(input("Por favor ingrese el capital a invertir "))
#Le pido al usuario que ingrese la cantidad de meses a invertir
mesInv = float(input("Por favor ingrese los meses a invertir "))
#Realizo la operación del incremento por mes
incInv = capInv * 0.06
#Realizo la operación del incremento por los meses ingresados
productividad = incInv * mesInv
#Realizo la operación de la total
resultado = capInv + productividad
#Imprimo un mensaje en pantalla
print("\n******************************\n*  Total en la cuenta:", resultado,"    \n******************************")