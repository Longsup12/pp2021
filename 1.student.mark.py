students = []
courses = []
marks = []

def Numberofstu():
    Numberofstu = int(input("The number of students: \n"))
    return Numberofstu 

def InputstuInfo():
    studentId = input("Student ID: \n")
    studentName = input(" Student name: \n")
    studentDoB = input("Student DoB: \n")
    return {"id": studentId, "name": studentName, "Dob": studentDoB}

def NumberOfCours():
    numberOfCours = int(input("The number of courses: \n"))
    return numberOfCours 

def CourseInfo():
    coursId = input("Courses ID: \n")
    coursName = input("Courses Name: \n")
    return {"id": coursId, "name": coursName}

def InputMark(course) :
    marks.append({course: {}})
    for i in range(len(students)):
        mark = float(input("Student marks: \n"))
        marks[len(marks) - 1][course].update({students[i]["name"]: mark})

def showCoursesInfo(courses):
    print("Courses Info: ")
    for key, value in courses.items():
        print(value)


def showStudentsInfo(students):
    print("Student Info: ")
    for i in range(len(students)):
        print("Student Id " + "Student name " + "Student date of birth ")
        for value in students[i].items():
            print(value[1])


def showMarksInfo(marks, courseName, studentName):
    for i in range(len(marks)):
        for key, value in marks[i].items():
            for keyy, valuee in value.items():
                if (key == courseName and keyy == studentName):
                    print(valuee)


if __name__ == "__main__":

    numberOfStudents = Numberofstu()
    print(numberOfStudents)
    for i in range(numberOfStudents):
        studentId, studentName, studentDob = InputstuInfo()
        students.append({"id": studentId, "name": studentName, "dob": studentDob})

    numberOfCourses = NumberOfCours()
    for i in range(0, numberOfCourses):
        coursId, coursName = CourseInfo()
        courses[coursId] = coursName

    y = input("continue press y, not continue press n")
    while (y == "y"):
        s = input("enter m for marks input other to cancel")
        if (s == "m"):
            coursId = input("Enter the courseId: ")
            coursName = courses[coursId]
            InputMark(students, coursName, marks)
        else:
            break

    print(marks)
    showCoursesInfo(courses)
    showStudentsInfo(students)
    courseName = input("Enter the name of the course: ")
    studentName = (input("Enter the name of the student: "))
    showMarksInfo(marks, courseName, studentName)
