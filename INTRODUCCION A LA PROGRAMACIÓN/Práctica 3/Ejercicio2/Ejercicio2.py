#A) Hacer un programa que muestre, mediante un ciclo, los números desde el 4 hasta el 7 (4, 5, 6 y 7).

#WHILE
i = 4

while i <= 7:
    print(i)
    i = i + 1

#FOR
for i in range(4,8,1):
    print(i)

#B) Hacer un programa que permita al usuario elegir un número m y un n y luego muestre todos los naturales entre m y n (m, m + 1, m + 2, · · · , n − 1, n). ¿Qué pasa si n es menor que m?

#WHILE
m = int(input("Por favor ingrese un valor "))
n = int(input("Por favor ingrese un valor "))

if m == n:
    print("Por favor elija valores distinto")
else:
    if m > n:
        while(m>=n):
            print(m)
            m = m - 1
    else:
        while(n>=m):
            print(m)
            m = m + 1

#FOR
m = int(input("Por favor ingrese un valor "))
n = int(input("Por favor ingrese un valor "))

if m == n:
    print("Por favor elija valores distinto")
else:
    if(m > n):
        for i in range(m,n-1,-1):
            print(i)
    else:
        for i in range(m,n+1,1):
            print(i)
