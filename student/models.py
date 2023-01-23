from django.db import models

# Create your models here.
class Student(models.Model):
    student_name = models.CharField(max_length=36)
    roll_number = models.IntegerField()

    def __str__(self):
        return self.student_name