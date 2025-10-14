# movie/views.py
from django.shortcuts import render
from django.db.models import Count
from .models import Movie
import matplotlib
matplotlib.use('Agg')  # Usar backend no interactivo (necesario en Django)
import matplotlib.pyplot as plt
import io, base64

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def statistics(request):
    # Agrupar películas por año
    data = Movie.objects.values('year').annotate(count=Count('id')).order_by('year')

    # Preparar listas para la gráfica
    years = []
    counts = []

    for row in data:
        year = row['year'] if row['year'] is not None else 'Desconocido'
        years.append(str(year))
        counts.append(row['count'])

    # Crear la gráfica
    plt.figure(figsize=(10, 6))
    plt.bar(years, counts, color='skyblue', width=0.6)
    plt.title('Movies per year')
    plt.xlabel('Year')
    plt.ylabel('Number of movies')
    plt.xticks(rotation=90)
    plt.tight_layout()

    # Guardar la imagen en memoria y convertir a base64
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    plt.close()

    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')

    return render(request, 'movie/statistics.html', {'graphic': graphic})

def statistics_genre(request):
    from django.db.models import Count
    from .models import Movie
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    import io, base64

    # Agrupar películas por género
    data = Movie.objects.values('genre').annotate(count=Count('id')).order_by('-count')

    genres = [row['genre'] if row['genre'] else 'Desconocido' for row in data]
    counts = [row['count'] for row in data]

    # Crear la gráfica
    plt.figure(figsize=(10, 6))
    plt.barh(genres, counts, color='lightcoral')
    plt.title('Movies per genre')
    plt.xlabel('Number of movies')
    plt.ylabel('Genre')
    plt.tight_layout()


    # Convertir a imagen base64
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    graphic = base64.b64encode(buffer.getvalue()).decode('utf-8')
    buffer.close()
    plt.close()

    return render(request, 'movie/statistics_genre.html', {'graphic': graphic})

def statistics_combined(request):
    from django.db.models import Count
    from .models import Movie
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    import io, base64

    # --- 1. Datos por año ---
    data_year = Movie.objects.values('year').annotate(count=Count('id')).order_by('year')
    years = [str(row['year']) if row['year'] else 'Desconocido' for row in data_year]
    count_years = [row['count'] for row in data_year]

    # --- 2. Datos por género ---
    data_genre = Movie.objects.values('genre').annotate(count=Count('id')).order_by('-count')
    genres = [row['genre'] if row['genre'] else 'Desconocido' for row in data_genre]
    count_genres = [row['count'] for row in data_genre]

    # --- 3. Crear figura con dos subgráficas ---
    plt.figure(figsize=(14, 6))

    # Gráfica 1: películas por año
    plt.subplot(1, 2, 1)
    plt.bar(years, count_years, color='skyblue')
    plt.title('Movies per Year')
    plt.xlabel('Year')
    plt.ylabel('Number of movies')
    plt.xticks(rotation=90)

    # Gráfica 2: películas por género
    plt.subplot(1, 2, 2)
    plt.barh(genres, count_genres, color='lightcoral')
    plt.title('Movies per Genre')
    plt.xlabel('Number of movies')
    plt.ylabel('Genre')

    plt.tight_layout()

    # --- 4. Convertir la figura en imagen base64 ---
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    graphic = base64.b64encode(buffer.getvalue()).decode('utf-8')
    buffer.close()
    plt.close()

    return render(request, 'movie/statistics_combined.html', {'graphic': graphic})