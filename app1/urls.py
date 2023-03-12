from django.urls import path
from app1.views import *
app_name='sample'
urlpatterns=[
    path('VIP/',VIP,name='VIP.html'),
]