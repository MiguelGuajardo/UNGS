import math
#El número 1/4π se puede aproximar de la siguiente manera:
# 1/4π = 1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + 1/13 - 1/15

#a) Escribir un programa que le pregunte al usuario la cantidad de términos a sumar y que muestre la aproximación de π con esa cantidad de términos.

n = 0
while(n <= 0):
    n = int(input("Por favor ingrese la cantidad de términos "))

suma = 0
for i in range(1,n+1):
    termino = 1/(2*i-1)
    signo = (-1)**(i+1)
    suma = suma + termino * signo
print("La aproximación del valor pi es: ",suma*4)


#b) ¿A partir de cuántos términos el valor alcanzado está a menos de 0.1 del valor que da la calculadora?

n = 0
while(n <= 0):
    n = float(input("Por favor ingrese la cantidad de términos "))

suma = 0
i = 1
while True:
    termino = 1/(2*i-1)
    signo = (-1)**(i+1)
    suma = suma + termino * signo
    if(termino * 4 < n):
        break
    i = i + 1
print("El valor de pi con un error de", n, ":", suma*4, "tras", i-1, "iteraciones")

#d) Modificar el programa para que en lugar de pedir la cantidad de términos a sumar, pida al usuario un número decimal ϵ (muy chico) y calcule la suma hasta que el error comparado con el valor de la calculadora sea menor que ϵ

