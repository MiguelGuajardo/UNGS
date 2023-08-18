#Le pido al usuario tres notas para promediar
num1 = int(input("Por favor ingrese la primer nota "))
num2 = int(input("Por favor ingrese la segunda nota "))
num3 = int(input("Por favor ingrese la tercer nota "))

#Verifico que las notas ingresada estén entre [0,10]
if((num1 < 0 or num1 > 10) or (num2 < 0 or num2 > 10) or (num3 < 0 or num3 > 10)):
    #Imprimo un mensajes si el valor no esta en este rango
    print("Por favor ingrese valores entre 0 y 10")
else:
    #Realizo las operaciones
    promedio = (num1 + num2 + num3) / 3
    #Imprimo un mensajes si el estudiante saco un promedio entre [0,4)
    if(promedio >= 0 and promedio < 4):
        print("\n******************************\n* Nota",round(promedio,1),",Reprobado ☹ \n*****************************")
    #Imprimo un mensajes si el estudiante saco un promedio entre [4,7)
    elif(promedio >= 4 and promedio < 7):
        print("\n******************************\n* Nota",round(promedio,1),",Debe rendir examen final 😑 \n*****************************")
    #Imprimo un mensajes si el estudiante saco un promedio entre [7,10]
    else:
        print("\n******************************\n* Nota",round(promedio,1),",Eximido 😀 \n*****************************")