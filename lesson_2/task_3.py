# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.
season = ["winter", "spring", "summer", "autumn"]  # решение через list
month = int(input("введите номер месяца"))
if month == 12 or month == 1 or month == 2:
    print(season[0])
elif month == 3 or month == 4 or month == 5:
    print(season[1])
elif month == 6 or month == 7 or month == 8:
    print(season[2])
elif month == 9 or month == 10 or month == 11:
    print(season[3])

season_dict = {"winter": (12, 1, 2), "spring": (3, 4, 5), "summer": (6, 7, 8),
               "autumn": (9, 10, 11)}
for key in season_dict.keys():
    if month in season_dict[key]:
        print(key)