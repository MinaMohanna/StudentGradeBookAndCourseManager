# Course class course attributes

class Course:
    def __init__(self, course_code, course_name, students=None, assessments= None):
        self.course_code = course_code
        self.course_name = course_name
        if students is None:
            self.students = []
        else:
            self.students = students

        if assessments is None:
            self.assessments = []
        else:
            self.assessments = assessments

    # add student to course
    def add_student(self, student_id):
        if student_id not in self.students:
            self.students.append(student_id)

    # add assessment for course
    def add_assessment(self, assessment):
        self.assessments.append(assessment)

    # Finds assessment to add student in this
    def find_assessment(self, title):
        if title is None:
            return None
        for a in self.assessments:
            if str(a.title).lower() == str(title).lower():
                return a
        return None

    # remove student from the course when we delete student from app records
    def remove_student(self, student_id):
        if student_id in self.students:
            self.students.remove(student_id)

    # Display all course Info( Course code, course name, students , assessments )
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





