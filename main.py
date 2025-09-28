import django_SetUp

from my_project.models import Teacher, Subject, Student, Class

def add_subject(name, description):
    subject, created = Subject.objects.get_or_create(name=name, defaults={"description": description})
    if created is True:
        print(f"Предмет {name} успішно створений")
    elif created is False:
        print(f"Предмет {name} вже існує")
    return subject

def add_teacher(name, surname, subject):
    teacher, created = Teacher.objects.get_or_create(name=name, surname=surname, defaults={"subject": subject})
    if created is True:
        print(f"Вчитель {name} успішно створений")
    elif created is False:
        print(f"Вчитель {name} вже існує")
    return teacher

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

def add_my_class(name, year_of_study):
    my_class, created = Class.objects.get_or_create(name=name, defaults={"year_of_study": year_of_study})
    if created is True:
        print(f"Класс {name} успішно створений")
    elif created is False:
        print(f"Класс {name} вже існує")
    return my_class

def add_student(name, surname, student_class):
    student, created = Student.objects.get_or_create(name=name, surname=surname, defaults={"student_class": student_class})
    if created is True:
        print(f"Студент {name} успішно створений")
    elif created is False:
        print(f"Студент {name} вже існує")
    return student

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

