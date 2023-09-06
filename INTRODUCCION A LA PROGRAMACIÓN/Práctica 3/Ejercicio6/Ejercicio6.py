#A)Hacer un programa que muestre, mediante un ciclo, los números desde el 15 hasta el 6 pero salteando de a tres (15, 12, 9, 6).

#WHILE
i = 15
while i >= 6:
    print(i)
    i = i - 3

#FOR
for i in range(15,6-1,-3):
    print(i)