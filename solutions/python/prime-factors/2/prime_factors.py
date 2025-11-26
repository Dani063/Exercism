def factors(value): #Intento optimo
    factores_primos = []
    #Primero quitamos la posibilidad de pares, esto despues de este primer paso reduce a la mitad el numero de comprobaciones
    while value % 2 == 0:
        factores_primos.append(2)
        value //= 2

    # Ahora solo puede ser divisible por algun numero impar
    divisor = 3
    while divisor * divisor <= value: 
        while value % divisor == 0:
            factores_primos.append(divisor)
            value //= divisor
        divisor += 2 
        print(divisor)

    #Para incluir el ultimo numero
    if value > 1:
        factores_primos.append(value)

    return factores_primos

print(factors(93819012551))
