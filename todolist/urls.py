from django.urls import path
from . import views


urlpatterns = [
    path('main/', views.lobby, name='lobby'),
    path('', views.lobby),
    path('search/', views.search, name='search')
]