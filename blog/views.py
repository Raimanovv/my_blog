from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.template.loader import render_to_string
from random import sample

data_posts = [
    {
        'title': 'Рыбалка',
        'description': 'Хорошо посидели',
        'date': '21 авг 2021',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Commodi distinctio doloremque et fuga iste neque, pariatur quod sit veritatis voluptates?'
    },
    {
        'title': 'Париж',
        'description': 'Незабываемое путешествие',
        'date': '5 сент 2020',
        'content': '''Lorem ipsum dolor sit amet, consectetur adipisicing elit. 
                Commodi distinctio doloremque et fuga iste neque, pariatur quod sit veritatis voluptates?'''
    },
    {
        'title': 'Финал лиги чемпионов',
        'description': 'Реал опять выиграл ЛЧ',
        'date': '28 мая 2022',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Qui, rem.'
    },
    {
        'title': 'Охота на уток',
        'description': 'Ни одна утка не пострадала',
        'date': '7 дек 2019',
        'content': 'Lorem ipsum dolor sit amet.'
    },
    {
        'title': 'Фестиваль огурца',
        'description': 'Суздаль ждет тебя',
        'date': '12 июль 2021',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Adipisci consectetur id inventore odit recusandae!'
    },
    {
        'title': 'Нашествие',
        'description': 'Даешь рок, но в следующем году',
        'date': '29 июль 2021',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Est mollitia recusandae rem?'
    },
    {
        'title': 'Новый год',
        'description': 'Эх, еще один год пролетел',
        'date': '31 дек 2022',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. A architecto corporis fuga ipsam laboriosam, nesciunt non quae qui ut veniam.'
    },
]


# Create your views here.

def index(request):
    rand_posts = sample(data_posts, 3)
    data = {
        'rand_posts': rand_posts
    }
    return render(request, 'blog/index.html', context=data)


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
