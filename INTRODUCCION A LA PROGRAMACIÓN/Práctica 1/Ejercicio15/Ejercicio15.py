#Declaro el sueldo base
sueldoBase = 42000
#Declaro el extra
extra = 0.1
#Pido al usuario que ingrese el valor de la primer venta
venta1 = float(input("Por favor ingrese el valor de la primer venta "))
#Pido al usuario que ingrese el valor de la segunda venta
venta2 = float(input("Por favor ingrese el valor de la segunda venta "))
#Pido al usuario que ingrese el valor de la tercer venta
venta3 = float(input("Por favor ingrese el valor de la tercer venta "))
#Realizo las operaciones
pagoExtra = (venta1 + venta2 +venta3) * extra
sueldo = sueldoBase + pagoExtra
#Imprimo un mensaje en pantalla
print("\n******************************\n*  Su sueldo es de: $", sueldo,"    \n******************************")