#A) Hacer un programa que muestre, mediante un ciclo, los 5 números naturales que le siguen al 10 (11, 12, · · · , 15).

#WHILE
i = 10
while i < 15:
    i = i + 1
    print(i)

#FOR
for i in range(11,16,1):
    print(i)

#B) Hacer un programa que permita al usuario elegir un número n y luego muestre los 5 números naturales que le siguen a n (n + 1, n + 2, · · · , n + 5).

#WHILE
n = int(input("Por favor ingrese un valor "))
i = n + 5
while n < i:
    n = n + 1
    print(n)

#FOR
n = int(input("Por favor ingrese un valor "))
for i in range(n+1,n+6,1):
    print(i)

#C) Hacer un programa que permita al usuario elegir un número n y un número c, y luego muestre los c números naturales que le siguen a n (n + 1, n + 2, · · · , n + c).
n = int(input("Por favor ingrese un valor"))
c = int(input("Por favor ingrese un valor"))
i = n + c
while n < i:
    n = n + 1
    print(n)

#FOR
n = int(input("Por favor ingrese un valor"))
c = int(input("Por favor ingrese un valor"))
if(n < c):
    for i in range(n+1,c+2,1):
        print(i)
else:
    print(n,"tiene que ser menor a",c)