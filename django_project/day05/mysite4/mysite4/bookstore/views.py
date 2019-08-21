from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import *
from django.db.models import F,Q
# Create your views here.
#file: bookstore/views.py

def add_view(request):
    if request.method=='GET':
        return render(request,'bookstore/add_book.html')
    elif request.method=='POST':
        title=request.POST.get('title')
        pub=request.POST.get('pub')
        price=float(request.POST.get('price','0'))
        m_price=float(request.POST.get('m_price','0'))
        try:
            Book.objects.create(
                title=title,
                pub=pub,
                price=price,
                market_price=m_price
            )
            return HttpResponseRedirect('/bookstore/show')
        except:
            return HttpResponse('添加失败!')

def show_all(request):
    books=Book.objects.all()
    for abook in books:
        print('书名:'+abook.title)
    return HttpResponse('ok')

def show_view(request):
    book=Book()
    books=Book.objects.all()
    if request.method=='GET':
        return render(request,'bookstore/show_book.html',locals())
    elif request.method=='POST':
        id=request.POST.get()

def mod_view(request,id):
    try:
        abook=Book.objects.get(id=id)
    except:
        return HttpResponse('没有id为'+id+'的数据记录')

    if request.method=='GET':
        return render(request,'bookstore/mod.html',
                      locals())
    elif request.method=='POST':
        m_price=float(request.POST.get('m_price','0'))
        abook.market_price=m_price
        abook.save()
        return HttpResponseRedirect('/bookstore/show')

def del_view(request,id):
    try:
        dbook=Book.objects.get(id=id)
    except:
        return HttpResponse('没有id为'+id+'的数据记录')

    if request.method=='GET':
        return render(request,'bookstore/del.html',locals())
    elif request.method=='POST':
        dbook.delete()
        return HttpResponseRedirect('/bookstore/show')


def select_price_view(request):
    if request.method=='GET':
        abook=Book.objects.all()
        return render(request,'bookstore/select_price.html',locals())
    elif request.method=='POST':
        price=float(request.POST.get('price','0'))
        abook=Book.objects.filter(market_price__lt=price)
        return render(request,'bookstore/select_price.html',locals())

def select_title_view(request):
    if request.method == 'GET':
        abook = Book.objects.all()
        return render(request, 'bookstore/select_title.html', locals())
    elif request.method == 'POST':
        title = request.POST.get('title', '0')
        abook = Book.objects.filter(title__contains=title)
        return render(request, 'bookstore/select_title.html', locals())

def cut_price_view(request):
    if request.method=='GET':
        abook=Book.objects.filter(market_price__lt=F('price'))
        return render(request,'bookstore/cut_price.html',locals())
    else:
        return HttpResponse('none')

def test_view(request):
    if request.method=='GET':
        abook=Book.objects.filter(~Q(pub="清华大学出版社")&Q(price__lt=50))
        return render(request,'bookstore/test.html',locals())
    else:
        return HttpResponse('none')

def set_cookies_view(request):
    resp=HttpResponse('ok')
    resp.set_cookie('myvar','aaa',max_age=10)
    return resp

def get_cookies_view(request):
    v=request.COOKIES.get('myvar','none')
    return HttpResponse('myvar='+v)