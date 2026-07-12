
class Student:
    def __init__(self, student_id, name, email):
        self.student_id = student_id
        self.name = name
        self._email = email
        self.courses = []


    def get_id(self):
        return self.student_id

    def set_id(self, student_id):
        self.student_id = student_id

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_email(self, email):
        self._email = email

    def get_email(self):
        return self._email

    def enroll_course(self, course_code):
        if course_code not in self.courses:
            self.courses.append(course_code)

    def display_info(self):
        print( self.student_id, self.name, self._email, self.courses)


