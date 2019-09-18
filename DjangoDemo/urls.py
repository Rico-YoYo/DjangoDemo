"""DjangoDemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Yogastie import views as yoga_views
from mblog import views as blog_views

# 存放Url映射关系的列表
urlpatterns = [

    path('admin/', admin.site.urls),
    # 配置APP的url
    path('article/', include('article.urls', namespace='article')),

    # helloblog项目，先注释掉 2019/9/17日
    # path('', include('helloblog.urls')),
    # helloblog项目的评论模块,先注释，需要时再打开 2019/9/17
    # path('', include('comments.urls')),

    # TODO 暂时不实现瑜伽网站的内容  《Django架站的16堂课》 9/2
    path('', blog_views.homepage),
    path('post/<slug:slug>/', blog_views.showpost),
    path('demo/<slug:demo>/', blog_views.showDemo),

]
