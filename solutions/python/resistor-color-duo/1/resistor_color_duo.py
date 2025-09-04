def value(colors):
    color_values =  {"black":"0","brown":"1","red":"2","orange":"3","yellow":"4","green":"5","blue":"6","violet":"7","grey":"8","white":"9"}
    sol = ""
    colors = colors[:2]
    for col in colors:
        for aux in color_values:
            if col == aux:
                sol += color_values[col]
    return int(sol)