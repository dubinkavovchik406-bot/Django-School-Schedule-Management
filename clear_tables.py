import django_SetUp

from my_project.models import Teacher, Subject

Subject.objects.all().delete()

Teacher.objects.all().delete()

