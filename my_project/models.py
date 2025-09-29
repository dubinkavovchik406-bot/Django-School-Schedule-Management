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

class Schedule(models.Model):
    day_of_week = models.CharField(max_length=100)
    start_time = models.TimeField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    schedule_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.day_of_week}, {self.start_time}"

class Grade(models.Model):
    grade_value = models.IntegerField()
    date = models.DateField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.grade_value}, {self.date}"
