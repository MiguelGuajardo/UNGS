#SUPER INDICE ² => ALT + 253
print("Este programa fue diseñado para detectar cuantas raíces posee las ecuaciones de segundo grado => ax² + bx + c = 0")

#Le pido al usuario los coeficientes para una ecuación de segundo grado
a = float(input("Por favor ingrese el primer coeficiente "))
b = float(input("Por favor ingrese el segundo coeficiente "))
c = float(input("Por favor ingrese el tercer coeficiente "))
#Verifico que el coeficiente A no sea 0 
if(a == 0):
    print("El coeficiente A no puede ser 0 porque sino se trataría de una ecuación de primer grado")
else:
    #Evalúo el discriminante para saber cuantas raíces tiene
    discriminante = (((b)**2) - (4 * a * c))
    if(discriminante < 0):
        print("La ecuación no posee raíces reales")
    else:
        x1 = ((-b) + discriminante ** 0.5) / (2 * a)
        x2 = ((-b) - discriminante ** 0.5) / (2 * a)
        if(discriminante > 0):
            print("La ecuación posee dos raíces")
            print("X1 =",x1)
            print("X2 =",x2)
        else:
            print("La ecuación posee una raíz doble")
            print("X1 =",x1)
            print("X2 =",x2)