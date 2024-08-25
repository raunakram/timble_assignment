from rest_framework import serializers
from .models import Movie, Genre, Review

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['name']

class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)

    class Meta:
        model = Movie
        fields = ['title', 'description', 'release_date', 'genres', 'poster_path']


class ReviewSerializer(serializers.ModelSerializer):

    movie = serializers.PrimaryKeyRelatedField(queryset=Movie.objects.all())
    class Meta:
        model = Review
        fields = ['id', 'movie', 'user', 'rating', 'comment', 'created_at', 'updated_at']
        
