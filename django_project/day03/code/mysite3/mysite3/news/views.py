from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def news_view(request):
    return HttpResponse('新闻首页')