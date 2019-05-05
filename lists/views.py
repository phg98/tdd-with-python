from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item


def home_page(request):
    if request.method == 'POST':
        Item.objects.create(text=(request.POST.get('item_text', '')))
        return redirect('/lists/only-list')

    return render(request, 'home.html')


def view_list(request):
    items = Item.objects.all()
    return render(request, 'list.html', {'item_list': items})
