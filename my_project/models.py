from django.db import models

# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=100, default="")
    description = models.TextField(default="")

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=100, default="")
    surname = models.CharField(max_length=100, default="")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}, {self.surname}"


class Class(models.Model):
    name = models.CharField(max_length=100, default="")
    year_of_study = models.IntegerField(default=2000)

    def __str__(self):
        return f"{self.name}, {self.year_of_study}"

class Student(models.Model):
    name = models.CharField(max_length=100, default="")
    surname = models.CharField(max_length=100, default="")
    student_class = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}, {self.surname}"
