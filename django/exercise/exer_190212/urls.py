from django.urls import path
from . import views
app_name = 'exer_190212'
urlpatterns = [
    path('',views.update_profile),

]