 ## Student GradeBook And Course Manager
## Mina Barati

## Name of project
Student Grade book And Course Manager System

## Details about project
This app is a comprehensive sytem for managing students, course , assessments , and grades.
Users interact with the system through an interactive menu to perform various management tasks.

### Student Operations:
- **Add Students:** Input student ID, name, and email to add a new student
- **View Students:** Display a complete list of all students which registered 
- **Search Students:** Find a student by name or ID
- **Delete Students:** Remove a student from the system along with all their records
- **Update Student:** Update student information (name, student ID, Email)


### Course Operations:
- **Add Course:** Define a new course with course code and course name
- **Enroll Students:** Register a student in a specific course


### Assessment and Grade Operations:
- **Add Assessment:** And three types of assessments (Quiz, Exam, Project) to a course and the max score
- **Record Grade:** Enter a student's score for each assessment

### Results and Reporting:
**View Report:** Display average grade, percentage, letter grade, and pass/fail status
**Get Letter grade:** Display students grade with an English alphabet 
**Dashboard:** Show overall statistics (total_students, courses, grade records)

**


## How To Run
``` bash
python main.py
then use the interactive menu by selecting 1-12 and 0 for exit

```
## ProjectFiles 
- **main.py:** Interactive  menu system for user interaction
- **GradeBook.py:** Gradebook system containing all logic 
- **student.py:** Student class for student data management 
- **course.py:** Course class for course management 
- **Assessment.py:** Assessments classes(quiz, exam, project) with inheritance
- **README.md:** Project documentation

## Programming Concepts Implemented
### 1.Encapsulation(data protection)
- **Student Email:** Stored as private attribute _email
- Accessed only through get_email() method
- Modified only through set_email() with email validation

### 2.Inheritance (Class Hierarchy)
**Assessment(Parent Class):**
- Common attributes : title, max_score
- common methods : calculate_percentage(), grade_message(), display_info()
- **Child classes:** Quiz, Exam, Project
- Inherit all parent attributes and methods

### 3.MethodOverriding
- Each assessment type overrides
- Grade Message in assessment
- Also overrides display_info() to show assessment type

### 4.InputValidation
- Verify student exists before operation
- Verify course exists before operations 
- Check student is enrolled in course before recording grades
- Validation score is between 0  and max_score
- Case_insensitive search for assessment 
- Clear error messages for invalid inputs

## Two CreativeFeatures 
### Feature1: LetterGradeSystem
Converts numeric average percentage to letter grades:
- A: 90% and above
- B: 80-89%
- C: 70-79%
- D: 55-69%
- F: Below 55%
#### Implements in get_letter_grade() method. Displayed in student reports.

## Feature2. Dashboard
#### Display total data storred in course
- Display total number of students in system 
- Display total number of courses in system
- Display total  number of assessments
- Display total number of grade records






