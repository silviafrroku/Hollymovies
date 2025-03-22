from django.shortcuts import render
from django.template.context_processors import request
from rest_framework.decorators import api_view
from rest_framework.generics import  GenericAPIView
from  rest_framework.mixins import (CreateModelMixin
                                    ,RetrieveModelMixin
                                    ,UpdateModelMixin
                                    ,DestroyModelMixin
                                    ,ListModelMixin)

from api.serializes import MovieReadModelSerializers,  MovieCreateModelSerializers
from viewer.models import Movie


@api_view(['POST','GET'])
def movies(request):
    if request.method == 'POST':
     pass
    elif request.method == 'GET':
     pass




class MovieListCreateView(ListModelMixin,CreateModelMixin,GenericAPIView):
    queryset = Movie.objects.all()
    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return MovieCreateModelSerializers
        elif self.request.method == 'PATCH':
            return MovieReadModelSerializers

    def get(self, request, *args, **kwargs):
        return self.list(request, args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

