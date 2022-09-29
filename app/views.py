from django.http import HttpResponse
from django.shortcuts import render, reverse
from django.views import generic

from datetime import datetime
from os import getcwd, listdir


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }

    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    # обратите внимание – здесь HTML шаблона нет,
    # возвращается просто текст
    current_time = datetime.now().time()
    current_date = datetime.now().date()
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    template_name = 'app/directory.html'
    # по аналогии с `time_view`, напишите код,
    # который возвращает список файлов в рабочей
    # директории
    current_directory = getcwd()
    current_list = listdir(current_directory)
    #raise NotImplemented
    context = {"list_dir": current_list, "current_dir": current_directory}
    return render(request, template_name, context)
