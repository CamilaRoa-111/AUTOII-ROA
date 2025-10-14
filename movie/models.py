from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='movie/images/', default='movie/images/default.jpg')
    genre = models.CharField(max_length=50, default='Unknown')
    year = models.IntegerField(default=0)

    def __str__(self):
        return self.title




