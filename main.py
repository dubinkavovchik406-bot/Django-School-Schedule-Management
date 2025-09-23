import django_SetUp

from my_project.models import Teacher, Subject

def add_subject(name, teacher_id):
    subject, created = Subject.objects.get_or_create(name=name, teacher_id=teacher_id)
    if created is True:
        print(f"Предмет {name} успішно створений")
    elif created is False:
        print(f"Предмет {name} вже існує")
    return subject

def add_teacher(name):
    teacher, created = Teacher.objects.get_or_create(name=name)
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

def update_subject(new_name, subject_id):
    if Subject.objects.filter(name=new_name).exclude(id=subject_id).exists():
        print(f"Предмет з назвою {new_name} вже існує.")
    else:
        updated_count = Subject.objects.filter(id=subject_id).update(name=new_name)
        if updated_count > 0:
            print(f"Предмет з id {subject_id} успішно оновлено")
        else:
            print(f"Предмет з id {subject_id} не знайдено")


created_teacher = add_teacher("Ілля")
created_subject = add_subject("Математика", created_teacher.id)
update_subject("Фізика", created_subject.id)
