#Le pido al usuario que ingrese una nota
nota = int(input("Por favor ingrese una nota "))

if(( nota < 0 ) or( nota > 10 )):
    print("Por favor ingrese un valor entre 0 y 10")
else:
    if( nota < 4):
        print("Debe recuperar")
    else:
        print("No debe recuperar")