from django.urls import path
from . import views

urlpatterns = [
    path('<int:query>', views.index, name='index'),
]