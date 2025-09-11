def commands(binary_str):
    actions = ['wink', 'double blink', 'close your eyes', 'jump']
    string = []
    for index, number in enumerate(reversed(binary_str)):
        if number == '1' and index < 4:
            string.append(actions[index])
    if binary_str[0] == '1':
        string.reverse()
    return string