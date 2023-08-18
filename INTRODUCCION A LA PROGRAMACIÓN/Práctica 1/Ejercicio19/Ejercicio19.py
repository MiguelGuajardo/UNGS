#Le pido al usuario que ingrese dos valores
x = int(input("Por favor ingrese un valor para X "))
y = int(input("Por favor ingrese un valor para Y "))

#Imprimo un mensaje en pantalla
print("\n******************************\n* El valor de X es:",x,"\n* El valor de Y es:",y,"\n******************************")
aux = x
x = y
y = aux
#Imprimo un mensaje en pantalla
print("\n******************************\n* El nuevo valor de X es:",x,"\n* El nuevo valor de Y es:",y,"\n******************************")