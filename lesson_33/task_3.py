# Реализовать функцию my_func(),
# которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.


def my_func(var_1, var_2, var_3):
    a = [var_1, var_2, var_3]
    a.remove(min(var_1, var_2, var_3))
    return sum(a)


print(my_func(4, 5, 8))
