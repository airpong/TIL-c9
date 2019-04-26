from django.urls import path
from . import views
app_name = 'accounts'
urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('logout/',views.logout,name='logout'),
    path('login/',views.login,name='login'),
    path('userlist/',views.userlist,name='userlist'),
    path('<str:username>/',views.userdetail,name='userdetail'),
    path('<str:username>/follow/',views.follow,name='follow'),
    path('<str:username>/update/',views.update,name='update'),
    path('<str:username>/password/',views.password,name='password'),
]