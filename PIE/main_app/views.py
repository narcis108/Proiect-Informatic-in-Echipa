from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views.generic.edit import UpdateView

from main_app.forms import InsertFilmFromURLForm
from main_app.models import Film, Actor, Regizor
from main_app.utils import query_tmdb
from .forms import SignUpForm
from .models import Utilizator

base_img_url = 'https://image.tmdb.org/t/p/'
width = 'w185/'


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def InsertFilmFromURL(request):
    result = []
    if request.method == 'POST':
        form = InsertFilmFromURLForm(request.POST)
        if form.is_valid():
            result = query_tmdb(form.cleaned_data['url_IMDB'])
            dict = result['movie_results'][0]
            image_path = '%s%s' % (base_img_url, width)
            for key, value in dict.items():
                print(key, ' : ', value)
            film = Film(titlu=dict['title'],
                        descriere=dict['overview'],
                        data_lansare=dict['release_date'],
                        rating=dict['vote_average'],
                        link_IMDB=form.cleaned_data['url_IMDB'],
                        link_Youtube=form.cleaned_data['url_IMDB'],
                        imagine='%s%s' % (image_path, dict['poster_path']))
            film.save()
            return render(request, 'index.htm', {'form': form, 'result': result, 'film': film})
    else:
        form = InsertFilmFromURLForm()

    return render(request, 'adauga.html', {'form': form, 'result': result})


def home(request):
    filme = Film.objects.all()
    film = Film.objects.first()
    return render(request, 'index.htm', {'filme': filme, 'current_film' : film})


def my_account(request):
    return render(request, 'my_account.html')


def process_film(request):
    filme = Film.objects.all()
    film = Film.objects.last()
    print(film)
    return render(request, 'index.htm', {'filme': filme, 'current_film': film})


class AccountUpdate(UpdateView):
    model = Utilizator
    fields = ('first_name', 'last_name', 'data_nasterii', 'gender',)
    context_object_name = 'accountUpdate'
    template_name = 'update_account.html'

    def form_valid(self, form):
        user = form.save()
        user.save()
        return redirect('myAccount')
