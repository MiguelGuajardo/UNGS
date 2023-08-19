#Le pido al usuario que ingrese dos valores
num1 = int(input("Por favor ingrese el primer valor "))
num2 = int(input("Por favor ingrese el segundo valor "))

if(num1 < num2):
    aux = num1
    num1 = num2
    num2 = aux
    print("El valor",num1,"es mayor a",num2)
else:
    print("El valor",num1,"es mayor a",num2)
