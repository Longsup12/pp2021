students = []
courses = []
def Number_of_students():
    return int(input('Enter number student now!:'))

def In4_of_student():
    return {
        'id' : input('Student id : \n'),
        'name' : input('Student name: \n'),
        'dob' : input('Student DOB: \n')
    }

def Number_of_course():
     return int(input('Give me a course number: \n'))

def Course_In4():
    return {
        'id' : input('Course name: \n'),
        'name' : input('Course ID: \n')
    }

def update_marks_of_course(course):
    print(f"Mark of {course['name']}:")
    course['marks'] = []

    for student in students:
        course['marks'].append((student,
            input(f"Mark of {student['name']}: ")))

def Courses_list():
    print ('We have:')
    for course in courses:
        print(f"- [{course['id']}] {course['name']}", end='')
        print( '(marks available)' if 'marks' in course else '')

def Student_list():
    print('Student list:')
    print(f'{"ID": ^10}{"Name":^15}{"DOB":^20}')
    for student in students: 
        print(f"{student['id']:^10}{student['dob']:^15}{student['name']:^20}")
    print()

def COursesmarks(course):
    if 'marks' in course:
        print(f"Marks of {course['name']}:")

        print(f'{"NAME":^10}{"MARK":^5}')
        for student, mark in course['marks']:
            print(f"{student['name']:<20}{mark:>5}")
    else:
        print('NO marks')

def select_course_prompt(intro_message):
    Courses_list()
    print(intro_message)

    return input('Choose a course: ')

def search(List, keyword):
    for item in List:
        if keyword in item.values():
            return item

    empty_item = List[0].copy()
    empty_item.clear()
    return empty_item

def action_loop(msg=None, callback=None):
    while True:
        keyword = select_course_prompt(f'-> {msg}')
        if not keyword:
            print()
            break
        callback(search(courses, keyword))
        print()

if __name__ == '__main__':

    for _ in range(Number_of_students()):
        students.append(In4_of_student())

    for _ in range(Number_of_course()):
        courses.append(Course_In4())

    Student_list()
    action_loop(msg='Marking courses...', callback=update_marks_of_course)
    action_loop(msg='Select a course to show marks...', callback=COursesmarks)

 