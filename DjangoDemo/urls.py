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

urlpatterns = [
    # TODO 暂时不实现瑜伽网站的内容  9/2
    # path('', blog_views.homepage),
    path('', include('helloblog.urls')),
    path('', include('comments.urls')),
    path('post/<slug:slug>/', blog_views.showpost),
    path('demo/<slug:demo>/', blog_views.showDemo),
    path('admin/', admin.site.urls),
]
