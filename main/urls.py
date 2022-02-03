from django.urls import path, include

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('enrollee/', enrollee, name='enrollee'),
    path('quotas/', quotas, name='quotas'),
    path('programs/', programs, name='programs'),
    path('ads/', ads, name='ads'),
    path('ad/<int:pk>', ad, name="ad"),
    path('central_department/', central_department, name="central_department"),
    path('department/', department, name="department"),
    path('management/', management, name="management"),
    path('external_department/', external_department, name="external_department"),
]
