#Hacer un programa que permita al usuario elegir un número positivo n y luego muestre en pantalla el producto (es decir, la multiplicación) de los números entre 1 y n.
n = 0
while n <= 0:
    n = int(input("Por favor ingrese un numero positivo"))
for i in range(1+1,n,1):
    x = i * n
    print(x)