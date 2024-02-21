# Завдання 1 Група студентів

# 1) Створіть клас, що описує людину (створіть метод, що виводить інформацію про людину).

# 2) На його основі створіть клас Студент (перевизначте метод виведення інформації).

# 3) Створіть клас Група, екземпляр якого складається з об'єктів класу Студент. Реалізуйте методи додавання, видалення студента та метод пошуку студента на прізвище.

# Метод пошуку студента повинен повертати саме екземпляр класу Студент, якщо студент є у групі, інакше - None.

# У методі видалення, використовуйте результат методу пошуку. Тобто. потрібно скомбінувати ці два методи;)

# Визначте для групи метод __str__() для повернення списку студентів у вигляді рядка.

# Нижче наведені заготовки, які необхідно доповнити.
############
class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.gender}, {self.age} years old)\n"


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        self.record_book = record_book
        super().__init__(gender, age, first_name, last_name)

    def __str__(self):
        resp = super().__str__()
        return f"Student {self.record_book}: " + resp


class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        self.group.add(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student is not None:
            self.group.remove(student)
            

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = ''
        for student in self.group:
            all_students += str(student)
        
        return f'Number:{self.number}\n{all_students} '


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st3 = Student('Male', 31, 'Michael', 'Jacson', 'AN143')
st4 = Student('Female', 26, 'Marilyn', 'Monroe', 'AN144')

gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
gr2 = Group('PD2')
gr2.add_student(st3)
gr2.add_student(st4)
print(gr)
print(gr2)
assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод пошуку має повертати екземпляр'

gr.delete_student('Taylor')
gr2.delete_student('Jacson')
print(gr)  # Only one student
print(gr2)  # Only one student

gr.delete_student('Taylor')  # No error!