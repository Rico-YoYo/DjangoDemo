__author__ = "Rico"
__date__ = "2019/9/17 23:27"

from django.urls import path
from . import views

# 正在部署的应用名称，即项目的命名空间，防止url冲突
app_name = "article"

urlpatterns = [
    path("article-list/", views.article_list, name="article_list")
    ]
