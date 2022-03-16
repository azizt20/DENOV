from django.shortcuts import render
from .models import *


def home(request):
    facultets = Facultets.objects.all()
    news = New.objects.all()
    return render(request, 'index.html', {'facultets': facultets, 'news': news})


def enrollee(request):
    content = Enrollee.objects.all()
    return render(request, 'enrollee.html', {'content': content})


def quotas(request):
    content = Quotas.objects.all()
    return render(request, 'quotas.html', {'content': content})


def finans(request):
    content = Quotas.objects.all()
    return render(request, 'finans.html', {'content': content})


def programs(request):
    content = Programs.objects.all()
    return render(request, 'programs.html', {'content': content})


def spirtual_education(request):
    content = SpirtualEducation.objects.all()
    return render(request, 'spiritual-education.html', {'content': content})


def ads(request):
    content = AdsCategory.objects.all()
    return render(request, 'ads.html', {'content': content})


def ad(request, pk):
    content = Ad.objects.get(id=pk)
    category = AdsCategory.objects.get(id=content.ad_id)
    return render(request, 'ad.html', {'c': content, 'category': category})


def ads_category(request, pk):
    content = AdsCategory.objects.get(id=pk)
    return render(request, 'ads-category.html', {'category': content})


def news(request):
    content = NewsCategory.objects.all()
    return render(request, 'news.html', {'content': content})


def new(request, pk):
    content = New.objects.get(id=pk)
    category = NewsCategory.objects.get(id=content.new_id)
    return render(request, 'new.html', {'c': content, 'category': category})


def news_category(request, pk):
    content = NewsCategory.objects.get(id=pk)
    return render(request, 'news-category.html', {'category': content})


def central_department(request):
    content = CentralDepartments.objects.all()
    return render(request, 'central-department.html', {'content': content})


def facultets(request):
    content = Facultets.objects.all()
    return render(request, 'facultets.html', {'content': content})


def science(request):
    content = Science.objects.all()
    return render(request, 'science.html', {'content': content})


def magistr(request):
    content = Magistr.objects.all()
    return render(request, 'magistr.html', {'content': content})


def fotos(request):
    content = FotoCategory.objects.all()
    return render(request, 'fotos.html', {'content': content})


def foto(request, pk):
    content = FotoCategory.objects.get(id=pk)
    return render(request, 'foto.html', {'content': content})


def international_relationships(request):
    content = InternationalRelationships.objects.all()
    return render(request, 'international-relationships.html', {'content': content})


def regulations(request):
    content = Regulations.objects.all()
    return render(request, 'regulations.html', {'content': content})


def decree(request):
    content = Decree.objects.all()
    return render(request, 'decree.html', {'content': content})


def department(request):
    content = Departments.objects.all()
    return render(request, 'department.html', {'content': content})


def management(request):
    content = Management.objects.all()
    return render(request, 'management.html', {'content': content})


def external_department(request):
    content = ExternalDepartment.objects.all()
    return render(request, 'external-department.html', {'content': content})
