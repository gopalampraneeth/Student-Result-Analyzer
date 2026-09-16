from models.student import Student
from services.result_manager import ResultManager


def get_marks():
    marks = {}

    while True:
        subject = input("Enter subject name (type 'done' to stop): ")

        if subject.lower() == "done":
            break

        try:
            mark = float(input(f"Marks for {subject}: "))

            if mark < 0 or mark > 100:
                print("Marks should be between 0 and 100.")
                continue

            marks[subject] = mark

        except ValueError:
            print("Please enter a valid number.")

    return marks


def main():

    manager = ResultManager()

    while True:

        print("\n=== Student Result Analyzer ===")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Find Topper")
        print("4. Exit")

        choice = input("Enter your choice: ")

        # Add Student
        if choice == "1":

            name = input("Enter student name: ")
            roll_no = input("Enter roll number: ")

            marks = get_marks()

            if not marks:
                print("Student must have at least one subject.")
                continue

            student = Student(name, roll_no, marks)

            manager.add_student(student)

            print("Student added successfully!")

        # View All Students
        elif choice == "2":

            students = manager.get_all_students()

            if not students:
                print("No students found.")

            else:
                print("\n=== All Students ===")

                for student in students:
                    print(student)

        # Find Topper
        elif choice == "3":

            topper = manager.find_topper()

            if topper:
                print("\n=== Class Topper ===")
                print(topper)

            else:
                print("No students available.")

        # Exit
        elif choice == "4":

            print("Thank you for using Student Result Analyzer!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()