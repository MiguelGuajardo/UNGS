#Le pido al usuario que ingrese un valor en segundos
seg = int(input("Por favor ingrese un tiempo en segundos "))
#Realizo las operaciones para saber el cociente y el resto en días,horas,minutos
dia = seg // 86400
restoDia = seg % 86400
hora = restoDia // 3600
restoHora = restoDia % 3600
min = restoHora // 60
restoMin = restoHora % 60
#Imprimo un mensaje en pantalla
print("\n******************************\n*", dia,"día(s) \n*", hora,"hora(s) \n*",min,"minuto(s) \n*",restoMin,"segundo(s) \n******************************")
