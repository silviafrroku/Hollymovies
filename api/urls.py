from django.urls import path
from .views import MovieListCreateView  # Sigurohu që është importuar saktë

urlpatterns = [
    path('movies/', MovieListCreateView.as_view(), name='api-movies'),
]
