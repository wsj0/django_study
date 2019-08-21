from django.conf.urls import url
from .views import *

urlpatterns=[
    url(r'^page1$',page1_view),
    url(r'^page2$',page2_view),
    url(r'^page3$',page3_view),
]