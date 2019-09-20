__author__ = 'Rico'
__date__ = '2019/9/20 15:14'
from django.urls import path
from . import views

app_name = 'userprofile'

urlpatterns = [
    # 用户登出
    path('logout/', views.user_logout, name='logout'),
    # 用户登入
    path('login/', views.user_login, name='login'),
]