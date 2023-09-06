from math import log
#El logaritmo natural de 2 (ln(2)) se puede aproximar de la siguiente manera:
#ln(2) = 1 − 1/2 + 1/3 - 1/4 + 1/5 ...

#a) Escribir un programa que le pregunte al usuario la cantidad de términos a sumar y que muestre la aproximación de ln(2) con esa cantidad de términos.

n = 0
while(n <= 0):
    n = int(input("Por favor ingrese la cantidad de términos "))

ln2 = 0
for i in range(1,n+1,1):
    if(i % 2 == 0):
        ln2 = ln2 - 1/i
    else:
        ln2 = ln2 + 1/i

print(ln2)

#b) ¿A partir de cuántos términos el valor alcanzado está a menos de 0.1 del valor que da la calculadora? En python se puede aproximar este valor usando math.log(2)

ln = log(2)
print(ln)

if(ln2 == ln ):
    print(True)