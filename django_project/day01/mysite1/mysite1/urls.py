"""mysite1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.index_view),
    # url(r'^page1',views.page1_view),
    # url(r'^page2',views.page2_view),
    # url(r'^page(\d+)',views.pagen_view),
    # url(r'^(\d+)/add/(\d+)',views.add_view),
    # url(r'^(\d+)/sub/(\d+)',views.sub_view),
    # url(r'^(\d+)/mul/(\d+)',views.sub_view),
    url(r'^(\d+)/(\S{3})/(\d+)',views.math_view),
    url(r'^person/(?P<name>\w+)/(?P<age>\d{1,2})',
        views.person_view),
    url(r'^birthday/(\d+)/(\d{1,2})/(\d+)',
        views.birth_view),
    url(r'birth/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})',
        views.birth_view1),
    url(r'^mypage',views.mypage_view),
    url(r'^sum',views.sum_view),
]
