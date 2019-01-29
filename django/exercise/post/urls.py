from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('new/',views.new),
    path('create/',views.create),
    path('<int:post_id>/',views.detail),
    path('<int:post_id>/delete/',views.delete),
    path('<int:post_id>/edit/',views.edit),
    path('<int:post_id>/confirm/',views.confirm),
]
