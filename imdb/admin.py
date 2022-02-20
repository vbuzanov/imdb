from django.contrib import admin
from .models import *

# Register your models here.


class MoviesInline(admin.TabularInline):
    model = Movie


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    inlines = [MoviesInline]


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title', 'year']}
    list_display = ['title', 'year', 'director', 'rating']
    list_filter = ['title', 'year', 'rating']