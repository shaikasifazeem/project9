from django.urls import path
from app2.views import *
app_name='sample'
urlpatterns=[
    path('vip2/',VIP2,name='VIP2.html'),
]