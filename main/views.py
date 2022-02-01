from django.shortcuts import render
from .models import PreStudents, Questions

# Create your views here.
def index(request):
    return render(request, 'index.html')

def preStudents(request):
    content = PreStudents.objects.all()
    return render(request, 'preStudens.html', {'content': content})