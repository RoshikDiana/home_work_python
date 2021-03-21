# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
my_number = int(input("введите положительное число "))
biggest_number = 0

while my_number > 0:
    if my_number % 10 > biggest_number:
        biggest_number = my_number % 10
    my_number = my_number // 10  # делим без остатка, перезаписываем переменную пока не станет равна нулю.
print(biggest_number)
