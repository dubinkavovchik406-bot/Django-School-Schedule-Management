import django_SetUp

from my_project.models import Teacher, Subject, Student, Class, Schedule, Grade
from datetime import date

def add_subject(name, description):
    subject, created = Subject.objects.get_or_create(name=name, defaults={"description": description})
    if created is True:
        print(f"Предмет {name} успішно створений")
    elif created is False:
        print(f"Предмет {name} вже існує")
    return subject

def delete_subject(name):
    deleted_count, _ = Subject.objects.filter(name=name).delete()
    if deleted_count > 0:
        print(f"Предмет {name} успішно видалений")
    else:
        print(f"Предмет {name} не знайдено")

def update_subject(new_name, subject, new_description=''):
    subject_id = subject.id
    if Subject.objects.filter(name=new_name).exclude(id=subject_id).exists():
        print(f"Предмет з назвою {new_name} вже існує.")
    else:
        updated_count = Subject.objects.filter(id=subject_id).update(name=new_name, description=new_description)
        if updated_count > 0:
            print(f"Предмет з id {subject.id} успішно оновлено")
        else:
            print(f"Предмет з id {subject.id} не знайдено")


def add_teacher(name, surname, subject):
    teacher, created = Teacher.objects.get_or_create(name=name, surname=surname, defaults={"subject": subject})
    if created is True:
        print(f"Вчитель {name} {surname} з предмету {subject} успішно створений")
    elif created is False:
        print(f"Вчитель {name} {surname} з предмету {subject} вже існує")
    return teacher

def add_student(name, surname, student_class):
    student, created = Student.objects.get_or_create(name=name, surname=surname, defaults={"student_class": student_class})
    if created is True:
        print(f"Студент {name} {surname} з классу {student_class} успішно створений")
    elif created is False:
        print(f"Студент {name} {surname} з классу {student_class} вже існує")
    return student


def add_my_class(name, year_of_study):
    my_class, created = Class.objects.get_or_create(name=name, defaults={"year_of_study": year_of_study})
    if created is True:
        print(f"Класс {name} успішно створений")
    elif created is False:
        print(f"Класс {name} вже існує")
    return my_class

def delete_class(name):
    deleted_count, _ = Class.objects.filter(name=name).delete()
    if deleted_count > 0:
        print(f"Клас {name} успішно видалений")
    else:
        print(f"Клас {name} не знайдено")

def update_class(new_name, new_year_of_study, my_class):
    my_class_id = my_class.id
    if Class.objects.filter(name=new_name).exclude(id=my_class_id).exists():
        print(f"Класс з назвою {new_name} вже існує.")
    else:
        updated_count = Class.objects.filter(id=my_class_id).update(name=new_name, year_of_study=new_year_of_study)
        if updated_count > 0:
            print(f"Класс з id {my_class_id} успішно оновлено")
        else:
            print(f"Класс з id {my_class_id} не знайдено")


def add_schedule_entry(day_of_week, start_time, subject, schedule_class, teacher):
    schedule, created = Schedule.objects.get_or_create(day_of_week=day_of_week, start_time=start_time,
                                                       schedule_class=schedule_class,
                                                       defaults={"subject": subject, "teacher": teacher})
    if created is True:
        print(f"Розклад у день {day_of_week} о {start_time} з предметом {subject} для классу {schedule_class} який веде вчитель {teacher} успішно створений")
    elif created is False:
        print(f"Розклад у {day_of_week} о {start_time} з предметом {subject}, классом {schedule_class} який веде вчитель {teacher} вже існує")
    return schedule

def add_grade(grade_value, date_str, student, subject):
    try:
        grade_date = date.fromisoformat(date_str)
    except ValueError:
        print("Введіть дату у форматі YYYY-MM-DD")
        return None
    grade = Grade.objects.create(grade_value=grade_value, date=grade_date, subject=subject, student=student)
    print(f"Оцінка {grade_value}, учня {student} з предмета {subject} о {grade_date} успішно створений")

    return grade


flag = True
print("Write 0 if you want to break cycle")
print("Write 1 if you want to add new subject")
print("Write 2 if you want to add new class")
print("Write 3 if you want to add new teacher")
print("Write 4 if you want to add new student ")
print("Write 5 if you want to add new schedule")
print("Write 6 if you want to add new grade ")

while flag is True:
    question = int(input("Write the operation number"))

    if question == 0:
        print("You break the cycling")
        flag = False


    elif question == 1:
        my_name = input("Write the name of your subject")
        my_description = input("Write the description of your subject")
        add_subject(name=my_name, description=my_description)

    elif question == 2:
        my_name = input("Write the name of your class")
        my_year_of_study = int(input("Write the year of study of your class"))
        add_my_class(my_name, my_year_of_study)

    elif question == 3:
        my_name = input("Write the name of your teacher")
        my_surname = input("Write the surname of your teacher")
        name_of_the_subject = input("Write the name of your teacher's subject")

        my_subject = Subject.objects.get(name=name_of_the_subject)
        add_teacher(name=my_name, surname=my_surname, subject=my_subject)

    elif question == 4:
        my_name = input("Write the name of your student")
        my_surname = input("Write the surname of your student")
        name_of_the_class = input("Write the name of your student's class")

        my_student_class = Class.objects.get(name=name_of_the_class)
        added_student = add_student(name=my_name, surname=my_surname, student_class=my_student_class)


