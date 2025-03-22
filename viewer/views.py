from audioop import reverse
from logging import Logger, getLogger

from django.contrib.auth import login
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin

from django.db.models.expressions import result
from django.http import HttpResponse, HttpResponseRedirect
from django.template.context_processors import request
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, FormView, CreateView, UpdateView, DeleteView
from .forms import MovieForm, MovieModelForm, DirectorModelForm
from .models import Genre, Movie,Director
from django.shortcuts import render
from django.views import View


# Create your views here.

LOGGER = getLogger()

def show_movies(request):
    movies = Movie.objects.all()
    return render(
        request=request,
        template_name="movies.html",
        context={"all_movies": movies}
    )


class MovieView(View):
    def get(self, request):
        movies = Movie.objects.all()
        return render(
            request=request,
            template_name="movies.html",
            context={"all_movies": movies}
        )


class MovieTemplateView(TemplateView):
    template_name = "movies.html"
    extra_context = {"all_movies": Movie.objects.all()}


class MovieListView(ListView):
    template_name = "movies.html"
    model = Movie
    context_object_name = "all_movies"


class MovieCreateFormView(FormView):
    template_name = "create_movie.html"
    form_class = MovieForm
    success_url = reverse_lazy("movies")

    def form_valid(self, form):
        if form.is_valid():
            result = super().form_valid(form)
            cleaned_data = form.cleaned_data
            Movie.objects.create(
                title=cleaned_data['title'],
                genre=cleaned_data['genre'],
                ratting=cleaned_data['ratting'],
                released=cleaned_data['released'],
                description=cleaned_data['description']
            )
        return super().form_valid(form)

    def from_invalid(self, form):
        LOGGER.error("Form is not valid")
        return super().form_invalid(form)





class MovieCreateView(LoginRequiredMixin,PermissionRequiredMixin, CreateView):
    template_name = 'create_movie.html'
    form_class = MovieModelForm
    success_url = reverse_lazy('movies')
    permission_required = "viewer.add_movie"



def index(request):
    return render(
        request=request,
        template_name="index.html"
    )


def hello(request, something):
    return HttpResponse(f'Hello {something}!')


def search(request):
    search_param = request.GET.get("search_param")
    return HttpResponse(f"User searched: {search_param}")

@permission_required("view_genre")
@login_required
def get_genrs(request):
    genrs = Genre.objects.all()
    return HttpResponse(genrs)



class DirectorCreateView(CreateView):
    form_class = DirectorModelForm
    template_name = 'create_director.html'
    success_url = reverse_lazy("index")

class DirectorListView(ListView):
    template_name = "directors.html"
    model = Director
    context_object_name = "directors"



class MovieUpdateView(UpdateView):
    template_name = 'create_movie.html'
    form_class = MovieModelForm
    model = Movie
    success_url = reverse_lazy("movies")

class MoviesUpdateSimpleView(View):
    def get(self,request,pk):
        movie = Movie.objects.get(id = pk)
        prefilled_form = MovieModelForm(instance=movie)
        return render(request,template_name="create_movie.html",context={"form":prefilled_form})
    def post(self,request,pk):
        movie = Movie.objects.get(id = pk)
        new_filled_form = MovieModelForm(request.POST,instance=movie)
        if new_filled_form.is_valid():
            new_filled_form.save()

        return HttpResponseRedirect(reverse_lazy("movies"))

class MovieDeleteView(DeleteView):
    template_name = "confirm_delete.html"
    model = Movie
    success_url = reverse_lazy('movies')

class MovieSimpleDeleteView(View):
    def get(self,request,pk):
        movie = Movie.objects.get(id=pk)
        return render(request,template_name="confirm_delete.html",context={"object": movie})
    def post(self,request,pk):
        movie = Movie.ovjects.get(id = pk)
        movie.delete()
        return HttpResponseRedirect(reverse_lazy('movies'))



