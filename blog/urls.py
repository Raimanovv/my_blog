from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:number_post>/', views.number_post_def),
    path('<str:str_post>/', views.str_post_def),
]
