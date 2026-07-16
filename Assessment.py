# Add assessment to course
class Assessment:
    def __init__(self, title, max_score):
        self.title = title
        self.max_score = max_score


    def calculate_percentage(self, score):
        return round((score / self.max_score) * 100, 2)

    def grade_message(self, score):
        precentage = self.calculate_percentage(score)
        if precentage >= 50:
            return 'Passed'
        else:
            return 'Failed'

    def display_info(self):
        print(f"{self.title} _ Max Score: {self.max_score}%")

# Assessments  of course
class Quiz(Assessment):
    def __init__(self, title, max_score):
        # Method override on display grade message
        super().__init__(title, max_score)
    def grade_message(self, score):
        if score >= 80:
            return 'Great quiz result'
        elif score >= 50:
            return 'Good quiz result'
        else:
            return 'You failed, try again please'

        # Using method override on display information  method
    def display_info(self):
        print(f"Quiz: {self.title} _ Max Score: {self.max_score}%")




class Exam (Assessment):
    def __init__(self, title, max_score):

        # Method override on Display information
        super().__init__(title, max_score)
    def display_info(self):
        print(f"Exam: {self.title} _ Max Score: {self.max_score}%")

        # Using method override on grade message method
    def grade_message(self, score):
        if score >= 80:
            return 'Great Exam result'
        elif score >= 50:
            return 'Good exam result'
        else:
            return 'You failed, try again please'


class Project(Assessment):
    def __init__(self, title, max_score):

        # Method override on display information from Assessment's display method
        super().__init__(title, max_score)

    def display_info(self):
        print(f"Project: {self.title} _ Max Score: {self.max_score}%")

        # Method override on grade message from Assessment's grade message method
    def grade_message(self, score):
        if score >= 90:
            return 'Great Project result'
        elif score >= 50:
            return 'Good project result'
        else:
            return 'Bad, try again , project needs improvement '
