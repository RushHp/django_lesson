from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


def index(request):
    items = Product.objects.all()
    # Передаем значения из БД на html.
    context = {
        'items': items
    }
    return render(request, 'myapp/index.html', context)

 
# Вывод значения по адресу url, по клику на ссылку /myapp/hello/1/.
# Этот id в параметре находится в urls.
def index_item(request, id):
    # Достаем id из БД, по id из urls.
    item = Product.objects.get(id=id)
    context = {
        'item': item
    }
    return render(request, 'myapp/detail.html', context=context)
