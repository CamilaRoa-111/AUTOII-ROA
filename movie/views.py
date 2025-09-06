from django.shortcuts import render

def home(request):
    # Diccionario con datos que queremos pasar a la plantilla
    context = {'name': 'Greg Lim'}
    return render(request, 'movie/home.html', context)

def about(request):
    return render(request, 'movie/about.html')


# Create your views here.
