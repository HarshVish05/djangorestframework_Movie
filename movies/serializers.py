# serializers - It allows complex data such as query sets, model instances to be converted 
#               to native python datatypes that can be easily rendered into formats like JSON or XML.

from .models import MovieData
from rest_framework import serializers


class MovieSerializers(serializers.ModelSerializer):
    image = serializers.ImageField(use_url = True)
    class Meta:
        model = MovieData
        fields = ['id', 'name', 'duration', 'rating', 'genre', 'image']