


class Student: 
        
        number_students = 0
        grade_up = 1

        def __init__(self, first, last, grade):
                self.first = first
                self.last = last 
                self.grade = grade
                Student.number_students += 1
        
        def fullname(self):
                return self.first + " " + self.last
    
        def email(self):
                return self.first[0] + self.last.lower() + '@raleigcharterhs.org'
    
        def graduation(self):
                self.grade = int(self.grade + self.grade_up)
                return self.grade

        @classmethod
        def grad(cls, amount):
                cls.grade_up = amount

        @classmethod
        def from_string(cls, student_string):
                first, last, grade = student_string.split('_')
                return cls(first, last, grade)

        def __repr__(self):
                return "Student({}, {}, {})".format(self.first, self.last, self.grade)
        
        def __str__(self):
                return "{} {}, grade: {}". format(self.first, self.last, self.grade)

class Senior(Student):
        
        def __init__(self, first, last, grade, batch):
                super().__init__(first, last, grade)
                self.batch = batch



Saketh = Student("Saketh", "Kamuju", 10)
Sampath = Senior('Sampath', 'Petchetti', 13, 2020)
Ani = Student("Ani", "Nagaraj", 12)

new_student = Student.from_string("Ryan_Qu_10")

if __name__ == "__main__":
    print(Student.from_string("Saketh_Kamuju_11"))
    print(Ani)