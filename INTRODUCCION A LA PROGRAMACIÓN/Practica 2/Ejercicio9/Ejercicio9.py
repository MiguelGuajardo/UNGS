#Declaro los DNIs del listado
dni1 = 30612453
dni2 = 23763290
dni3 = 21448503
dni4 = 34582048
dni5 = 15364857

#Le pido al usuario que ingrese su dni para verificar que se encuentre en él
dni = int(input("Por favor ingrese su DNI "))

#Verifico que el DNI ingresado sea positivo y tenga como máximo 8 dígitos
if((dni < 0) or (dni > 99999999)):
    print("Por favor ingrese un DNI valido")
else:
    if((dni == dni1) or (dni == dni2) or (dni == dni3) or (dni == dni4) or (dni == dni5)):
        #Imprimo mensajes si se encuentra en el listado
        print("El dni ingresado se encuentra en el listado")
    else:
        #Imprimo mensajes si no se encuentra en el listado
        print("El dni",dni,"no se encuentra en el listado")
