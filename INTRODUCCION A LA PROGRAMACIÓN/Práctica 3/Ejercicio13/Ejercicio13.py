#a) Hacer un programa que permita al usuario elegir un número positivo n y luego muestre en pantalla los n primeros términos de la sucesión an = 2n. Es decir 2, 4, 6...
n = 0
while n <= 0:
    n = int(input("Por favor ingrese un numero positivo"))
for i in range(1,n+1,1):
    an=2*i
    print(an)

#b) Idem anterior para la sucesión an = 2n − 1.
n = 0
while n <= 0:
    n = int(input("Por favor ingrese un numero positivo"))
for i in range(1,n+1,1):
    an = 2 * i - 1
    print(an)

#c) Idem anterior para la sucesión an = n2
n = 0
while n <= 0:
    n = int(input("Por favor ingrese un numero positivo"))
for i in range(1,n+1,1):
    an = 2 ** i
    print(an)

#d) Idem anterior para la sucesión an = n3 − n2.
n = 0
while n <= 0:
    n = int(input("Por favor ingrese un numero positivo"))
for i in range(1,n+1,1):
    an = i**3 - i**2
    print(an)

#e) Idem anterior para la sucesión an = 1 / n2 .
n = 0
while n <= 0:
    n = int(input("Por favor ingrese un numero positivo"))
for i in range(1,n+1,1):
    an = 1 / i**2
    print(an)