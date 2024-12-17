from person import Person

class Student(Person):
    def __init__(self,name , age , id ,educational_Level):
        super().__init__(name)
        super().__init__(age)
        super().__init__(id)
        self.educational_Level = educational_Level
        self.grades = []

    def add_grades(self,grade):
        self.grades.append(grade) if 20<= grade <=0 else    print("Invalid grade! The grade must be between 0 and 20.")

    def calculate_average(self):
        return sum(self.grades) / len(self.grades) if self.grades   else    "There is not any grades!!"