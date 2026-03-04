def suffix_elecction(n:int) -> str:
    if 11 <= n % 100 <= 13:
        return 'th'
    return {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')

def line_up(name, number):
    return f"{name}, you are the {number}{suffix_elecction(number)} customer we serve today. Thank you!"