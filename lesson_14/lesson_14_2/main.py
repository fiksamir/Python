# Завдання 2 Створення власних модулів

# У цьому завданні Вам необхідно зробити дві речі на підставі попереднього ДЗ.

# До класу Студента необхідно додати метод порівняння. Порівнювати можна за тими рядками, які повертає метод __str__ Для того, щоб спрацювала коректно ось ця перевірка
# assert gr.find_student('Jobs') == st1
# Рознесіть класи, які використовували під час виконання завдання про групу студентів за модулями.
# Переконайтеся у працездатності проекту – створіть окремо файл main.py, у якому необхідно імпортувати потрібні класи та запустити код перевірки.

#######

from Student import Student
from Group import Group


class UserException(Exception):

    def __init__(self, message, x):
        super().__init__()
        self.message = message
        self.x = x

    def get_exception_message(self):
        return self.message
    

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add_student(st1)

try:
    gr.add_student(st2)
except UserException as err:
    print(err.get_exception_message())
    print(err.x)

print(gr)
assert gr.find_student('Jobs') == st1 #'Steve Jobs'
assert gr.find_student('Jobs2') is None

gr.delete_student('Taylor')
print(gr) # Only one student