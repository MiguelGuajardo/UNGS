#Declaro los billetes
milPesos = 1000
quinientosPesos = 500
doscientosPesos = 200
cienPesos = 100
cincuentaPesos = 50
#Le pido al usuario que ingrese el valor de la extracción
monto = int(input("Por favor ingrese el monto que desea retirar "))
#Realizo operaciones según los restos
cociente1000 = monto // 1000
resto1000 = monto % 1000
cociente500 = resto1000 // 500
resto500 = resto1000 % 500
cociente200 = resto500 // 200
resto200 = resto500 % 200
cociente100 = resto200 // 100
resto100 = resto200 % 100
cociente50 = resto100 // 50
resto50 = resto100 % 50
#Imprimo un mensaje en pantalla
print("\n******************************\n*  Usted recibirá:\n*", cociente1000," billetes de $ 1000   \n*", cociente500," billetes de $ 500   \n*", cociente200," billetes de $ 200   \n*", cociente100," billetes de $ 100   \n*", cociente50," billetes de $ 50   \n* El monto restante en el cajero es de:$",resto50,"\n*****************************")
