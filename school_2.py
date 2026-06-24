class Student:
    def __init__(self, student_name, student_cls, student_id):
        self.student_name = student_name
        self.student_cls = student_cls
        self.student_id = student_id
    
    def __repr__(self) -> str:
        return f'Student with Name: {self.student_name}. Her Class: {self.student_cls}. Her Id: {self.student_id}'

class Teacher:
    def __init__(self, teacher_name, subject, teacher_id):
        self.teacher_name = teacher_name
        self.teacher_subject = subject
        self.teacher_id = teacher_id

    def __repr__(self) -> str:
        return f'Teacher Name: {self.teacher_name}. Her Subject: {self.teacher_subject}. Her Id: {self.teacher_id}'

class School:
    def __init__(self, name):
        self.name = name
        self.teachers = []
        self.students = []
    
    def add_teacher(self, id, name, subject):
        id = len(self.teachers) + 101
        teacher = Teacher(id, name, subject)
        self.teachers.append(teacher)
    
    def enroll(self, student_name, student_cls, fee):
        if fee < 6500:
            return 'Not Enough Fee'
        else:
            id = len(self.students) + 1
            student = Student(student_name, student_cls, id)
            self.students.append(student)
            return f'{student_name} is enroll with id: {id}. extra, money: {fee - 6500}'
    
    def __repr__(self) -> str:
        print('Welcome To: ', self.name)
        print('------OUR Teachers-------')
        for teacher in self.teachers:
            print(teacher)
        print('------OUR Students-------')
        for student in self.students:
            print(student)
            return 'All Done For Today.'


# rimi = Student('Rimi Akther', 6, 101)
# print(rimi)
# piyas = Teacher('Piyas Mahmud', 'Data Stucture', 101)
# nayem = Teacher('HM Nayem', 'Algoritom', 2)
# print(piyas)

phitron = School('Phitron')
phitron.enroll('baker', 6, 5200)
phitron.enroll('alia', 8, 8000)
phitron.enroll('sami', 8, 9000)

phitron.add_teacher('sumit sha', 'JS', 2)
phitron.add_teacher(3, 'HM Nayem', 'DS')
phitron.add_teacher(4, 'Piyas', 'C++')

print(phitron)