# Создать программно файл в текстовом формате,
# записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.
with open("new_file", "w+") as f:
    while True:
        new_line = input("Введите данные ")
        if new_line == "": break
        f.write(new_line+"\n")
    f.seek(0)
    content = f.readlines()
    print(f"содержимое файла {content}")
