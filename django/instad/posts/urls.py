from django.urls import path
from . import views
app_name = 'posts'

urlpatterns = [
    path('<str:username>/',views.list,name='list'),
    path('<str:username>/create/',views.create,name='create'),
    path('<str:username>/<int:post_id>/update/',views.update, name='update'),
    path('<str:username>/<int:post_id>/delete/',views.delete,name='delete'),
    path('<str:username>/<int:post_id>/comments/create/',views.comment_create,name='comment_create'),
    path('<str:username>/<int:post_id>/comments/<int:comment_id>/delete/',views.comment_delete,name="comment_delete"),
    path('<str:username>/<int:post_id>/like/',views.like,name="like"),
    # path('<int:post_id>/like/togo',views.liketogo,name='liketogo'),
]