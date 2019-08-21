from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
#file: bookstore/views.py

def add_view(request):
    try:
        abook=Book()
        abook.title = 'HTML5'
        abook.price1 = 90
        abook.price2 = 105
        abook.save()
        return  HttpResponse('添加图书成功！')
    except Exception as e:
        return HttpResponse('添加图书失败！')