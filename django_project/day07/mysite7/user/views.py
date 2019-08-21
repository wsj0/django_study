from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import *
from . import forms
# Create your views here.
def reg_view(request):
    if request.method=='GET':
        return render(request,'user/register.html')
    elif request.method=='POST':
        username=request.POST.get('username','')
        password1 = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')
        #验证数据的合法性
        if len(username)<6:
            username_error='用户名太短'
            return render(request,'user/register.html',locals())
        #验证密码是否为空
        if len(password1)==0:
            password_error='密码不能为空'
            return render(request,'user/register.html',locals())
        #验证两次密码是否一致
        if password2!=password1:
            password2_error='两次密码不一致'
            return render(request,'user/register.html',locals())
        try:
            auser=User.objects.get(
                username=username)
            username_error='用户名已存在'
            return render(request,'user/register.html',locals())
        except:
            auser=User.objects.create(username=username,
                                      password=password1)
        html = "注册成功！<a href='/user/login'>进入登入</a>"
        resp=HttpResponse(html)
        resp.set_cookie('username',username)
        return resp

def login_view(request):
    #设置session的值
    # request.session['abc']=123
    # val=request.session.get('abc','xxx')
    # return HttpResponse(val)
    if request.method=='GET':
        username=request.COOKIES.get('username','')
        return render(request,'user/login.html',locals())
    elif request.method=='POST':
        username=request.POST.get('username','')
        password=request.POST.get('password','')
        if username=='':
            username_error='用户名不能为空'
            return render(request,'user/login.html',
                          locals())
        #处理登陆的逻辑
        try:
            auser=User.objects.get(
                username=username,
                password=password
            )
            #记录一个登录状态
            request.session['user']={
                'username':username,
                'id':auser.id,
            }
            resp=HttpResponseRedirect('/')
            if 'remember' in request.POST:#如果是选中状态
                resp.set_cookie('username',username)
            return resp
        except:
            password_error='用户名或密码不正确'
            return render(request,'user/login.html',locals())

def logout_view(request):
    #退出登录
    if 'user' in request.session:
        del request.session['user'] #清除登录记录
    return HttpResponseRedirect('/')#返回主页

def reg2_view(request):
    if request.method=='GET':
        myform1=forms.MyRegForm()
        return render(request,
                      'user/register2.html',
                      locals())
    # html=myform1.as_p()
    # print(html)
    # return HttpResponse(html)
    elif request.method=='POST':
        myform=forms.MyRegForm(request.POST)
        if myform.is_valid():
            dic=myform.cleaned_data
            username=dic['username']
            password=dic['password']
            password2=dic['password1']
            if len(username)<6:
                return HttpResponse('用户名太短')
            return HttpResponse(str(dic))
        else:
            return HttpResponse('表单验证失败')

        # username=request.POST.get('username','')
        # password1 = request.POST.get('username', '')
        # password2 = request.POST.get('username', '')
        # dic=dict(request.POST)
        # return HttpResponse(str(dic))