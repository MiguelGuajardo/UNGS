#Le pido al usuario que ingrese dos valores
num1 = int(input("Por favor ingrese el primer valor "))
num2 = int(input("Por favor ingrese el segundo valor "))

if(num1 > num2):
    print("El primer valor ingresado fue",num1,",",num1,"es mayor a",num2)
else:
    print("El segundo valor ingresado fue",num2,",",num2,"es mayor a",num1)