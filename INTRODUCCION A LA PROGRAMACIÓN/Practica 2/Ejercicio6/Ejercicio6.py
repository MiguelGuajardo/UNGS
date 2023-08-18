#Le pido al usuario que ingrese dos valores
num1 = int(input("Por favor ingrese el primer valor "))
num2 = int(input("Por favor ingrese el segundo valor "))

#Verifico que los valores no sean iguales
if(num1 == num2):
    print("Por favor no ingrese valores iguales")
else:
    #Verifico si el primer valor es mayor que el segundo
    if (num1 > num2):
        print(num1,"es mayor a",num2)
    else:
        print(num1,"es menor a",num2)