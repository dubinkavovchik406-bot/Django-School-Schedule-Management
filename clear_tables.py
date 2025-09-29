import django_SetUp

from my_project.models import Subject, Class

Subject.objects.all().delete()
Class.objects.all().delete()
