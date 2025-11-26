
abc = 'abcdefghijklmnopqrstuvwxyz'
cipher = 'zyxwvutsrqponmlkjihgfedcba'
def encode(plain_text):
    result = ''
    cont = 0
    for char in plain_text:
        if cont == 5:
            result += ' '
            cont = 0
        if char.lower() in abc:
            result += cipher[abc.index(char.lower())]
            cont += 1
        elif char not in [' ',',','.']: 
            result += char        
            cont += 1
    if result[-1] == ' ':
        return result[:-1]
    return result

def decode(ciphered_text):
    result = ''
    for char in ciphered_text:
        if char.lower() in abc:
            result += abc[cipher.index(char.lower())]
        elif char != ' ': result += char
    return result