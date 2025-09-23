import django_SetUp

from my_project.models import Teacher, Subject

def add_subject(name, teacher_id):
    subject, created = Subject.objects.get_or_create(name=name, teacher_id=teacher_id)
    if created is True:
        print(f"Предмет {name} успішно створений")
    if created is False:
        print(f"Предмет {name} вже існує")
    return subject
