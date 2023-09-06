#A) Hacer un programa que muestre, mediante un ciclo, los números desde el 5 hasta el 11 salteando de a 2 elementos (5, 7, 9 y 11)

#WHILE
i = 5
while i <= 11:
    print(i)
    i = i + 2

#FOR
for i in range(5,12,2):
    print(i)

#B) Hacer un programa que permita al usuario elegir un número m y un n y luego muestre todos los naturales entre m y n, pero salteando de a 3. Por ejemplo, si el usuario ingresara un n igual a 2 y un m igual a 14, el programa deberá mostrar 2, 5, 8, 11, 14.

#WHILE
m = int(input("Por favor ingrese un valor"))
n = int(input("Por favor ingrese un valor"))
if(m == n):
    print("Por favor ingrese valores distintos")
else:
    if m > n:
        while n <= m:
            print(n)
            n = n + 3
    elif m < n:
        while m <= n:
            print(m)
            m = m + 3

#FOR
m = int(input("Por favor ingrese un valor"))
n = int(input("Por favor ingrese un valor"))
if(m == n):
    print("Por favor ingrese valores distintos")
else:
    if n > m:
        for i in range(m,n+1,3):
            print(i)

#C) Hacer un programa que permita al usuario elegir un número n, un m y un p y luego muestre todos los naturales entre m y n, pero salteando de a p números. Por ejemplo, si el usuario ingresara un n igual a 2 y un m igual a 14, y un p igual a 4, el programa deberá mostrar 2, 6, 10, 14.

#WHILE
m = int(input("Por favor ingrese un valor"))
n = int(input("Por favor ingrese un valor"))
p = int(input("Por favor ingrese un valor"))

if((m == n) or (m > n) or (p == 0) or (p < 0)):
    print("Por favor ingrese valores distintos")
else:
    if m > n:
        while n <= m:
            print(n)
            n = n + p
    elif m < n:
        while m <= n:
            print(m)
            m = m + p

#FOR
m = int(input("Por favor ingrese un valor"))
n = int(input("Por favor ingrese un valor"))
p = int(input("Por favor ingrese un valor"))

if((m == n) or (m > n) or (p == 0) or (p < 0)):
    print("Por favor ingrese valores distintos")
else:
    for i in range(m,n+1,p):
        print(i)