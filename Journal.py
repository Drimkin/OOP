class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
 
    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _average_grade(self):
        average_grade = sum([sum(grade) for grade in self.grades.values()]) / sum([len(grade) for grade in self.grades.values()])
        return average_grade

 
    def __str__(self):
        some_student = f'Имя: {self.name}\n Фамилия: {self.surname}\n Средняя оценка за домашние задания:' \
                       f' {self._average_grade()}\n Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n ' \
                       f'Завершенные курсы: {", ".join(self.finished_courses)}'
        return some_student

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Это не студент')
        else:
            return self._average_grade() < other._average_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _average_grade(self):
        average_grade = sum([sum(grade) for grade in self.grades.values()]) / sum([len(grade) for grade in self.grades.values()])
        return average_grade

    def __str__(self):
        some_lecturer = f'Имя: {self.name}\n Фамилия: {self.surname}\n Средняя оценка за лекции: {self._average_grade()}'
        return some_lecturer

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Это не лектор')
        else:
            return self._average_grade() < other._average_grade()

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        some_reviewer = f'Имя: {self.name}\n Фамилия: {self.surname}'
        return some_reviewer

def average_grade_student(list_student, course):
   res = sum([sum(student.grades[course]) for student in list_student]) / sum([len(student.grades[course]) for student in list_student])
   return res

def average_grade_lecturer(list_lecturer, course):
   res = sum([sum(lecturer.grades[course]) for lecturer in list_lecturer]) / sum([len(lecturer.grades[course]) for lecturer in list_lecturer])
   return res

lecturer_1 = Lecturer('Yuriy', 'Smirnov')
lecturer_1.courses_attached.append('Python')
lecturer_1.courses_attached.append('Java')

lecturer_2 = Lecturer('Inna', 'Ivanova')
lecturer_2.courses_attached.append('Java')
lecturer_2.courses_attached.append('Go')

reviewer_1 = Reviewer('Stepan', 'Bublikov')
reviewer_1.courses_attached.append('Java')
reviewer_1.courses_attached.append('Go')

reviewer_2 = Reviewer('Victor', 'Petrov')
reviewer_2.courses_attached.append('Python')

student_1 = Student('Dmitry', 'Ivanov', 'man')
student_1.courses_in_progress.append('Java')
student_1.finished_courses.append('Python')

student_2 = Student('Yana', 'Popova', 'woman')
student_2.courses_in_progress.append('Python')
student_2.courses_in_progress.append('Java')
student_2.finished_courses.append('Go')

student_1.rate_lecturer(lecturer_1, 'Python', 10)
student_1.rate_lecturer(lecturer_1, 'Python', 7)
student_1.rate_lecturer(lecturer_1, 'Java', 9)
student_1.rate_lecturer(lecturer_2, 'Java', 9)
student_1.rate_lecturer(lecturer_1, 'Java', 8)

student_2.rate_lecturer(lecturer_2, 'Go', 8)
student_2.rate_lecturer(lecturer_2, 'Go', 7)
student_2.rate_lecturer(lecturer_1, 'Python', 9)
student_2.rate_lecturer(lecturer_1, 'Python', 10)
student_2.rate_lecturer(lecturer_2, 'Java', 8)
student_2.rate_lecturer(lecturer_2, 'Java', 9)
student_2.rate_lecturer(lecturer_1, 'Java', 7)

reviewer_1.rate_hw(student_1, 'Java', 10)
reviewer_1.rate_hw(student_1, 'Java', 8)
reviewer_1.rate_hw(student_2, 'Go', 7)
reviewer_1.rate_hw(student_2, 'Go', 8)
reviewer_1.rate_hw(student_2, 'Java', 9)
reviewer_1.rate_hw(student_2, 'Java', 9)

reviewer_2.rate_hw(student_1, 'Python', 10)
reviewer_2.rate_hw(student_2, 'Python', 8)
reviewer_2.rate_hw(student_1, 'Python', 9)
reviewer_2.rate_hw(student_2, 'Python', 9)
reviewer_2.rate_hw(student_1, 'Python', 10)

print(f'Первый лектор:\n {lecturer_1}')
print()
print(f'Второй лектор:\n {lecturer_2}')
print()
print(f'Первый ревьювер:\n {reviewer_1}')
print()
print(f'Второй ревьювер:\n {reviewer_2}')
print()
print(f'Первый студент:\n {student_1}')
print()
print(f'Второй студент:\n {student_2}')
print()
print(f'Первый студент учится хуже второго? {student_1 < student_2}')
print()
print(f'Средний бал всех студентов по курсу "Java": {average_grade_student([student_1, student_2],"Java")}')
print()
print(f'Средний бал всех лекторов по курсу "Java": {average_grade_lecturer([lecturer_1, lecturer_2],"Java")}')




