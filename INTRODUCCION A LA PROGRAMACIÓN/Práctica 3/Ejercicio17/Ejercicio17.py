import math
#Escribir un programa que solicite al usuario un número positivo y aproxime el valor del número e de la siguiente manera: (ejemplo para 7 términos)
#7 términos: 1/0! + 1/1! + 1/2! + 1/3! + 1/4! + 1/5! + 1/6!

n = 0
while n <= 0:
    n = int(input("Por favor ingrese un numero"))

suma = 0
for i in range(0,n):
    suma = suma + 1/ math.factorial(i)

print(suma)