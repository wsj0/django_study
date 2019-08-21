from django.http import HttpResponse
from django.shortcuts import render

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
