from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^add',views.add_view),
    url(r'^all',views.show_all),
    url(r'^show',views.show_view),
    url(r'^mod/(\d+)',views.mod_view),
    url(r'^del/(\d+)',views.del_view),
    url(r'^select_price',views.select_price_view),
    url(r'^select_title',views.select_title_view),
    url(r'^cut_price',views.cut_price_view),
    url(r'^test',views.test_view),
]