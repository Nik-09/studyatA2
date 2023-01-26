from django.db import models

# Create your models here.
class student(models.Model):
    student_id = models.CharField(max_length=20,primary_key=True)
    student_name = models.CharField(max_length=30)
    student_class = models.IntegerField()
    student_roll = models.IntegerField()
    student_image = models.ImageField(upload_to='upload to/')
    student_username = models.EmailField()
    student_password = models.CharField