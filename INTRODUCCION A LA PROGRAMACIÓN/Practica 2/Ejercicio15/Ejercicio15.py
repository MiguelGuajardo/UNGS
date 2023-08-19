#Le pido al usuario tres valores enteros
a = int(input("Por favor ingrese el primer valor "))
b = int(input("Por favor ingrese el segundo valor "))
c = int(input("Por favor ingrese el tercer valor "))

if((a == b) or (a == c) or (b == c)):
    print("Los valores ingresados no pueden ser iguales")
else:
    if((a < b) and (b < c)):
        print(a,"-",b,"-",c)
    elif((b < a) and (a < c)):
        aux = b
        b = a
        a = aux
        print(a,"-",b,"-",c)
    elif((c < a) and (a < b)):
        aux = a
        a = c
        c = b
        b = aux
        print(a,"-",b,"-",c)
    elif((c < b) and (b < a)):
        aux = a
        a = c
        c = aux
        print(a,"-",b,"-",c)
    elif((a < c) and (c < b)):
        aux = b
        b = c
        c = aux
        print(a,"-",b,"-",c)
    elif((b < c) and (c < a)):
        aux = a
        a = b
        b = c
        c = aux
        print(a,"-",b,"-",c)

