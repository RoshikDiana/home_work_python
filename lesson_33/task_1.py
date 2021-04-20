# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль
def my_function():
    try:
        first_number = int(input("введите первое число "))
        second_number = int(input("введите второе число "))
        result = first_number / second_number
    except ZeroDivisionError:
        return "Attention! you can't do division by zero"
    result = first_number / second_number
    return result


print(my_function())