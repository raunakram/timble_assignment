from rest_framework.pagination import PageNumberPagination
from .models import Movie, Genre, Review
from .serializers import ReviewSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import MovieSerializer
from rest_framework import viewsets, permissions, filters
from rest_framework.permissions import IsAuthenticated

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 1 
    page_size_query_param = 'page_size'
    max_page_size = 100

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['genres', 'release_date']
    search_fields = ['title', 'description']
    pagination_class = StandardResultsSetPagination

    

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['movie', 'rating']
    search_fields = ['comment', 'movie__title']
    pagination_class = StandardResultsSetPagination

    
