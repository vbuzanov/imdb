from django.urls import path
from . import views

app_name = "imdb"

urlpatterns = [
    path('', views.index, name='index'),
    path('movie/<slug:slug>/', views.MovieDetail.as_view(), name='movie-detail'),
    path('movies/', views.MovieList.as_view(), name='movie-list'),
    path('movies/top_seven/', views.TopSevenMovieList.as_view(), name='top-seven-movies-list'),
]