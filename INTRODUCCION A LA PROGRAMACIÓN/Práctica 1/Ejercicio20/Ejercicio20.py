#Le pido al usuario que ingrese tres valores
x = int(input("Por favor ingrese el primer valor "))
y = int(input("Por favor ingrese el segundo valor "))
z = int(input("Por favor ingrese el tercer valor "))

#imprimo mensaje en pantalla
print("\n******************************\n* El valor de X es:",x,"\n* El valor de Y es:",y,"\n* El valor de Z es:",z,"\n*****************************")

#Realizo las operaciones
aux = x
x = y
y = z
z = aux

#imprimo mensaje en pantalla
print("\n******************************\n* El valor de X es:",x,"\n* El valor de Y es:",y,"\n* El valor de Z es:",z,"\n*****************************")