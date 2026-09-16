from models.student import Student
from utils.file_handler import FileHandler


class ResultManager:

    def __init__(self):
        self.file_handler = FileHandler()
        self.students = self.load_students()

    def add_student(self, student: Student):
        self.students.append(student)
        self.save_students()

    def get_all_students(self):
        return self.students

    def find_topper(self):
        if not self.students:
            return None

        return max(
            self.students,
            key=lambda student: student.calculate_total()
        )

    def save_students(self):
        data = [
            student.to_dict()
            for student in self.students
        ]

        self.file_handler.save(data)

    def load_students(self):
        data = self.file_handler.load()

        return [
            Student.from_dict(item)
            for item in data
        ]