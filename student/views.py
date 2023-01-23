from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

# Create your views here.
def index(request, query):
    students = Student.objects.all()
    for student in students:
        print(student.student_name)
    print(len(students))
    print(query)
    return HttpResponse("Hello, world. You're at the polls index.")