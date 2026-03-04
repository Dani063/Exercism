def egg_count(display_value):
    x=50
    res = 0
    while display_value != 0:
        if (display_value - (2**x)) >= 0:
            display_value -= 2**x
            res += 1
        else: 
            x -= 1
    return res
