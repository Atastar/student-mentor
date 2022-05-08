class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_in_progress = []
        self.grades = {}
        self.courses_attached = []


    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_attached and course in lecturer.courses_in_progress:
            if course in lecturer.lect_grades:
                lecturer.lect_grades[course] += [grade]
            else:
                lecturer.lect_grades[course] = [grade]
        else:
            return 'Ошибка'


    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {calc(grade_list_st)} \nКурсы в процессе изучения: {self.courses_in_progress[0]}, {self.courses_in_progress[1]} \nЗавершенные курсы: Введение в программирование"



class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


class Reviewer(Mentor):
    def rate_rev(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname}"



class Lecturer(Student, Mentor):
    lect_grades = {}

    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {calc(grade_list_lec)}"


def calc (main_list: list):
    if not main_list:
        return 0

    quantity = len(main_list)
    value = 0
    for item in main_list:
        value += item

    result = value / quantity
    return result


class Comparison:

    def __init__(self, grade_st, grade_lec):
        self.grade_st = calc(grade_list_st)
        self.grade_lec = calc(grade_list_lec)

    def __eq__(self, other):
        if self.grade_st==self.grade_lec:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.grade_st < self.grade_lec:
            return True
        else:
            return False

    def __le__(self, other):
        if self.grade_st <= self.grade_lec:
            return True
        else:
            return False


best_student = Student('Ruoy', 'Eman')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['SQL']
best_student.courses_attached += ['Python']
best_student.courses_attached += ['SQL']

cool_mentor = Mentor('Men', 'Tor')
cool_mentor.courses_attached += ['Python']
cool_mentor.courses_attached += ['SQL']

reviewer = Reviewer('Some', 'Buddy')
reviewer.courses_attached += ['Python']
reviewer.courses_attached += ['SQL']

cool_lecturer = Lecturer('Lec', 'Ture')
cool_lecturer.courses_in_progress += ['Python']
cool_lecturer.courses_in_progress += ['SQL']


reviewer.rate_rev(best_student, 'Python', 10)
reviewer.rate_rev(best_student, 'Python', 9)
reviewer.rate_rev(best_student, 'Python', 8)

reviewer.rate_rev(best_student, 'SQL', 10)
reviewer.rate_rev(best_student, 'SQL', 10)

best_student.rate_lec(cool_lecturer, 'Python', 10)
best_student.rate_lec(cool_lecturer, 'Python', 8)
best_student.rate_lec(cool_lecturer, 'Python', 10)

best_student.rate_lec(cool_lecturer, 'SQL', 10)
best_student.rate_lec(cool_lecturer, 'SQL', 10)

grade_list_st = []
for key, value in best_student.grades.items():
    for item in value:
        grade_list_st.append(item)

grade_list_lec = []
for key, value in cool_lecturer.lect_grades.items():
    for item in value:
        grade_list_lec.append(item)


print(best_student)
print()
print(reviewer)
print()
print(cool_lecturer)
print()
print(calc(grade_list_st) == calc(grade_list_lec))
