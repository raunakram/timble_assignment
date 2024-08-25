from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
import requests
from .models import Movie, Genre
from .serializers import MovieSerializer
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from .models import Review
from .serializers import ReviewSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .pagination import StandardResultsSetPagination
from rest_framework import serializers
from rest_framework.exceptions import ValidationError



API_KEY = '103392435a661a565bec2c869cd4bdaf'
URL = 'https://api.themoviedb.org/3/discover/movie'

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['genres', 'release_date']  # Fields you want to filter by
    search_fields = ['title', 'description']  # Fields you want to search by
    pagination_class = StandardResultsSetPagination

    @action(detail=False, methods=['get'], url_path='fetch-movies')
    def fetch_movies(self, request):
        response = requests.get(URL, params={'api_key': API_KEY})
        data = response.json()
        # print(data, "data------------------->>>>>>>>>>>")
        for movie_data in data['results']:
            title = movie_data['title']
            description = movie_data['overview']
            release_date = movie_data['release_date']
            poster_path = movie_data['poster_path']

            movie, created = Movie.objects.get_or_create(
                title=title,
                defaults={
                    'description': description,
                    'release_date': release_date,
                    'poster_path': f"https://image.tmdb.org/t/p/w500{poster_path}"
                }
            )

            genre_ids = movie_data['genre_ids']
            for genre_id in genre_ids:
                genre_name = self.get_genre_name(genre_id)
                genre, _ = Genre.objects.get_or_create(name=genre_name)
                movie.genres.add(genre)

        return Response({"status": "Movies fetched successfully!"})

    def get_genre_name(self, genre_id):
        genre_map = {
            28: 'Action',
            35: 'Comedy',
            878: 'Science Fiction',
            16: 'Animation',
            10751: 'Family',
            12: 'Adventure',
            80: 'Crime',
            53: 'Thriller',
            18: 'Drama',
            10749: 'Romance',
            27: 'Horror',
        }
        return genre_map.get(genre_id, 'Unknown')






class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated] 
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['movie', 'rating']  # Fields you want to filter by
    search_fields = ['comment', 'movie__title']  # Fields you want to search by
    pagination_class = StandardResultsSetPagination

    def perform_create(self, serializer):
        # Ensure the movie ID is provided and valid
        movie_id = self.request.data.get('movie')
        if not movie_id:
            raise ValidationError("Movie ID is required.")

        # Validate that the movie exists
        if not Movie.objects.filter(id=movie_id).exists():
            raise ValidationError("Invalid movie ID.")
        
        # Save the review with the current user
        serializer.save(user=self.request.user)

    def get_queryset(self):
        # Filter the reviews by the current logged-in user
        user = self.request.user
        if user.is_authenticated:
            return Review.objects.filter(user=user)
        return Review.objects.none()
