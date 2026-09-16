class Student:

    def __init__(self, name: str, roll_no: str, marks: dict):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def calculate_total(self):
        return sum(self.marks.values())

    def calculate_average(self):
        if len(self.marks) == 0:
            return 0

        return self.calculate_total() / len(self.marks)

    def calculate_grade(self):
        avg = self.calculate_average()

        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"

    def to_dict(self):
        return {
            "name": self.name,
            "roll_no": self.roll_no,
            "marks": self.marks
        }

    @staticmethod
    def from_dict(data):
        return Student(
            name=data["name"],
            roll_no=data["roll_no"],
            marks=data["marks"]
        )

    def __str__(self):
        return (
            f"Name: {self.name}, "
            f"Roll No: {self.roll_no}, "
            f"Total: {self.calculate_total()}, "
            f"Average: {self.calculate_average():.2f}, "
            f"Grade: {self.calculate_grade()}"
        )