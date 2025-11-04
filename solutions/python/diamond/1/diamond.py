abc = 'abcdefghijklmnopqrstuvwxyz'

def rows(letter):
    result = []
    aux = []
    idx = abc.index(letter.lower())
    for i in range(idx+1):
        if i == 0:
            texto = poner_espacios(idx-i) + abc[i].upper() + poner_espacios(idx-i)
        else:
            texto = poner_espacios(idx-i) + abc[i].upper() + poner_espacios(((i-1)*2)+1) + abc[i].upper() + poner_espacios(idx-i)
        result.append(texto)
    for i in range(len(result)):
        aux.append(result[len(result)-i-2])
    return result + aux[:-1]

def poner_espacios(num):
    espacios = ""
    for i in range(num):
        espacios += " "
    return espacios

print(rows('E'))