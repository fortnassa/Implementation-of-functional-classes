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
            if grade in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Ошибка"

    def average_rating(self):
        total_rating = 0
        total_count = 0

        for grades in self.grades.values():
            total_rating += sum(grades)
            total_count += len(grades)

            if total_rating == 0:
                return 0.0
            else:
                return total_rating/total_count

    def __eq__(self, other):
        return self.average_rating() == other.avarage_rating()

    def __ne__(self, other):
        return self.average_rating() != other.avarage_rating()

    def __lt__(self, other):
        return self.average_rating() < other.avarage_rating()

    def __le__(self, other):
        return self.average_rating() <= other.avarage_rating()

    def __str__(self):
        return f'Имя: {self.name}\n Фамилия: {self.surname}\n Средняя оценка за домшнее задание: {self.grades}\n Курсы в процессе изучения: {self.courses_in_progress}\n Завершенные курсы: {self.finished_courses}'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

    def add_grade(self, course, grade):
        if course not in self.grades:
            self.grades[course] = []
        self.grades[course].append(grade)

    def average_rating(self):
        total_rating = 0
        total_count = 0

        for grades in self.grades.values():
            total_rating += sum(grades)
            total_count += len(grades)
        if total_rating == 0:
            return 0.0
        else:
            return total_rating/total_count

    def __eq__(self, other):
        return self.average_rating() == other.avarage_rating()

    def __ne__(self, other):
        return self.average_rating() != other.avarage_rating()

    def __lt__(self, other):
        return self.average_rating() < other.avarage_rating()

    def __le__(self, other):
        return self.average_rating() <= other.avarage_rating()

    def __str__(self):
        return f'Имя: {self.name}\n Фамилия: {self.surname}\n Средняя оценка за лекции: {self.courses_attached}'


class Reviewer(Mentor):
    def __init__(self, name, surname, courses_attached):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.course_in_progress:
            if grade in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return "Ошибка"

    def __str__(self):
        return f'Имя: {self.name}\n Фамилия: {self.surname}'



student1 = Student('Chandler', 'Bings', 'man')
student1.finished_courses += ['Основы языка программирования Python']
student1.courses_in_progress += ['ООП и работа с API']
student1.grades['Основы языка программирования Python'] = [9, 10, 9, 8]
student1.grades['ООП и работа с API'] = [8, 10]

student2 = Student('Monica', 'Bing', 'woman')
student2.finished_courses += ['ООП и работа с API']
student2.courses_in_progress += ['Git']
student2.grades['ООП и работа с API'] = [10, 10, 10, 9]
student2.grades['Git'] = [10, 10]


print(student1.name)
print(student2.name)
print(student1.gender)
print(student2.gender)
print(student1.finished_courses)
print(student2.finished_courses)
print(student1.courses_in_progress)
print(student2.courses_in_progress)
print(student1.grades)
print(student2.grades)
print(student1.average_rating())
print(student2.average_rating())

if student1 > student2:
    print(f'Студент {student1} учится лучше, чем {student2}')
else:
    print(f'Студент {student2} учится лучше, чем {student1}')

mentor1 = Mentor('Sheldon' 'Cooper')
mentor1.courses_attached += []

mentor2 = Mentor('Thomas', 'Shelby')
mentor2.courses_attached += []

print(mentor1.name)
print(mentor2.name)
print(mentor1.surname)
print(mentor2.surname)
print(mentor1.courses_attached)
print(mentor2.courses_attached)

lecturer1 = Lecturer('Ted', 'Mosbey')
lecturer1.courses_attached += []
lecturer1.grades += {}

lecturer2 = Lecturer ('Bruce', 'Banner')
lecturer2.courses_attached += []
lecturer2.grades += {}

print(lecturer1.name)
print(lecturer2.name)
print(lecturer1.surname)
print(lecturer2.surname)
print(lecturer1.courses_attached)
print(lecturer2.courses_attached)
print(lecturer1.grades)
print(lecturer2.grades)
print(lecturer1.average_rating())
print(lecturer2.average_rating())

reviewer1 = Reviewer('Cameron', 'Diaz')
reviewer1.rate_hw(student2)

reviewer2 = Reviewer('Solomon', 'Grandy')
reviewer2.rate_hw(student1)

print(reviewer1.name)
print(reviewer2.name)
print(reviewer1.surname)
print(reviewer2.surname)
print(reviewer1.rate_hw(student1))
print(reviewer2.rate_hw(student2))

def all_students_rate(student_list, course_name):
    some_list = []
    sum_ = 0
    count = 0
    for student_hw in students_list:
        for k,v in rate_hw.grades.items():
            if k == course_name:
                some_list.append(value)
        for i in some_list:
            for n in i:
                sum_ += n
                count += 1
        avg_rating_all = sum_/ count
        return avg_rating_all

def all_lecturer_rate(lecturer_list, course_name):
    some_list = []
    sum_ = 0
    count = 0

    for lecturer_lection in lecturer_list:
        for k,v in rate_lecturer:
            if k == course_name:
                some_list.append(value):
                for i in some_list:
                    for n in i:
                        sum_ += n
                        count += 1
                        avg_rating_all_lecturer = sum_/count
                return avg_rating_all_lecturer



