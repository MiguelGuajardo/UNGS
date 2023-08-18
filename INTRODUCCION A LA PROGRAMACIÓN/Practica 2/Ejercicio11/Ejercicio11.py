#Le pido al usuario tres valores
num1 = int(input("Por favor ingrese el primer valor "))
num2 = int(input("Por favor ingrese el segundo valor "))
num3 = int(input("Por favor ingrese el tercer valor "))

#if((num1 > num2) and (num1 > num3)):
#    print("El valor",num1,"es mayor que ",num2,"y",num3)
#elif((num2 > num1) and (num2 > num3)):
#    print("El valor",num2,"es mayor que ",num1,"y",num3)
#elif((num3 > num1) and (num3 > num2)):
#    print("El valor",num3,"es mayor que ",num1,"y",num2)
#else:
#    print("Alguno de los valores son iguales")

if(num2 < num1 > num3):
    print("El valor",num1,"es mayor que ",num2,"y",num3)
elif(num1 < num2 > num3):
    print("El valor",num2,"es mayor que ",num1,"y",num3)
elif(num1 < num3 > num2):
    print("El valor",num3,"es mayor que ",num1,"y",num2)
else:
    print("Por favor ingrese nuevos valores ya que algunos son iguales")
