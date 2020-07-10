class Student:
    counter = 0
    def __get_id__(self):
        Student.counter += 1
        return Student.counter

    def __init__(self, first_name, last_name, courses=None):
        self.first_name = first_name
        self.last_name = last_name
        if courses is None:
            self.courses = []
        else:
            self.courses = courses
        self.student_id = self.__get_id__()

    def add_course(self, new_course):
        if new_course not in self.courses:
            self.courses.append(new_course)
            print(f'{self.first_name} {self.last_name} was enrolled to the {new_course} course')
        else:
            print(f'{self.first_name} {self.last_name} is already enrolled in the {new_course} course')

    def remove_course(self, course):
        if course in self.courses:
            self.courses.remove(course)
            print(f'{self.first_name} {self.last_name} was removed from the {course} course')
        else:
            print(f'{course} not found')

    def __eq__(self, other):
        return self.first_name == other.first_name and self.last_name == other.last_name

    def __repr__(self):
        return f'{self.student_id}: {self.first_name} {self.last_name} is student at courses: {self.courses}'

class Group:
    def __init__(self, amt):
        self.group = []
        for _ in range(amt):
            self.group.append(None)

    def __repr__(self):
        return f'{self.group}'

students = []
with open('D:\\USERDATA\\Documents\\4git\\oop\\ch_algo\\students_list.txt', 'r') as f:
    for line in f:
        name, courses = line.strip().split(':')
        first_name, last_name = name.split(',')
        courses = courses.split(',')
        student = Student(first_name, last_name, courses)
        students.append(student)

print(*students)

group = Group(4)
print(group)