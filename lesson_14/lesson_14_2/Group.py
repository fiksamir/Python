from main import UserException


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
    