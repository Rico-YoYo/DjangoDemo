__author__ = 'Rico'
__date__ = '2019/9/16 13:58'

from django.urls import path
from . import views


app_name = 'comments'

urlpatterns = [
    path('comment/<int:post_pk>', views.comment, name='comment')
]