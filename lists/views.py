from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item, List


def home_page(request):
    return render(request, 'home.html')


def view_list(request):
    items = Item.objects.all()
    return render(request, 'list.html', {'item_list': items})


def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=(request.POST.get('item_text', '')), list=list_)
    return redirect('/lists/only-list/')
