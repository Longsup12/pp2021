import curses


def numOfStudent():
         std_num = int(input("How many student in class?: "))
         return std_num


def numOfCourse():
         course_num = int(input("How many student in class?: "))
         return course_num


def my_input(stdscr, r, c, prompt_string):
    curses.echo()
    stdscr.addstr(r, c, prompt_string)
    stdscr.refresh()
    __input = stdscr.getstr(r + 1, c, 20).decode('utf-8')
    return __input


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