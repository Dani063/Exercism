"Lista que reccibiendo un numero base 10 que hace referencia a un numero binario cuenta el numero de bits positivos (huevos) que hay"

def egg_count(display_value):
    Exp=50
    res = 0
    while display_value != 0:
        if (display_value - (2**Exp)) >= 0:
            display_value -= 2**Exp
            res += 1
        else: 
            Exp -= 1
    return res
