from django.urls import path
from . import views
from accounts import views as accounts_views
app_name = 'accounts'

urlpatterns = [
    path('<str:username>/signup/',views.signup,name='signup'),
    path('<str:username>/login/',views.login,name='login'),
    path('<str:username>/logout/',views.logout,name='logout'),
    path('<str:username>/',accounts_views.people,name='people'),
]