from django.urls import path, include

from .views import index, preStudents, quotas, programs, ads, ad, department

urlpatterns = [
    path('', index, name='home'),
    path('prestudents/', preStudents, name='preStudents'),
    path('quotas/', quotas, name='quotas'),
    path('programs/', programs, name='programs'),
    path('ads/', ads, name='ads'),
    path('ad/<int:pk>', ad, name="ad"),
    path('department/', department, name="department"),
]
