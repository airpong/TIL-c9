from django.urls import path
from . import views
app_name = 'exer_190130'
urlpatterns = [
    # path('<int:question_id>/',views.sbmit, name='sbmit'),
    path('<int:question_id>/<int:menu_id>/',views.submit, name='submit'),
    path('<int:question_id>/upload/',views.upload, name='upload'),
    path('<int:question_id>/newChoice',views.newChoice, name='newChoice'),
    path('/newquestion',views.newquestion, name='newquestion'),
    path('/createquestion',views.createquestion, name='createquestion'),
    path('',views.index2, name='list'),
]