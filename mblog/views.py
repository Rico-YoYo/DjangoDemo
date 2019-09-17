from django.template.loader import get_template
from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from .models import Post


# 程序逻辑主要放在View文件中


# 显示Demo文件
def showDemo(request, demo):
    template = get_template("demo.html")
    try:
        if demo is not None:
            html = template.render(locals())
            return HttpResponse(html)
    except:
        return redirect("/")


# 显示详细数据
def showpost(request, slug):
    template = get_template("post.html")
    try:
        post = Post.objects.get(slug=slug)
        if post != None:
            html = template.render(locals())
            return HttpResponse(html)
    except:
        return redirect("/")


# 取出Post中所有的数据
def homepage(request):
    # 加载模版
    template = get_template('index.html')
    # 获取全部帖子
    posts = Post.objects.all()
    # 获取当前时间
    now = datetime.now()
    html = template.render(locals())
    # post_lists = list()
    # for count, post in enumerate(posts):
    #     post_lists.append('No.{}:'.format(str(count)) + str(post) + "<hr>")
    #     post_lists.append("<small>" + str(post.body) + "</small><br><br>")
    return HttpResponse(html)
