from django.core.management.base import BaseCommand
from movie.models import Movie
import json
import os

class Command(BaseCommand):
    help = 'Carga películas desde un archivo JSON a la base de datos'

    def handle(self, *args, **kwargs):
        # Ruta del archivo JSON
        file_path = os.path.join('movie', 'management', 'commands', 'movies.json')

        # Leer el archivo JSON
        with open(file_path, encoding='utf-8') as json_file:
            movies_data = json.load(json_file)

            # Cargar máximo 100 registros para evitar exceso
            for movie in movies_data[:100]:
                title = movie.get('title', 'Sin título')
                description = movie.get('description', 'Sin descripción')
                genre = movie.get('genre', 'Desconocido')
                year = movie.get('year', 0)

                # Crear cada película en la base de datos
                Movie.objects.create(
                    title=title,
                    description=description,
                    genre=genre,
                    year=year,
                    image='movie/images/default.jpg'
                )

        self.stdout.write(self.style.SUCCESS('✅ Películas cargadas exitosamente a la base de datos'))
