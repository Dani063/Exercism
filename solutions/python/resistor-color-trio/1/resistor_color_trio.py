def label(colors):
    color_values = {
        "black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4,
        "green": 5, "blue": 6, "violet": 7, "grey": 8, "white": 9
    }
    prefixes = {
        0: " ohms",
        3: " kiloohms",
        6: " megaohms",
        9: " gigaohms"
    }
    base = int(str(color_values[colors[0]]) + str(color_values[colors[1]]))
    
    multiplier = 10 ** color_values[colors[2]]
    resistance = base * multiplier

    exp = 0
    while resistance % 1000 == 0 and exp < 9 and resistance != 0:
        resistance //= 1000
        exp += 3

    return f"{resistance}{prefixes[exp]}"
