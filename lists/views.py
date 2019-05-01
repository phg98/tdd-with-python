from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):
    return HttpResponse('<!Doctype html><html><title>일정관리</title></html>\n')
