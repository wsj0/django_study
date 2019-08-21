from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def sport_view(request):
    return HttpResponse('运动首页')