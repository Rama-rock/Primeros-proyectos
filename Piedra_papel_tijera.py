####### Importar
import random

######### Variables y listas
opc_pc = ["piedra", "papel", "tijera"]
eleccion_pc = ""

victorias = 0
empates = 0
derrotas = 0

######## INICIO
print("¿Estás listo para jugar al Piedra, Papel o Tijera?")
print("El que llegue a TRES, gana.")
print("Empecemos.")
print("")

########################## BUCLE DE JUEGO
while True:
    ##### Si ya se llego a las 3 victorias, parar
    if victorias == 3 or derrotas == 3:
        break

    ##### La PC elige
    eleccion_pc = opc_pc[random.randint(0, 2)]
    
    ###### El jugador elige
    print("-----------------------------------")
    print("(Elegís: ¿piedra, papel o tijera?)")
    eleccion_jug = input("[Recordá poner la palabra en minúscula]: ")
    
    print("")
    
    ##### Relatar
    print("Elegiste " + eleccion_jug + ". La PC eligió " + eleccion_pc + ".")
    
    ##### Analizar resultado
    opcion_ganadora = opc_pc[(opc_pc.index(eleccion_pc) + 1)]
    opcion_perdedora = opc_pc[(opc_pc.index(eleccion_pc) - 1)]
    
    if eleccion_jug == eleccion_pc: ###EMPATE
        empates += 1 
        print("EMPATE.")
        print("Estadísticas: " + str(victorias) + " VICT, " + str(empates) + " EMP y " + str(derrotas) + " DERR")
        print("")
    
    elif eleccion_jug == opcion_ganadora: ###VICTORIA
        victorias += 1
        print("GANASTE.")
        print("Estadísticas: " + str(victorias) + " VICT, " + str(empates) + " EMP y " + str(derrotas) + " DERR")
        print("")
        
    elif eleccion_jug == opcion_perdedora: ###DERROTA
        derrotas += 1
        print("PERDISTE.")
        print("Estadísticas: " + str(victorias) + " VICT, " + str(empates) + " EMP y " + str(derrotas) + " DERR")
        print("")

    else:
        print("...¿Qué? ¿Escribiste bien eso?")
        print("Procurá poner las palabras en minúscula, tal como se presentan.")
        print("")

#################### FIN DEL JUEGO
print("----------------------------")
if victorias == 3:
    print("Conseguiste tus tres victorias. ¡Ganaste!")
else:
    print("La PC consiguió tres victorias. ¡Perdiste!")
    
    