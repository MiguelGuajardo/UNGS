#Declaro el costo de la comunicación
costoCom = 12
#Declaro el costo por segundo
costoSeg = 1.5
#Le pido al usuario que ingrese el total de llamadas realizadas
llamadas = int(input("Por favor ingrese el total de llamadas realizadas "))
#Le pido al usuario que ingrese el total de segundos utilizados
tiempo = int(input("Por favor ingrese el total de segundos utilizados "))
#Realizo las operaciones
impLlamada = llamadas * costoCom
impTiempo = tiempo * costoSeg
importe = impLlamada + impTiempo
#Imprimo un mensaje en pantalla
print("\n******************************\n*  El importe total es:", importe,"    \n******************************")