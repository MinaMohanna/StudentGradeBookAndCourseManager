from Gradebook import Gradebook
from student import Student
from course import Course
from Assessment import Quiz, Exam, Project


gb = Gradebook(passing_grade=55)

# Interactive menu for user
while True:
    print("\n===== Gradebook Manager =====")
    print("1. Add Student ")
    print("2. View Students")
    print("3. Add Course")
    print("4. Enroll")
    print("5. Add Assessment")
    print("6. Record Grade")
    print("7. View Report")
    print("8. Search")
    print("9. Delete Student  ")
    print("10. Get_letter_grade")
    print("11. Dashboard")
    print("12. Update Student information")
    print("0. Exit")

    choice = input("Choose: ").strip()

    try:
        if choice == "0":
            print("Goodbye!")
            break

        elif choice == "1":
            sid = input("Student ID: ")
            name = input("Name: ")
            email = input("Email: ")
            gb.add_student(Student(sid, name, email))

        elif choice == "2":
            gb.view_students()

        elif choice == "3":
            code = input("Course Code: ")
            name = input("Course Name: ")
            gb.add_course(Course(code, name))

        elif choice == "4":
            sid = input("Student ID: ")
            ccode = input("Course Code: ")
            gb.enroll_student(sid, ccode)

        elif choice == "5":
            ccode = input("Course Code: ")
            atype = input("Type (Q=Quiz, E=Exam, P=Project): ").upper()
            title = input("Title: ")
            max_score = float(input("Max Score: "))
            cls = {"Q": Quiz, "E": Exam, "P": Project}.get(atype, Quiz)
            gb.add_assessment(ccode, cls(title, max_score))

        elif choice == "6":
            sid = input("Student ID: ")
            ccode = input("Course Code: ")
            title = input("Assessment Title: ")
            score = float(input("Score: "))
            gb.record_grade(sid, ccode, title, score)

        elif choice == "7":
            sid = input("Student ID: ")
            gb.show_report(sid)

        elif choice == "8":
            keyword = input("Search by name or ID: ")
            found = gb.search_student(keyword)
            if found:
                for s in found:
                    s.display_info()
                    print("-" * 30)
            else:
                print("No students found.")

        elif choice == "9":
            sid = input("Student ID to delete: ")
            gb.delete_student(sid)

        elif choice == "10":
            sid= input("Student ID: ")
            ccode = input("Course Code: ")

            average = gb.calculate_average(sid, ccode)
            letter = gb.get_letter_grade(average)

            print(f"Average: {average}")
            print(f"Letter Grade: {letter}")
        elif choice == "11":
            gb.show_dashboard()

        elif choice == "12":
            sid = input("Student ID: ")
            name = input("Student Name: ")
            email = input("Student Email: ")
            gb.update_student(sid, name, email)
        else:
            print("Invalid option, try again.")

    # For unexpected Errors during app execution
    except Exception as e:
        print(f"Something went wrong: {e}")


