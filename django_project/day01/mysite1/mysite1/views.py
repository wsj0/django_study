#file：mysite1/views.py
from django.http import HttpResponse,HttpResponseRedirect


def page1_view(request):
    html='<h3>这是第1个页面</h3>'
    return HttpResponse(html)
def index_view(request):
    html='<h3>这是我的首页</h3>'
    return HttpResponse(html)
def page2_view(request):
    html='<h3>这是第2个页面</h3>'
    return HttpResponse(html)
def pagen_view(request,n):
    html='<h3>这是第%s页面</h3>' % n
    return HttpResponse(html)

# def add_view(request,n1,n2):
#     result=int(n1)+int(n2)
#     return HttpResponse(result)
# def sub_view(request,n1,n2):
#     result=int(n1)-int(n2)
#     return HttpResponse(result)
# def sub_view(request,n1,n2):
#     result=int(n1)*int(n2)
#     return HttpResponse(result)
def math_view(request,n1,op,n2):
    result=0
    if op=='add':
        result = int(n1) + int(n2)
    elif op=='sub':
        result = int(n1) - int(n2)
    elif op=='mul':
        result = int(n1) * int(n2)
    if result ==0:
        return HttpResponseRedirect('https://www.baidu.com/')
    else:
        return HttpResponse('结果：'+str(result))

def person_view(request,**kwargs):
    s=str(kwargs['name'])
    return HttpResponse(s)
def birth_view(request,n1,n2,n3):
    if len(n1)>len(n3):
        result='生日为：%s年%s月%s日'%(n1,n2,n3)
    else:
        result = '生日为：%s年%s月%s日' % (n3, n1, n2)
    return HttpResponse(result)

def birth_view1(request,**kwargs):
    year=kwargs['year']
    month=kwargs['month']
    day=kwargs['day']
    result = '生日为：%s年%s月%s日' % (year, month, day)
    return HttpResponse(result)

def mypage_view(request):
    """
    http://127.0.0.1:8000/mypage?a=100&b=200
    """
    if request.method=='GET':
        a=request.GET.getlist('a')
        b=request.GET['b']
        html='a ='+str(a)+'b ='+b
        return HttpResponse(html)
    else:
        return HttpResponse('当前不是GET请求')

def sum_view(request):
    if request.method=='GET':
        start=int(request.GET['start'])
        stop = int(request.GET['stop'])
        step = int(request.GET['step'])
        print(start,step,stop)
        result=sum(range(start,stop,step))
        return HttpResponse(result)
    else:
        return HttpResponse('当前不是GET请求')
