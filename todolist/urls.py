from django.urls import path
from . import views


urlpatterns = [
    path('main/', views.lobby, name='lobby'),
    path('', views.lobby),
    path('main/<int:page>', views.lobby, name='lobby_page'),
    path('<int:page>', views.lobby),
    path('create/', views.create, name='create'),
    path('mark/', views.mark, name='mark'),
    path('delete/<int:task_id>', views.delete, name='delete')
]