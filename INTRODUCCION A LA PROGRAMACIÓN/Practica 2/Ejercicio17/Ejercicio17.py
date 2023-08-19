print("Este programa fue diseñado para resolver ecuaciones de primer grado => ax + b = 0")
#Le pido al usuario los coeficientes para una ecuación de primer grado
a = float(input("Por favor ingrese el primer valor "))
b = float(input("Por favor ingrese el segundo valor "))

if((a == 0) and (b != 0)):
    #Conjunto vació : Ø => Alt + 157
    print("No tiene tiene soluciones -- X = Ø")
else:
    if((a == 0) and (b == 0)):
        print("Las solución son todos los números Reales-- X = R ")
    elif((a != 0) and (b == 0)):
        print("La solución es X = 0")
    else:
        x = -b / a
        print("La solución es X =", x)