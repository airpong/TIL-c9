from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('<int:food_id>/delete',views.delete,name='delete'),
    path('<int:food_id>/edit',views.update,name='update'),
    path('<int:food_id>',views.detail,name='detail'),
    path('create/<str:category>',views.create,name='create'),
    path('',views.index,name='index'),
]