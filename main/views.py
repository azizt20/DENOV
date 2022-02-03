from django.shortcuts import render
from .models import *


def index(request):
    return render(request, 'index.html')


def enrollee(request):
    content = Enrollee.objects.all()
    return render(request, 'enrollee.html', {'content': content})


def quotas(request):
    content = Quotas.objects.all()
    return render(request, 'quotas.html', {'content': content})


def programs(request):
    content = Programs.objects.all()
    return render(request, 'programs.html', {'content': content})


def ads(request):
    content = Ads.objects.all()
    return render(request, 'ads.html', {'content': content})


def ad(request, pk):
    content = Ad.objects.get(id=pk)
    return render(request, 'ad.html', {'c': content})


def central_department(request):
    content = CentralDepartments.objects.all()
    return render(request, 'central-department.html', {'content': content})


def department(request):
    content = Departments.objects.all()
    return render(request, 'department.html', {'content': content})


def management(request):
    content = Management.objects.all()
    return render(request, 'management.html', {'content': content})


def external_department(request):
    content = ExternalDepartment.objects.all()
    return render(request, 'external-department.html', {'content': content})

