import json
import re

class StudentManagement:
    def __init__(self):
        self.Students = []

    def load_Data(self):    
        try:
            with open("student.json", "r") as jsonFile:
                return json.load(jsonFile)
        except FileNotFoundError:
            print("Creating File")
            f = open("student.json", "x")
            f.close()
            return []

    def savetoJSON(self, students):
        with open("student.json", "w") as jsonFile:
            json.dump(students, jsonFile, indent=4)

    def addStudent(self, studentID, studentName, studentCourse, studentYR):
        # Input Validation
        if not studentID.isdigit():
            print("❌ Invalid Student ID. Must be a number.")
            return
        
        if any(student["id"] == studentID for student in self.Students):
            print("❌ Student ID already exists.")
            return

        # Allow letters and spaces for name and course
        if not studentName or not re.match("^[A-Za-z\s]+$", studentName):
            print("❌ Invalid Student Name. It should only contain letters and spaces.")
            return

        if not studentCourse or not re.match("^[A-Za-z\s]+$", studentCourse):
            print("❌ Invalid Course Name. It should only contain letters and spaces.")
            return

        if not studentCourse or not re.match("^[A-Za-z\s]+$", studentCourse):
            print("❌ Invalid Course Year. It should only contain letters and spaces.")
            return

        student = {
            "id": studentID,
            "StudentName": studentName,
            "StudentCourse": studentCourse,
            "StudentYear": studentYR
        }

        self.Students = self.load_Data()
        self.Students.append(student)
        self.savetoJSON(self.Students)
        print("✅ Student added successfully!")

    def viewStudent(self):
        self.Students.clear()
        self.Students = self.load_Data()
        print("\nStudent Record")
        for student in self.Students:
            print(f"\nID: {student['id']}")
            print(f"Student's Name: {student['StudentName']}")
            print(f"Student's Course: {student['StudentCourse']}")
            print(f"Student's Year: {student['StudentYear']}")

    def updateStudent(self, studentID):
        self.Students.clear()
        self.Students = self.load_Data()
        for index, student in enumerate(self.Students):
            if studentID == student["id"]:
                student["StudentName"] = input(f"Enter Student Name[{student['StudentName']}]: ")
                student["StudentCourse"] = input(f"Enter Student Course[{student['StudentCourse']}]: ")
                student["StudentYear"] = input(f"Enter Student Year[{student['StudentYear']}]: ")
                self.savetoJSON(self.Students)
                print("✅ Student information updated!")
                return
        print("❌ Student ID not found.")

    def delete_student(self, studentID):
        self.Students.clear()
        self.Students = self.load_Data()
        for student in self.Students:
            if studentID == student["id"]:
                self.Students.remove(student)
                self.savetoJSON(self.Students)
                print("🗑️ Student information deleted!")
                return
        print("❌ Student ID not found.")

    def searchStudent(self, studentID):
        self.Students.clear()
        self.Students = self.load_Data()
        print("\nFound Student Record:")
        for student in self.Students:
            if studentID == student["id"]:
                print(f"\nID: {student['id']}")
                print(f"Student's Name: {student['StudentName']}")
                print(f"Student's Course: {student['StudentCourse']}")
                print(f"Student's Year: {student['StudentYear']}")
                return
        print("❌ Student ID not found.")


class StudentAction:
    def execute(self):
        pass

class AddStudent(StudentAction):
    def execute(self):
        studentID = input("Enter Student ID: ")
        studentName = input("Enter Student Name: ")
        studentCourse = input("Enter Student Course: ")
        studentYR = input("Enter Student Year: ")
        sm = StudentManagement()
        sm.addStudent(studentID, studentName, studentCourse, studentYR)

class ViewStudent(StudentAction):
    def execute(self):
        sm = StudentManagement()
        sm.viewStudent()

class UpdateStudent(StudentAction):
    def execute(self):
        sm = StudentManagement()
        studentID = input("Enter Student ID: ")
        sm.updateStudent(studentID)

class DeleteStudent(StudentAction):
    def execute(self):
        sm = StudentManagement()
        studentID = input("Enter Student ID: ")
        sm.delete_student(studentID)

class SearchStudent(StudentAction):
    def execute(self):
        sm = StudentManagement()
        studentID = input("Enter Student ID: ")
        sm.searchStudent(studentID)

def selectFunc():
    print("Student Information System")
    print("1. Add a Student")
    print("2. View student Record")
    print("3. Update Student Record")
    print("4. Delete Student Record")
    print("5. Search a Student")
    print("Please select one of the following")
    choice = input("Enter Choice: ")
    return choice

choice = selectFunc()

if choice == '1':
    addStudent = AddStudent()
    addStudent.execute()
elif choice == '2':
    viewStudent = ViewStudent()
    viewStudent.execute()
elif choice == '3':
    updateStudent = UpdateStudent()
    updateStudent.execute()
elif choice == '4':
    deleteStudent = DeleteStudent()
    deleteStudent.execute()
elif choice == '5':
    searchStudent = SearchStudent()
    searchStudent.execute()
else:
    print("❌ Invalid Choice... Exiting")
