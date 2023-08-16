#Le pido al usuario un valor en segundos
seg = int(input("Ingrese una cantidad en segundos "))
#Declaro minutos horas y días
min = seg/60
hora = min/60
dia = hora/24
#Imprimo un mensaje en pantalla
print("\n******************************\n*  Usted ingreso:", seg,"segundos    \n* Minutos:" , min ,"\n* Horas:", hora,"\n* Dias:", dia,"\n*****************************")
