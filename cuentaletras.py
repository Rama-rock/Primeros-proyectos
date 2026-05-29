contar = {} ## Lista principal, usada en todo el programa.
           ## Dice cuantas veces se uso cada letra
           ## (No aparece acá si no fue usada nunca.)
#-------------------------------------------------#
def contar_caracteres(mensaje):
    for caracter in mensaje:
        ## Hacer que las mayúsculas y minúsculas sean iguales
        caracter = caracter.upper()
        ## Poner la letra en la lista si es que todavía no estaba
        contar.setdefault(caracter, 0)
        ## La letra aparecio una vez más!!
        contar[caracter] = contar[caracter] + 1

#------------------------------------------------------------------------------#
def mostrar_data(form):
    lista = []
    
    ## Orden alfabetico
    if form == 1:
        ## Poner todas las letras en una lista así puedo ordenarlas
        ## con el metodo .sort
        for letra in contar.keys():
            lista += [letra]
        lista.sort()
        
        ## Ahora que estan ordenadas, mostrárselas al usuario
        for letra in lista:
            if letra == " ":
                print(f"--Hay { contar[letra] } ESPACIOS.")
            else:
                print(f"--La letra {letra} apareció { contar[letra] } veces.")
    
    ## Orden por frecuencia (del más recurrente al menos frecuente)        
    elif form == 2:
        ## Poner los números en una lista asi puedo ordenarlos de
        ## menor a mayor con el metodo .sort
        ## (esta lista no va a repetir ningún número)
        for num in contar.values():
            if num not in lista:
                lista += [num]
        lista.sort(reverse=True)
        
        ## Primero, buscar las parejas numero-letra que tengan la mayor
        ## reincidencia (el numero de apariciones más alto es el 1er
        ## valor de lista). Luego, ir bajando por la lista.
        for num in lista:
            for letra, frec in contar.items():
                if frec == num:
                    if letra == " ":
                        print(f"--Hay {frec} ESPACIOS.")
                    else:
                        print(f"--La letra {letra} apareció {frec} veces.")
    else:
        ## El diccionario contar ya esta ordenado por aparición :D
        for letra in contar.keys():
            if letra == " ":
                print(f"--Hay {contar[letra]} ESPACIOS.")
            else:
                print(f"--La letra {letra} apareció {contar[letra]} veces.")
#-----------------------------------------------------------------------------#
                
def pedir_forma():
    while True:
        print("Cómo querés que aparezca la información?")
        try:
            mostrar_como = int(input("1: Orden alfabético // 2: Orden por frecuencia" \
                                     " // 3. Orden por aparición   "))
        except KeyboardInterrupt:
            exit()
        except ValueError:
            print()
            print("Por favor ingresá un valor numérico (1, 2, 3)")
            continue
        else:
            if mostrar_como in [1, 2, 3]:
                return mostrar_como
            else:
                print()
                print("Ingresá un número entre el 1, el 2 o el 3.")
        
## CÓDIGO
print("Veamos cuántas veces aparece cada letra en tu mensaje...")
contar_caracteres( input("Escribilo acá: ") )

print("")
mostrar_data( pedir_forma() )
