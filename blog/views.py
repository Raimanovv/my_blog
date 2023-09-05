from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def number_post_def(request, number_post: int):
    return HttpResponse(f'Здесь содержится информация о посте под номером {number_post}')


def str_post_def(request, str_post: str):
    return HttpResponse(f'Информация о посте {str_post}')
