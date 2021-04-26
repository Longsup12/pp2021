import math
import numpy as np


class Student:
    def __init__(self, student_id, studentname, studentdob):
        self.id = student_id
        self.name = studentname
        self.dob = studentdob
        self.marks = np.array([[], [], []])

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_dob(self):
        return self.dob

    def get_mark(self):
        return self.marks

    def set_id(self, __id):
        self.id = __id

    def set_name(self, __name):
        self.name = __name

    def set_dob(self, __dob):
        self.dob = __dob

    def set_mark(self, __course, __mark, __credit):
        self.marks = np.append(self.marks, [[__course], [__mark], [__credit]], axis=1)

    def get_gpa(self, courses):
        sum_credits = 0
        for i in range(len(courses)):
            self.gpa += int(self.marks[1][i]) * int(self.marks[2][i])
            sum_credits += int(self.marks[2][i])

        self.gpa = math.floor((self.gpa / sum_credits) * 10) / 10
        return self.gpa

    def display_mark(self, stdscr, courses, course):
        for i in range(len(courses)):
            if len(self.marks[0]) > i:
                if self.marks[0][i] == course:
                    stdscr.addstr(f"{self.name} 's mark: {self.marks[1][i]}\n")
                    break
            else:
                stdscr.addstr(f"{self.name} 's mark: none\n")
                break

    def display_student(self, stdsrc):
        stdsrc.addstr(f"Student ID: {self.id}\n"
                      f"Student name: {self.name}\n"
                      f"Student DoB: {self.dob}\n"
                      f"Student GPA: {self.gpa}\n"
                      f"-------\n")


class Course:
    def __init__(self, id, name, credit):
        self.id = id
        self.name = name
        self.credit = credit

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_credit(self):
        return self.credit

    def set_id(self, id):
        self.id = id

    def set_name(self, name):
        self.name = name

    def set_credit(self, credit):
        self.credit = credit

    def display_course(self, stdsrc):
        stdsrc.addstr(f"Course ID: {self.id}\n"
                      f"Course name: {self.name}\n"
                      f"Course credit: {self.credit}\n"
