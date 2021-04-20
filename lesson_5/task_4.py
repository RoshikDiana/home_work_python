# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу,
# открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
second_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
first_list = []
with open('file_task_4', 'r') as file_obj:
    for i in file_obj:
        i = i.split(' ', 1)
        first_list.append(second_dict[i[0]] + '  ' + i[1])
        print(first_list)
        with open("new_file_task_4", "w") as new_file:
            new_file.writelines(first_list)
