class Course:
    def __init__(self, course_code, course_name, students=None, assessments= None):
        self.course_code = course_code
        self.course_name = course_name
        self.students = students if students else []
        self.assessments = assessments if assessments else []

    def add_student(self, student_id):
        if student_id not in self.students:
            self.students.append(student_id)
    def add_assessment(self, assessment):
        self.assessments.append(assessment)
    def find_assessment(self, title):
        if title is None:
            return None
        for a in self.assessments:
            if str(a.title).lower() == str(title).lower():
                return a
        return None

    def remove_student(self, student_id):
        if student_id in self.students:
            self.students.remove(student_id)

    def display_info(self):
        print(f"course_code: {self.course_code}")
        print(f"course_name: {self.course_name}")
        print(f"Enrolled Students: {self.students}")
        print(f"Assessments: ")
        if not self.assessments:
            print("No Assessments")
        for a in self.assessments:
            print('_', a)
            a.display_info()





