from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')

def formulario(request):
    return render(request, 'core/formulario.html')