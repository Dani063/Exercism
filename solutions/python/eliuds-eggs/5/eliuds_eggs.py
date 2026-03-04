"Funcion que reccibiendo un numero base 10 que hace referencia a un numero binario cuenta el numero de bits positivos (huevos) que hay"

def egg_count(display_value):
    "Funcion que reccibiendo un numero base 10 que hace referencia a un numero binario cuenta el numero de bits positivos (huevos) que hay"
    exp=50
    res = 0
    while display_value != 0:
        if (display_value - (2**exp)) >= 0:
            display_value -= 2**exp
            res += 1
        else: 
            exp -= 1
    return res
