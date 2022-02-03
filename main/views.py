from django.shortcuts import render
from .models import PreStudents, Questions, Quotas, Programs, Ads, Ad, Department

# Create your views here.
def index(request):
    return render(request, 'index.html')

def preStudents(request):
    content = PreStudents.objects.all();
    return render(request, 'preStudens.html', {'content': content})

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

def department(request):
    content = Department.objects.all()
    return render(request, 'department.html', {'content': content})

