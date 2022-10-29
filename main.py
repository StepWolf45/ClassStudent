import inspect
class Student:
    def __init__(self, name=None, surname=None, age=None, grade=None, marks=None):
        if name is None:
            name, surname = "Vasya", "Pupkin"
            age, grade = 16, 10
            marks = [5, 5, 5]
        self.name = name
        self.surname = surname
        self.age = age
        self.grade = grade
        self.marks = marks
    def show(self):
        data = f'{self.name} {self.surname} {self.age} {self.grade} {len(self.marks)}'
        marks = " ".join(list(map(str, self.marks)))
        print(f'{data}\n{marks}')
    def get_average_mark(self):
        res = 0
        for i in range(len(self.marks)):
            res+=self.marks[i]
        print('%.6f' % (res/len(self.marks)))
    def will_graduate(self, after_years):
        if self.grade+after_years>11:
            return True
        return False
    def age_enterance(self):
        school_age = self.age - self.grade +1
        print(school_age)
def read_student():
    data = input().split()
    name, surname = data[0], data[1]
    age, grade, count = map(int, data[2:])
    marks = list(map(int,input().split()))
    return Student(name,surname,age,grade,marks)
def print_all_students(journal):
    for student in journal:
        student.show()
def main():
    journal = []
    for i in range(5):
         journal.append(read_student())
         if i!=4:
             pust = input()
    for student in journal:
        student.age_enterance()
def check_names():
    names = [
        {'name': 'Student', 'type': 'класс'},
        {'name': 'read_student', 'type': 'метод'},
        {'name': 'print_all_students', 'type': 'метод'},
    ]
    for item in names:
        if item['name'] not in globals().keys():
            raise RuntimeError(f"Ошибка: в программе не определён {item['type']} {item['name']}")
def check_types():
    type_settings = [
        {'name': 'Student', 'type': 'isclass', 'typename': 'класс'},
        {'name': 'read_student', 'type': 'isfunction', 'typename': 'метод'},
        {'name': 'print_all_students', 'type': 'isfunction', 'typename': 'метод'},
    ]
    for item in type_settings:
        method = getattr(inspect, item['type'])
        if not method(globals()[item['name']]):
            raise RuntimeError(f"Ошибка: {item['name']} не является {item['typename']}ом")
def check_student_defaults():
    try:
        Student()
    except TypeError:
        raise RuntimeError('Ошибка: в конструкторе класса Student не указаны значения по умолчанию для всех параметров')
def check_student_show():
    s = Student('Bill', 'Gates', 42, 11, [5, 5, 5])
    if not hasattr(s, 'show'):
        raise RuntimeError('Ошибка: в классе Student нет метода show')
    if not inspect.ismethod(s.show):
        raise RuntimeError('Ошибка: поле show класса Student не является методом')
def check_print_all_students():
    try:
        a = print_all_students
    except NameError:
        raise RuntimeError('Ошибка: в программе не определён метод print_all_students')
if __name__ == '__main__':
    check_names()
    check_types()
    check_student_defaults()
    check_student_show()
    check_print_all_students()
    main()
