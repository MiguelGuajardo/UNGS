#A) Hacer un programa que muestre, mediante un ciclo, los primeros 5 números naturales (1, 2, 3, 4 y 5).

#WHILE
i = 1
while i <= 5:
    print(i)
    i = i + 1

#FOR
for i in range(1,6,1):
    print(i)

#B) Hacer un programa que permita al usuario elegir un número n y luego muestre los primeros n números naturales (1, 2, · · · , n).

#WHILE
n = int(input("Por favor ingrese un valor "))
i = 1
while i <= n:
    print(i)
    i = i + 1

#FOR
n = int(input("Por favor ingrese un valor "))
for i in range(1,n+1,1):
    print(i)