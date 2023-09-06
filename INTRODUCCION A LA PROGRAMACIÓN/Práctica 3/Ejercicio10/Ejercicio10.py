#a) Hacer un programa que permita al usuario elegir un número positivo n y luego muestre en pantalla todos los divisores de n.
n = 0
while n <= 0:
    n = int(input("Por favor ingrese un numero positivo"))
i=1
while i <= n:
    divisor = n % i
    if(divisor == 0):
        print(i)
    i = i + 1

#b) Hacer un programa que permita al usuario elegir un número positivo n y luego muestre en pantalla todos los divisores pares de n.
n = 0
while n <= 0:
    n = int(input("Por favor ingrese un numero positivo"))
i=1
while i <= n:
    divisor = n % i
    if(divisor == 0):
        par = i % 2
        if(par == 0):
            print(i)
    i = i + 1

#c) Hacer un programa que permita al usuario elegir un número positivo n y luego muestre en pantalla la cantidad de divisores de n.
n = 0
while n <= 0:
    n = int(input("Por favor ingrese un numero positivo"))
i=1
cantidad = 0
while i <= n:
    divisor = n % i
    if(divisor == 0):
        cantidad = cantidad + 1
    i = i + 1
print(cantidad)

#d) Hacer un programa que permita al usuario elegir un número positivo n y luego muestre en pantalla la suma de los divisores de n.
n = 0
while n <= 0:
    n = int(input("Por favor ingrese un numero positivo"))
i=1
suma = 0
while i <= n:
    divisor = n % i
    if(divisor == 0):
        suma = suma + i
    i = i + 1
print(suma)

#e) Hacer un programa que permita al usuario elegir dos números positivos c y n y luego muestre en pantalla los primeros c divisores de n.
n = 0
while c <= 0:
    c = int(input("Por favor ingrese un numero positivo"))
while n <= 0:
    n = int(input("Por favor ingrese un numero positivo"))
i=1
while i <= n:
    divisor = n % i
    if(divisor == 0):
        suma = suma + i
    i = i + 1
print(suma)