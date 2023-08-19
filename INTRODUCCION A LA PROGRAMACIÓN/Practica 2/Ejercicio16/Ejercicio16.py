#Le pido al usuario un año para verificar si es bisiesto
year = int(input("Por favor ingrese un año"))

if ( (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0))):
    print("El año",year,"es bisiesto")
else:
    print("El año",year,"no es bisiesto")

