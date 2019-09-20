__author__ = "Rico"
__date__ = "2019/9/20 14:56"

from django import forms
from django.contrib.auth.models import User


# 登陆表单，继承forms.Form类
class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
