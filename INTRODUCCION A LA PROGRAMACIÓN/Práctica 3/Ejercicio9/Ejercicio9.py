#A) Hacer un programa que reciba un número n y muestre todas las potencias de 2 menores a n. Por ejemplo, si el usuario ingresa 20, el programa mostrará: 1 2 4 8 16. Ayuda: pensar primero si sería más práctico utilizar la sentencia while o for.

#WHILE
n = int(input('Por favor ingrese un valor'))
i = 0
x = 2**i

while x < n:
    print(x)
    i = i + 1
    x = 2**i

#FOR
n = int(input('Por favor ingrese un valor'))
for i in range(0,n,1):
    x=2**i
    if(x < n):
        print(x)

#B) Hacer un programa que reciba un número n (n > 0) y muestre las n primeras potencias de 2. Por ejemplo, si el usuario ingresa 6, el programa mostrará: 1 2 4 8 16 32.

#WHILE
n = int(input('Por favor ingrese un valor'))
if(n < 0 or n == 0):
    print("Por favor ingrese un valor positivo")
else:
    i = 0
    x = 2**i
    while i < n:
        print(x)
        i = i + 1
        x = 2**i

#FOR
n = int(input('Por favor ingrese un valor'))
if(n < 0 or n == 0):
    print("Por favor ingrese un valor positivo")
else:
    for i in range(0,n,1):
        x = 2**i
        print(x)

#C)Hacer un programa que reciba un número n (n > 0) y muestre las n primeras potencias de n. Por ejemplo, si el usuario ingresa 4, el programa mostrará: 1 4 27 256. Es decir, 1**1 2**2 3**3 4**4.

#WHILE
n = int(input('Por favor ingrese un valor'))
if(n < 0 or n == 0):
    print("Por favor ingrese un valor positivo")
else:
    i = 1
    potencia = i**i
    while i <= n:
        print(potencia)
        i = i + 1
        potencia = i**i

#FOR
n = int(input('Por favor ingrese un valor'))
if(n < 0 or n == 0):
    print("Por favor ingrese un valor positivo")
else:
    for i in range(1,n+1,1):
        potencia = i**i
        print(potencia)