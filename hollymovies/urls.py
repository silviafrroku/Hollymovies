"""
URL configuration for hollymovies project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from xml.etree.ElementInclude import include

from django.contrib import admin

from authentication.models import CustomUser
from viewer.admin import MovieAdmin
from viewer.models import Genre, Movie  # ✅ Correct if Genre is inside viewer app
from viewer.views import DirectorCreateView, show_movies, MovieView, MovieTemplateView, hello, search, get_genrs, \
    MovieDeleteView, MovieUpdateView, DirectorListView, MovieCreateView, index

from authentication.views import CustomRegistrationView, CustomLoginView, CustomLogoutView

# Avoid duplicate registration error
from django.contrib.admin.sites import AlreadyRegistered

try:
    admin.site.register(Genre)
    admin.site.register(CustomUser)
except AlreadyRegistered:
    pass





from django.urls import path,include



urlpatterns = [
    path('admin/', admin.site.urls),

    path("index/", index,name = "index"),

    path("movies/",show_movies,name = "movies"), # Function based view
    path("movies/",MovieView.as_view,name = "movies"),# CLASS BASED VIEW
    path("movies/",MovieTemplateView.as_view,name = "movies"),# class templateview
    path("movies/", MovieTemplateView.as_view(), name="movies"),

    path("index/<something>", hello),

    path("index/search/", search),

    path("genres/", get_genrs),

    path("movies/create/", MovieCreateView.as_view(), name='movie-create'),

    path("directors/create/", DirectorCreateView.as_view(), name = 'director-create'),

    path("directors/", DirectorListView.as_view(), name = 'directors'),

    path("movies/<pk>/edit/", MovieUpdateView.as_view(), name='movie-update'),

    path("movies/<pk>/delete/", MovieDeleteView.as_view(), name='movie-delete'),

    path("auth/register/",CustomRegistrationView.as_view(),name = 'user-register'),

    path("auth/login/",CustomLoginView.as_view(),name = 'user-login'),

    path("auth/logout/",CustomLogoutView.as_view(),name = 'user-logout'),

    path('api/', include('api.urls'))


]
