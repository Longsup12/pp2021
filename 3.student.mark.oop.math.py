import math
import numpy as np

students = []
courses = []
class Student:
    def __init__(self, student_id, studentname, studentdob):
        self.id = student_id
        self.name = studentname
        self.dob = studentdob
        self.gpa = 0
        self.marks = np.array([[], [], []])

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_dob(self):
        return self.dob

    def get_mark(self):
        return self.marks

    def set_id(self, _id):
        self.id = _id

    def set_name(self, name):
        self.name = name

    def set_dob(self, dob):
        self.dob = dob
    
    def set_mark(self, course, mark, credit):
        self.marks = np.append(self.marks, [[course], [mark], [credit]], axis=1)

    def get_gpa(self):
        sum_credits = 0
        for i in range(len(courses)):
            self.gpa += int(self.marks[1][i]) * int(self.marks[2][i])
            sum_credits += int(self.marks[2][i])

        self.gpa = math.floor((self.gpa/sum_credits) * 10) / 10
        return self.gpa

    def displayStudent(self):
        print("Student ID: " + self.id)
        print("Student name: " + self.name)
        print("Student DoB: " + self.dob)
        print("Student GPA: " + str(self.gpa))


class Course:
    def __init__(self, id, name,credit):
        self.id = id
        self.name = name
        self.credit = credit

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def set_id(self, id):
        self.id = id

    def set_name(self, name):
        self.name = name

    def set_credit(self, credit):
        self.credit = credit

    def displayCourse(self):
        print("Course ID: " + self.id)
        print("Course name: " + self.name)
        print("Course credit: " + self.credit)

def numOfStudent():
         std_num = int(input("How many student in class?: "))
         return std_num
       

def studentInfo():
    std_id = input("Student ID: ")
    std_name = input("Student name: ")
    std_dob = input("Student DOB: ")
    return std_id, std_name, std_dob


def numOfCourse():
            course_num = int(input("Number of courses: "))
            return course_num
       
def courseInfo():
    course_id = input("Course ID: ")
    course_name = input("Course name: ")
    course_credit = input("Enter course credit: ")
    return course_id, course_name, course_credit


def findCourseName(courses, course_id):
    for course in courses:
        if course.get_id() == course_id:
            return course.get_name()
    print("Err: Invalid ID")

def findCourseCredit(courses, course_id):
    for course in courses:
        if course.get_id() == course_id:
            return course.get_credit()
    print("Err: Invalid ID")


def sortByGpa():
    sorted_students = sorted(students, key=lambda student: student.gpa, reverse=True)
    for student in sorted_students:
        student.displayStudent()


if __name__ == "__main__":

    student_num = numOfStudent()
    for i in range(0, student_num):
        id, name, dob = studentInfo()
        students.append(Student(id, name, dob))

    course_num = numOfCourse()
    for i in range(0, course_num):
        id, name, credit = courseInfo()
        courses.append(Course(id, name, credit))

    print("Display courses information:\n")
    for course in courses:
        course.displayCourse()

    x = 'y'
    while x == 'y':
        sel_course_id = input("Select a course ID: ")
        sel_course = findCourseName(courses, sel_course_id)
        sel_credit = findCourseCredit(courses, sel_course_id)
        print("Course name: " + sel_course + "\n")
        for student in students:
            mark = input("Enter " + student.name + "'s mark: ")
            student.set_mark(sel_course, mark, sel_credit)
        x = input("Do you want to select another course? y/n: ")
        print("-------")

    for student in students:
        student.get_gpa()

    print("Display student list by GPA descending:\n")
    sortByGpa()