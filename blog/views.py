from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.template.loader import render_to_string


# list_guinness_records = ['Мощный удар', 'Гамбургер', 'Человек-ёж']


# Create your views here.

def index(request):
    return render(request, 'blog/index.html')


def posts(request):
    response = render(request, 'blog/list_detail.html')
    return HttpResponse(response)


def keanu(request):
    data = {
        'post': 'keanu',
        'year_born': '2 сентября 1964 г.',
        'city_born': 'Бейрут, Ливан',
        'movie_name': 'На гребне волны',
    }
    return render(request, 'blog/post.html', context=data)


def number_post_def(request, number_post: int):
    return HttpResponse(f'Здесь содержится информация о посте под номером {number_post}')


def str_post_def(request, str_post: str):
    return HttpResponse(f'Информация о посте {str_post}')


def number_post(request, number_post: int):
    data = {
        'number': number_post
    }
    return render(request, 'blog/detail_by_number.html', context=data)


def post_name(request, post_name: str):
    data = {
        'name': post_name
    }
    return render(request, 'blog/detail_by_name.html', context=data)


def guinness_records(request):
    data = {
        'power_man': 'Narve Laeret',
        'bar_name': 'Bob’s BBQ & Grill',
        'count_needle': 1790,
    }
    return render(request, 'blog/guinness_records.html', context=data)

# def guinness_records(request):
#     li_elements = ''
#     for record in list_guinness_records:
#         li_elements += f"<li>{record.title()}</a></li>"
#     response = f'<ol>{li_elements}</ol>'
#     return HttpResponse(response)
