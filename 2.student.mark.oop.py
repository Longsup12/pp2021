student_list = []
course_list = []

class student:
    def __init__(self, studName="", studId="", studDob="", courses=""):
        self.studName   = studName
        self.studId    = studId
        self.studDob    = studDob
        self.courses = courses
    
    def inputSt(self, name, studId, studDob, courses):
        st = student(name, studId, studDob, courses)
        student_list.append(st)
    
    def listSt(self, st):
        print(f'Name: {st.studName}')
        print(f'Id: {st.studId}')
        print(f'Date Of Bird: {st.studDob}')
        for u, v in st.courses.items():
            print(f'Mark for {u}: {v}')
    
    def listCourse(self, course_name):
        
        anotherStList = []
        
        for i in range(len(student_list)):
            for u, v in student_list[i].courses.items():
                if course_name == u:
                    anotherStList.append(student_list[i].studName)
        
        print(f'number of student in {course_name}: {len(anotherStList)}')
        print('Student list: ')
        for i in anotherStList:
            print(f'             - {i}')
            
    def deleteSt(self, name):
        for i in range(len(student_list)):
            if name == student_list[i].studName:
                print(f'student {name} is deleted')
                del student_list[i]

class course:
    def __init__(self, courseId="", courseName=""):
        self.courseId = courseId
        self.courseName = courseName
    
    def inputCourse(self, courseId, courseName):
        c = course(courseId, courseName)
        course_list.append(c)
    
    def mark(self, name, courseName, mark):
        for i in range(len(student_list)):
            if name in student_list[i].studName:
                student_list[i].courses[courseName] = mark

class GPA:
    def __init__(self, name=''):
        self.namee = name

    def calcGPA(self, name, credit):
        ls = []
        for i in range(len(student_list)):
            if name == student_list[i].stName:
                print(student_list[i].courses)
                ls.append(student_list[i].courses)
                grade = np.array([list(d.values()) for d in ls])
                credit = np.array(credit)
                gpa = grade.dot(credit)/sum(credit)
                return tuple((name, gpa))
    
    def sort(self):
        gpa_list = []
        for i in range(len(student_list)):
            gpa_list.append(self.calcGPA(student_list[i].stName, [3, 5]))
        sorted_list = sorted(gpa_list, key=lambda i: i[1])
        for head,tail in enumerate(sorted_list):
            print(f"Ranking {head+1} is {tail[0]} with {tail[1]} points")
            
st = student()
st.inputSt('Minh', 'bi10-118', '2001', {})
st.inputSt('Khai', 'bi10-077', '2001', {})
st.inputSt('Nghia', 'bi10-075', '2001', {})
m = course('','')
m.inputCourse(0, 'Python')

m.mark('Minh', 'Python', 17)
m.mark('Khai', 'Python', 15)
m.mark('Nghia', 'Python', 16)

m.mark('Minh', 'ADS', 19)
m.mark('Khai', 'ADS', 18)
m.mark('Nghia', 'ADS', 17)

for i in range(len(student_list)):
    st.listSt(student_list[i])

st.listCourse('Python')

for i in range(len(student_list)):
    st.listSt(student_list[i])

gpa = GPA()
gpa.sort()