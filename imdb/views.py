from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import *

# Create your views here.
def index(request):
    context = {
        'best_movies': Movie.objects.order_by('-rating')[:4],
    }
    return render(request, template_name='imdb/index.html', context=context)


class MovieDetail(DetailView):
    model = Movie

    def get_object(self, queryset=None):
        obj = super(MovieDetail, self).get_object(queryset=queryset)
        obj.views += 1
        obj.save()
        return obj


class MovieList(ListView):
    model = Movie
    queryset = Movie.objects.order_by('title')


class TopSevenMovieList(ListView):
    model = Movie
    template_name = 'imdb/top_seven_movies_list.html'
    queryset = Movie.objects.order_by('-rating')[:7]