from django.db import models

# Create your models here.
from django.urls import reverse


class Director(models.Model):
    first = models.CharField(max_length=128)
    last = models.CharField(max_length=128)
    portrait = models.ImageField(upload_to='directors/', null=True, blank=True)

    def __str__(self):
        return f'{self.first} {self.last}'

class Movie(models.Model):
    title = models.CharField(max_length=128)
    year = models.IntegerField(null=True, blank=True)
    rating = models.FloatField(default=4.0)
    views = models.IntegerField(default=0)
    poster = models.ImageField(upload_to='posters/', null=True, blank=True)
    plot = models.FileField(upload_to="plots/", null=True, blank=True)
    director = models.ForeignKey(Director, on_delete=models.SET_NULL, related_name="movies", null=True, blank=True)
    trailer = models.CharField(max_length=11, null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.title

    def url(self):
        return reverse('imdb:movie-detail', kwargs={'slug': self.slug})