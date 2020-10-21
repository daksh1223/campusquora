from django.urls import path

from . import views

urlpatterns = [
    path('<int:id>/',views.feed,name='feed'),
    path('<int:uid>/<int:qid>/',views.quest,name='quest'),
]