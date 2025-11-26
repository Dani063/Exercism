def is_paired(input_string):
    open = ['(','[','{']
    close = [')',']','}']
    lista = []
    # Comprueba orden correcto
    for ch in input_string:
        if ch in open:
            lista.append(ch)
        if ch in close:
            if lista and open.index(lista[-1]) == close.index(ch):
                lista.pop()
            else: return False
    
    # Comprueba cantidad exacta
    if lista == []:
        return True
    else: return False