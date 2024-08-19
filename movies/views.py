from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MovieSerializers
from .models import MovieData

# Create your views here.

class MoviewViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.all()
    serializer_class = MovieSerializers
    
class ActionViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(genre = 'action')
    serializer_class = MovieSerializers
    
class ComedyViewSet(viewsets.ModelViewSet):
    # If you want to make the filter case-insensitive, you can use the iexact lookup, which performs a case-insensitive match
    queryset = MovieData.objects.filter(genre__iexact = 'comedy')
    serializer_class = MovieSerializers
