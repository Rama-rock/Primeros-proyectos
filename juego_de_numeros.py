######## Necesito importar el codigo de RNG
import random, time

######## Variables
n_intentos = 0
numero = random.randint(1, 20)
def dialogo(decir):
    print(decir)
    time.sleep(2)

######## INICIO
dialogo("Estoy pensando en un número entre el 1 y el 20.")
dialogo("Tenés 6 intentos para adivinarlo...")
dialogo("desde ahora.")
print("")

######### Hay 6 intentos, empieza el juego.
for n_intentos in range(6):
    ## pregunta
    if n_intentos == 0:
        print("¿Cuál es?")
        intento = int(input(">>Es el...  "))
        print("")
    else:
        intento = int(input(">>Entonces es el..."))
        print("")
    
    ## correccion
    if intento == numero:
        print("¡Muy bien, lo adivinaste!")
        break
    elif intento > numero and n_intentos < 5:
        print("No, es un número menor al " + str(intento) + ".")
    elif intento < numero and n_intentos < 5:
        print("No, es un número mayor al " + str(intento) + ".")
        
######### Final
if intento == numero:
    print("Lo conseguiste en " + str(n_intentos) + " intentos.")
else:
    print("Perdiste. El número era " + str(numero) + ".")