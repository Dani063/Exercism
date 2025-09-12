def square_of_sum(number):
    sol = 0
    for index in range(1,number+1):
        sol += index
    return sol ** 2


def sum_of_squares(number):
    sol = 0
    for index in range(1,number+1):
        sol += index ** 2
    return sol


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
