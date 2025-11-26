def square_root(number):
    for num in range (0,number+1):
        if num ** 2 == number:
            return num
    raise ValueError("No tiene raiz exacta")
