# movie/views.py
from django.shortcuts import render
from .models import Movie

def home(request):
    # obtener el término de búsqueda desde ?searchMovie=...
    searchTerm = request.GET.get('searchMovie')

    if searchTerm:
        movies = Movie.objects.filter(title__icontains=searchTerm)
    else:
        movies = Movie.objects.all()

    return render(request, 'movie/home.html', {
        'searchTerm': searchTerm,
        'movies': movies
    })

def about(request):
    # usar plantilla about.html
    return render(request, 'movie/about.html')
