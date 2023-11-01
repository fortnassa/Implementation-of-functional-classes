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
                lecturer.grades[course] += [grade] #реализация закрепленного кура за Лекторами, для того что бы осуществить проверку оценок
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
        #нужно пройтись по списку используя for или list comprehension
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
        super().__init__(name, surname, courses_attached)

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


# def avg_courses(students_name, course_name):
#     if
student1 = Student('Chandler', 'Bings', 'man')
student1.finished_courses += ['Основы языка программирования Python']
student1.courses_in_progress += ['ООП и работа с API']
student1.grades['Основы языка программирования Python'] = [9, 10, 9, 8]
student1.grades['ООП и работа с API'] = [8, 10]

print(student1.name)
print(student1.gender)
print(student1.finished_courses)
print(student1.courses_in_progress)
print(student1.grades)
# best_student = Student('Ruoy', 'Eman', 'your_gender')
# best_student.finished_courses += ['Git']
# best_student.courses_in_progress += ['Python']
# best_student.grades['Git'] = [10, 10, 10, 10, 10]
# best_student.grades['Python'] = [10, 10]
#
# print(best_student.finished_courses)
# print(best_student.courses_in_progress)
# print(best_student.grades)
#
# cool_mentor = Mentor('Some', 'Buddy')
# cool_mentor.courses_attached += ['Python']
# print(cool_mentor.courses_attached)
#
# best_student = Student('Ruoy', 'Eman', 'your_gender')
# best_student.courses_in_progress += ['Python']
#
# cool_mentor = Mentor('Some', 'Buddy')
# cool_mentor.courses_attached += ['Python']
#
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
#
# print(best_student.grades)


