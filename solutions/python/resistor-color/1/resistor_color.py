def color_code(color):
    color_list = colors()
    for index, col in enumerate(color_list):
        if col == color:
            return index

def colors():
    return ["black",
            "brown",
            "red",
            "orange",
            "yellow",
            "green",
            "blue",
            "violet",
            "grey",
            "white"]
