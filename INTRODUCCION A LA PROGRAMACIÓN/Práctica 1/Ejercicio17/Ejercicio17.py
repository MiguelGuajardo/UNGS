#Declaro los billetes
milPesos = 1000
quinientosPesos = 500
doscientosPesos = 200
cienPesos = 100
cincuentaPesos = 50
veintePesos = 20
diezPesos = 10
cincoPesos = 5
dosPesos = 2
unPeso = 1

#Le pido al usuario que ingrese el valor de la extracción
monto = int(input("Por favor ingrese el monto que desea retirar "))

#Realizo operaciones según los restos
#MIL PESOS
cocienteMil = monto // milPesos
restoMil = monto % milPesos
#QUINIENTOS PESOS
cocienteQuinientos = restoMil // quinientosPesos
restoQuinientos = restoMil % quinientosPesos
#DOSCIENTOS PESOS
cocienteDoscientos = restoQuinientos // doscientosPesos
restoDoscientos = restoQuinientos % doscientosPesos
#CIEN PESOS
cocienteCien = restoDoscientos // cienPesos
restoCien = restoDoscientos % cienPesos
#CINCUENTA PESOS
cocienteCincuenta = restoCien // cincuentaPesos
restoCincuenta = restoCien % cincuentaPesos
#VEINTE PESOS
cocienteVeinte = restoCincuenta // veintePesos
restoVeinte = restoCincuenta % veintePesos
#DIEZ PESOS
cocienteDiez = restoVeinte // diezPesos
restoDiez = restoVeinte % diezPesos
#CINCO PESOS
cocienteCinco = restoDiez // cincoPesos
restoCinco = restoDiez % cincoPesos
#DOS PESOS
cocienteDos = restoCinco // dosPesos
restoDos = restoCinco % dosPesos
#UN PESO
cocienteUn = restoDos // unPeso
restoUn = restoDos % unPeso

#Imprimo un mensaje en pantalla
print("\n******************************\n*  Usted recibirá:\n*", cocienteMil," billete(s) de $ 1000   \n*", cocienteQuinientos," billete(s) de $ 500   \n*", cocienteDoscientos," billete(s) de $ 200   \n*", cocienteCien," billete(s) de $ 100   \n*", cocienteCincuenta," billete(s) de $ 50   \n*", cocienteVeinte," billete(s) de $20  \n*",cocienteDiez," billete(s) de $10   \n*", cocienteCinco," billete(s) de $5  \n*",cocienteDos," moneda(s) de $2  \n*",cocienteUn," moneda(s) de $1  \n*****************************")
