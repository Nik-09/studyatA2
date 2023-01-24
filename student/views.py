from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

# Create your views here.
def home(request):
    return render(request, 'home.html')

def student_dashboard(request):
    return render(request, 'student-dashboard.html')