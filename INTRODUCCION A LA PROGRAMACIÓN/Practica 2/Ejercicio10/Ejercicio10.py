#Declaro valores fijos
tarifaFija = 480
kw = 25.5
impuestos = 78
#Le pido al usuario el consumo inicial y el consumo final
consumoInicial = int(input("Por favor ingrese el kw inicial del medidor "))
consumoFinal = int(input("Por favor ingrese el kw final del medidor "))
consumo = consumoFinal - consumoInicial
if(consumo <= 0):
    print("Por favor ingrese valores positivos")
else:
    if(consumo <= 200):
        print("Su consumo es de",consumo)
        totalFactura = tarifaFija + impuestos
        print("Como usted no se excedió en el consumo eléctrico usted debe abonar",totalFactura,"pesos")
    else:
        print("Su consumo es de",consumo)
        excedente = (consumo - 200) * kw
        totalFactura = tarifaFija + excedente + impuestos
        print("Debido a un excedente en el consumo eléctrico usted debe abonar",totalFactura,"pesos")