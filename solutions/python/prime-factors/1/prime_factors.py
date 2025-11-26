def factors(value):
    factores_primos = []
    divisor = 2
    while value != 1:
        if value % divisor == 0:
            value = value / divisor
            factores_primos.append(divisor)
            divisor = 2
        else: divisor += 1
    return factores_primos

print(factors(40))
