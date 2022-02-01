from django.urls import path, include

from .views import index, preStudents
urlpatterns = [
    path('', index, name='home'),
    path('prestudents/', preStudents, name='preStudents'),
]
