from django.urls import path
from . import views
app_name = 'exer_190131'
urlpatterns = [
    path('',views.movielist,name='movielist'),
    path('newmovie',views.newmovie,name='newmovie'),
    path('createmovie',views.createmovie,name='createmovie'),
]

