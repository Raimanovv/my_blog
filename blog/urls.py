from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),

    path('posts/', views.posts),
    path('post/keanu/', views.keanu),

    path('post/<int:number_post>/', views.number_post),
    path('post/<str:post_name>/', views.post_name),

    path('guinness_records/', views.guinness_records),

    path('<int:number_post>/', views.number_post_def),
    path('<str:str_post>/', views.str_post_def),
]
