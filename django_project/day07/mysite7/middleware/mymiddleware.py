from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse
class MyMW(MiddlewareMixin):
    def process_request(self,request):
        print("中间件 process_request方法被调用！")
        print("路由是:",request.path)
        print('请求方法：',request.method)
        if request.path== '/aaaa':
            return HttpResponse('当前路由是：/aaaa')

class VisitLimit(MiddlewareMixin):
    #此字典的键为IP地址，值为IP地址的访问次数
    visit_times={}
    def process_request(self,request):
        #得到客户端的IP
        ip=request.META['REMOTE_ADDR']
        if request.path_info!='/test':
            return None
        times=self.visit_times.get(ip,0)
        print(times)
        print("IP",ip,'已访问过/test',times,'次')
        self.visit_times[ip]=times+1
        if times<5:
            return None
        return HttpResponse("您已经访问过："+str(times)
                            +'次')