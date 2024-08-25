from django.urls import path, include
from . views import *
from rest_framework.routers import DefaultRouter
from .views import ReviewViewSet




router = DefaultRouter()
router.register(r'reviews', ReviewViewSet, basename='review')


urlpatterns = [
    path('fetch-movies/', MovieViewSet.as_view({'get': 'fetch_movies'})),
    path('', include(router.urls)),
    
]
