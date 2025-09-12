def append(list1, list2):
    result = []
    for x in list1:
        result += [x]
    for y in list2:
        result += [y]
    return result

def concat(lists):
    result = []
    for sublist in lists:
        for item in sublist:
            result += [item]
    return result

def filter(function, list):
    result = []
    for item in list:
        if function(item):
            result += [item]
    return result

def length(list):
    cont = 0
    for _ in list:
        cont += 1
    return cont

def map(function, list):
    result = []
    for x in list:
        result += [function(x)]
    return result

def foldl(function, list, initial):
    for x in list:
        initial = function(initial,x)
    return initial

def foldr(function, xs, acc):
    for x in reverse(xs):   
        acc = function(acc, x)
    return acc

def reverse(list):
    result = []
    for i in range(length(list) - 1, -1, -1):
        result += [list[i]]
    return result