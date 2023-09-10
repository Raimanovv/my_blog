from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string


# Create your views here.

def index(request):
    response = render_to_string('blog/index.html')
    return HttpResponse(response)


def posts(request):
    response = render(request, 'blog/list_detail.html')
    return HttpResponse(response)


def number_post_def(request, number_post: int):
    return HttpResponse(f'Здесь содержится информация о посте под номером {number_post}')


def str_post_def(request, str_post: str):
    return HttpResponse(f'Информация о посте {str_post}')
