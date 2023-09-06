#a) Hacer un programa que permita al usuario elegir un número positivo n y luego muestre en pantalla las n primeras sumas parciales de la sucesión an = 2n. Es decir, 2 6 12 20...
n = 0
while n <= 0:
    n = int(input("Por favor ingrese un numero positivo"))
suma = 0
for i in range(1,n+1,1):
    an = 2 * i
    suma = suma + an
    print(suma)

#b) Idem anterior para la sucesión an = 2n − 1.
n = 0
while n <= 0:
    n = int(input("Por favor ingrese un numero positivo"))
suma = 0
for i in range(1,n+1,1):
    an = 2 * i - 1
    suma = suma + an
    print(suma)

#c) Idem anterior para la sucesión an = n2
n = 0
while n <= 0:
    n = int(input("Por favor ingrese un numero positivo"))
suma = 0
for i in range(1,n+1,1):
    an = 2 ** i
    suma = suma + an
    print(suma)

#d) Idem anterior para la sucesión an = n3 − n2.
n = 0
while n <= 0:
    n = int(input("Por favor ingrese un numero positivo"))
suma = 0
for i in range(1,n+1,1):
    an = i**3 - i**2
    suma = suma + an
    print(suma)

#e) Idem anterior para la sucesión an = 1 / n2 .
n = 0
while n <= 0:
    n = int(input("Por favor ingrese un numero positivo"))
suma = 0
for i in range(1,n+1,1):
    an = 1 / i**2
    suma = suma + an
    print(suma)