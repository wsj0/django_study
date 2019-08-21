from django.http import HttpResponse
from django.shortcuts import render

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

login_form_html="""
<form method='post' action="/login">
   用户名:<input type="text" name="username">
   密码:<input type="password" name='password'>
   <input type='submit' value='登录'>
</form>
"""

def login_view(request):
    if request.method=='GET':
        return HttpResponse(login_form_html)
    elif request.method=='POST':
        # name=request.POST.get('username','属性错误')
        # password = request.POST.get('password', '属性错误')
        # html='姓名'+name+'密码'+password
        s=str(dict(request.POST))
        return  HttpResponse(s)

def login2_view(request):
    if request.method=='GET':
        #返回模板生成的html给浏览器
        # #方法1
        # #加载模块
        # from django.template import loader
        # t=loader.get_template('mylogin.html')
        # #用模板生成html
        # html=t.render('name','tarena')
        # #返回给浏览器
        # return HttpResponse(html)
        #方法2
        return render(request,'mylogin.html',)

def test_view(request):
    s='hello world'
    lst=['北京','上海','重庆']
    mydic={'name':'tedu','age':20}
    dic={
        's':s,
        'lst':lst,
        'mydic':mydic,
    }
    return render(request,'test.html',dic)

def mytemp_view(request):
    dic={
        'x':0
    }
    return render(request,'mytemp.html',dic)

def local_view(request):
    s=1
    lst=[1,2,3]
    dic={'name':'wsj',
         'age':12}
    return render(request,'locals.html',locals())

def mycal_view(request):
    if request.method=='GET':
        return render(request,'calculate.html')
    elif request.method=='POST':
        x=int(request.POST.get('x','0'))
        y=int(request.POST.get('y','0'))
        cal=request.POST.get('cal')
        if cal=='add':
            result=x+y
        elif cal=='sub':
            result=x-y
        elif cal=='mul':
            result=x*y
        elif cal=='div':
            result=x/y
        return render(request,'calculate.html',locals())
    else:
        return 'none'

def for_view(request):
    lst=['北京','上海','天津','重庆']
    s='hello world'
    return render(request,'for.html',locals())

def index_view(request):
    return render(request,'base.html')
def sport_view(request):
    return render(request,'sport.html')
def news_view(request):
    return render(request,'new.html')

def baoxian_view(request):
    if request.method=='GET':
        return render(request,'baoxian.html')
    elif request.method=='POST':
        fund=int(request.POST.get('base','0'))
        address=(request.POST.get('is_city','1'))
        old1=fund*0.08
        old2=fund*0.19
        print(fund, address)
        if address=='1':
            work1=0.002*fund
            work2=0.008*fund
        elif address=='0':
            work1 = 0.000 * fund
            work2 = 0.008 * fund
        gs1=0.000*fund
        gs2=0.005*fund
        sy1=0.000*fund
        sy2=0.008*fund
        yl1=0.02*fund+3
        yl2=0.1*fund
        gjj1=0.12*fund
        gjj2=0.12*fund
        person=old1+work1+gs1+sy1+yl1+gjj1
        factor=old2+work2+gs2+sy2+yl2+gjj2
        sum=person+factor
        return render(request,'shebao.html',locals())
