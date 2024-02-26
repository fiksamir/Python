# Завдання 1 Виняток користувача

# Модифікуйте клас Група (завдання минулої лекції) так, щоб при спробі додавання до групи більше 10-ти студентів, було порушено виняток користувача. 

# Таким чином потрібно створити ще й виняток користувача для цієї ситуації. І обробити його поза межами класу. Тобто. потрібно перехопити цей виняток, при спробі додавання 11-го студента
###########

class UserException(Exception):

    def __init__(self, message, x):
        super().__init__()
        self.message = message
        self.x = x

    def get_exception_message(self):
        return self.message


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

    max_student = 10

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= self.max_student:
            raise UserException(f"Error add_student(): Досягнуто максимуму! max_student = ", self.max_student)
        else:
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


st_list = [
    Student('Male', 30, 'Steve', 'Jobs', 'AN142'),
    Student('Female', 25, 'Liza', 'Taylor', 'AN145'),
    Student('Male', 31, 'Michael', 'Jacson', 'AN143'),
    Student('Female', 26, 'Marilyn', 'Monroe', 'AN144'),
    Student('Male', 27, 'Bob', 'Marley', 'AN145'),
    Student('Male', 24, 'Elthon', 'John', 'AN146'),
    Student('Male', 30, 'Rob', 'Dilan', 'AN147'),
    Student('Female', 28, 'Mariia', 'Kuri', 'AN148'),
    Student('Male', 29, 'Nikolay', 'Tesla', 'AN149'),
    Student('Female', 21, 'Emma', 'Whatson', 'AN150'),
    Student('Male', 19, 'Roi', 'Kent', 'AN151'),
]

gr = Group('PD1')
for st in st_list:
    try:
        gr.add_student(st)
    except UserException as err:
        print(err.get_exception_message())
        print(err.x)
