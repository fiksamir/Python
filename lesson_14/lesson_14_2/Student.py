from Human import Human

class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        self.record_book = record_book
        super().__init__(gender, age, first_name, last_name)

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.__str__() == other.__str__()
        return NotImplemented
    
    def __hash__(self):
        return hash(str(self))

    def __str__(self):
        resp = super().__str__()
        return f"Student {self.record_book}: " + resp
