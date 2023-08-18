#Le pido al usuario que ingrese su edad y distancia del centro votación
edad = int(input("Por favor ingrese su edad "))
distancia = int(input("Por favor a que distancia (en km) se encuentra del centro de votación "))

if((edad < 18) or (edad > 70) or (distancia > 500)):
    #Imprimo mensaje si el usuario es menor a 17 años o mayor a 70 años
    print("Usted esta exento de votar")
else:
    print("Usted posee todas las condiciones necesarias para votar")