from django.shortcuts import render

def index(request):
    return render(request, 'core.html', {})

def courses(request):
	return render(request, 'cursos.html', {})

# Create your views here.
