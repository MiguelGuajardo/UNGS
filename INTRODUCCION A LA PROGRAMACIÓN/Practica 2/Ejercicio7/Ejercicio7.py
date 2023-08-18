#Le pido al usuario que ingrese dos valores
num1 = float(input("Por favor ingrese el primer valor "))
num2 = float(input("Por favor ingrese el segundo valor "))

#Verifico que los valores estén entre 0 y 10
if((num1 < 0) or (num1 > 10) or ((num2 < 0) or (num2 > 10))):
    print("Por favor ingrese valores entre 0 y 10")
else:
    promedio = (num1 + num2) / 2
    if( promedio > 7 ):
        print("Aprobado")
    else:
        print("Desaprobado")