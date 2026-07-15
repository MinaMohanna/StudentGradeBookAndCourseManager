from student import Student
from course import Course
from Assessment import Quiz, Exam, Project, Assessment

# GradeBook class connect all classes together and contain all logic
class Gradebook:
    def __init__(self,  passing_grade):
        self.students = {}
        self.courses = {}
        self.grades = {}
        self.passing_grade = passing_grade
    # Add student method stores students information and add it to gradebook
    def add_student(self, student):
        if student.get_id() not in self.students:
            self.students[student.get_id()] = student
            print(f"Student {student.get_name()} added successfully")
        else:
            print("Student already added")

    # Adding Course by getting course Name and  Course ID from user
    def add_course(self, course):
        if course.course_code not in self.courses:
            self.courses[course.course_code] = course
            print(f"Course {course.course_code} added successfully")
        else:
            print("Course already added")

    # Enrolling student by using Student id and student name
    def enroll_student(self, student_id, course_code):

        # Display a message to user if student_id does not exist  and avoiding from error for user
        if student_id not in self.students:
            print("Error: Student not found")
            return

        # Display a message to user if course_code  does not exist  and avoiding from error for user
        if course_code not in self.courses:
            print("Error: Course not found")
            return

        # If there was not a problem for enrolling student then user can enroll student
        student = self.students[student_id]
        course = self.courses[course_code]
        student.enroll_course(course_code)
        course.add_student(student_id)
        print(f"{student.get_name()} enrolled in course {course_code}")

    # Add assessment in gradebook by getting course code and assessment name
    def add_assessment(self, course_code, assessment):

        # Display a message for user that course code is not true and avoid error for user
        if course_code not in self.courses:
            print("Error: Course not found")
            return

        course = self.courses[course_code]
        course.add_assessment(assessment)
        print(f" assessment {assessment.title} added to course {course.course_name}. ")

    # Records grade for assessment that user interred for student by getting student id , course code , assessment title and score from user
    def record_grade(self, student_id, course_code, assessment_title, score):
        # display message for user and avoiding from error
        if student_id not in self.students:
            print("Error: Student not found")
            return

        # display message for user and avoiding from error
        if course_code not in self.courses:
            print("Error: Course not found")
            return

        # if course code was added to course before  adds record
        course = self.courses[course_code]

        # if course code was not  added to course before  do not add the record and display message for user
        if student_id not in course.students:
            print("Error: Student with this ID not found in this course")
            return

        # if assessment   was added to course before  adds record
        assessment = course.find_assessment(assessment_title)

        # if assessment  was not  added to assessment before  do not add the record and display message for user
        if assessment is None:
            print("Error: Assessment not found")
            return

        # Avoid error if user enter a negative number or bigger then max score:
        if score < 0 or score > assessment.max_score:
            print(f"Error: Score must be between 0 and {assessment.max_score}")
            return

        self.grades.setdefault(student_id,{}).setdefault(course_code,{})
        self.grades[student_id][course_code][assessment.title] = score

        print(f" Recorded {score}/ {assessment.max_score} for {assessment_title}")
        print(f"Feedback: {assessment.grade_message(score)}")

    def calculate_average(self, student_id, course_code):
        if student_id not in self.grades:
            return 0

        course_grades = self.grades[student_id][course_code]
        course =self.courses[course_code]

        percentage =[]
        for title, score in course_grades.items():
            assessment = course.find_assessment(title)
            if assessment:
                pct = assessment.calculate_percentage(score)
                percentage.append(pct)
        if not percentage:
            return 0

        return round(sum(percentage)/len(percentage),2)

    def show_report(self, student_id):
        if student_id not in self.students:
            print("Error: Student not found")
            return

        student = self.students[student_id]
        print("\n ============ Student Report =============")
        print(f"Student ID : {student.get_id()}")
        print(f"Student Name : {student.get_name()}")
        print(f"Student Email : {student.get_email()}")

        for course_code in student.courses:
            course = self.courses.get(course_code)
            if not course:
                continue

            print(f" \nCourse: {course_code} - {course.course_name}")
            course_grades = self.grades.get(student_id,{}).get(course_code)

            if not course_grades:
                print("No grades recorded yet")
                continue

            print("Grades:")
            for title, score in course_grades.items():
                assessment = course.find_assessment(title)
                pct = assessment.calculate_percentage(score)
                print(f"  {title}: {score} / {assessment.max_score if assessment else '?'} = {pct}%")

            avg = self.calculate_average(student_id, course_code)
            print(f"Average score: {avg} %")
            print(f"Result: {self.get_result(avg)}")
        print("=" * 27)

    def get_result(self, average):
        return "Passed" if average >= self.passing_grade else "Failed"


    def search_student(self, keyword):
        keyword = keyword.lower()
        results = []

        for student in self.students.values():
            if keyword in student.get_id().lower() or keyword in student.get_name().lower():
                results.append(student)

        return results

    def delete_student(self, student_id):
        if student_id not in self.students:
            print("Error: Student not found")
            return

        student = self.students[student_id]

        for course_code in list(student.courses):
            course = self.courses.get(course_code)
            if course:
                course.remove_student(student_id)

        if student_id in self.grades:
            del self.grades[student_id]

        del self.students[student_id]
        print(f"Student '{student.get_name()}' deleted")


    def view_students(self):
        if not self.students:
            print("No students yet")
            return

        print("\n ============ All students ============")
        for student in self.students.values():
            student.display_info()
            print("_" * 30)



    def get_letter_grade(self, average):
        if average >= 90:
            return "A"
        elif average >= 80:
            return  "B"
        elif average >= 70:
            return "C"
        elif average >= 55:
            return "D"
        else:
            return "F"



    def show_dashboard(self):
        total_students = len(self.students)
        total_courses = len(self.courses)
        total_assessments = sum(len(c.assessments) for c in self.courses.values())

        total_records =0
        for student in self.grades.values():
            for course_grades in student.values():
                total_records += len(course_grades)

        print("\n============= Dashboard ============")
        print(f"Total Students: {total_students}")
        print(f"Total Courses: {total_courses}")
        print(f"Total Assessments: {total_assessments}")
        print(f"Total grades Records: {total_records}")


    def update_student(self, student_id, name, email):
        if student_id not in self.students:
            print("Error: Student not found")
            return

        student = self.students[student_id]
        student.set_name(name)
        student.set_email(email)

        print(f"Student '{student.get_name()}' updated successfully")
