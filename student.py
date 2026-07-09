class Student:
    def __init__(self, student_id, name, email, courses):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.courses = []


    def get_id(self, student_id):
        return self.student_id

    def set_id(self, student_id, name):
        self.student_id = student_id

    def set_name(self, _name):
        self.name = _name

    def get_name(self, name):
        return self.name

    def set_email(self, _email):
        self.email = _email

    def get_email(self):
        return self.email

    def enroll_courses(self, *course_code):
        self.courses.append(course_code)

    def display_info(self):
        print( self.student_id, self.name, self.email, self.courses)


new_student = Student("12345", "Mina", "mina@gmail.com", [])
new_student.display_info()
new_student.enroll_courses('python', 'math', 'islamic')
print(new_student.get_email())
print(new_student.courses)
