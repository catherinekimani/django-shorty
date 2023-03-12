from django.urls import path
from .views import index, create_short_url, redirect_original

urlpatterns = [
    path('', index, name='index'),
    path('create/', create_short_url, name='create_short_url'),
    path('<str:shortened_url>/', redirect_original, name='redirect_original'),
]
