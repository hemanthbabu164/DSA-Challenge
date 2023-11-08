import json

class Student:
    def __init__(self, student_id, name, courses=[]):
        self.student_id = student_id
        self.name = name
        self.courses = courses

    def enroll_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
            return True
        else:
            print(f"{self.name} is already enrolled in {course.name}.")
            return False

    def drop_course(self, course):
        if course in self.courses:
            self.courses.remove(course)
            return True
        else:
            print(f"{self.name} is not enrolled in {course.name}.")
            return False

    def display_courses(self):
        print(f"{self.name}'s enrolled courses:")
        for course in self.courses:
            print(f"{course.name} ({course.code})")

class Course:
    def __init__(self, code, name, instructor):
        self.code = code
        self.name = name
        self.instructor = instructor

class University:
    def __init__(self):
        self.students = {}
        self.courses = []

    def add_student(self, student):
        self.students[student.student_id] = student

    def remove_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]

    def add_course(self, course):
        self.courses.append(course)

    def display_students(self):
        print("List of Students:")
        for student_id, student in self.students.items():
            print(f"Student ID: {student.student_id}, Name: {student.name}")

    def display_courses(self):
        print("List of Courses:")
        for course in self.courses:
            print(f"Course Code: {course.code}, Name: {course.name}, Instructor: {course.instructor}")

def load_data_from_json(university, filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            students_data = data.get("students", {})
            for student_id, student_info in students_data.items():
                student = Student(student_id, student_info["name"], student_info.get("courses", []))
                university.students[student_id] = student

            courses_data = data.get("courses", [])
            for course_info in courses_data:
                course = Course(course_info["code"], course_info["name"], course_info["instructor"])
                university.courses.append(course)
    except FileNotFoundError:
        print("File not found.")


def main():
    
    university = University()
    load_data_from_json(university, 'university_data.json') 

    while True:
        print("\nUniversity Management System")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. Enroll Student in Course")
        print("4. Drop Student from Course")
        print("5. List Students")
        print("6. List Courses")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            student = Student(student_id, name)
            university.add_student(student)
            print(f"{name} has been added as a student.")
        elif choice == '2':
            student_id = input("Enter student ID to remove: ")
            university.remove_student(student_id)
            print(f"Student with ID {student_id} has been removed.")
        elif choice == '3':
            student_id = input("Enter student ID: ")
            if student_id in university.students:
                student = university.students[student_id]
                university.display_courses()
                course_code = input("Enter course code to enroll: ")
                for course in university.courses:
                    if course.code == course_code:
                        student.enroll_course(course)
                        break
                else:
                    print("Course not found.")
            else:
                print(f"Student with ID {student_id} not found.")
        elif choice == '4':
            student_id = input("Enter student ID: ")
            if student_id in university.students:
                student = university.students[student_id]
                student.display_courses()
                course_code = input("Enter course code to drop: ")
                for course in university.courses:
                    if course.code == course_code:
                        student.drop_course(course)
                        break
                else:
                    print("Course not found.")
            else:
                print(f"Student with ID {student_id} not found.")
        elif choice == '5':
            university.display_students()
        elif choice == '6':
            university.display_courses()
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
