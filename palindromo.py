import copy

def esPalindromo(txt):
    ## Para evitar que Hola --> aloH
    txt = list( txt.lower() )
    ## Creamos una copia de la lista para invertirla
    txt_inverso = copy.copy(txt)
    txt_inverso.reverse()
    
    if txt_inverso == txt:
        return True
    else:
        return False
    
def otra_vez():
    while True:
        print("¿Querés probar con otra palabra? [Sí, No]")
        siNo = input(">> ")
        print("")
        respuestas_posibles = [ ["Sí", "sí", "si", "Si", "sI", "sÍ"],
                                ["No", "no", "nO"] ]
        
        if siNo in respuestas_posibles[1]:
            return False
        elif siNo in respuestas_posibles[0]:
            return True
        else:
            print("Por sí o por no... ", end="")

while True:
    ## Pedir la frase o palabra.
    print("Vamos a ver si tu oración o palabra es un palíndromo.")
    print("Ingresala acá:")
    tu_input = input(">> ")
    
    ## Verificar si es un palíndromo.
    if esPalindromo(tu_input):
        print("¡Es un palíndromo!")
    else:
        print("Nop, no es un palíndromo.")
    
    ## Preguntar si quiere poner otra palabra.
    print("")
    if not otra_vez():
        break