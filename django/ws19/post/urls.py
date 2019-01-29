from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('new/',views.new),
    path('',views.index),
    path('create/',views.create),
    path('<int:student_id>/',views.detail),
    path('<int:student_id>/delete/',views.delete),
    path('<int:student_id>/update/',views.update),
    path('<int:student_id>/confirm/',views.confirm),
    path('search/',views.search),
    path('<str:student_name>/postit/',views.postit),
    path('<str:student_name>/messageconfirm/',views.messageconfirm),
]