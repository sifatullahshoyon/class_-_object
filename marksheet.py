class Student:
    def __init__(self, mark):
        self.mark = mark
        self.max_mark = 100
        self.min_mark = 0
        self.a_plus = 80
        self.a = 70
        self.b = 60
        self.c = 50
        self.d = 40
        self.e = 33
    
    def bangla(self, student_name, mark):
        if mark > self.min_mark and mark <= self.max_mark:
            if mark > self.a_plus:
                print(f'{student_name} got a GPA 5')
                return
            elif mark >= self.a and mark < self.a_plus:
                print(f'{student_name} got a gpa A')
                return
            elif mark >= self.b and mark < self.a:
                print(f'{student_name} got a gpa B')
                return
            elif mark >= self.c and mark < self.b:
                print(f'{student_name} got a gpa C')
                return
            elif mark >= self.d and mark < self.c:
                print(f'{student_name} got a gpa D')
                return
            elif mark >= self.e and mark < self.d:
                print(f'{student_name} got a gpa E')
                return
            else:
                print(f'{student_name} Fail')
                return
        else:
            print('Invalid Mark.')
            return

grade_sheet = Student(55)
grade_sheet.bangla('Auntu', 58)