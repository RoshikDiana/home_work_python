# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
from sys import argv

salary_calculation, output_in_hours, salary, promotion = argv
output_in_hours = float(output_in_hours)
salary = float(salary)
promotion = float(promotion)
if output_in_hours <= 8:
    print(f"Зарплата сотрудника составила {output_in_hours * salary: .2f} ")
elif output_in_hours > 8:
    print(f"Зарплата сотрудника с премией {output_in_hours * salary + promotion:.2f}")
