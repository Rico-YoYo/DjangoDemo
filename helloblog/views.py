import markdown
import re
from django.utils.text import slugify
from markdown.extensions.toc import TocExtension
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post, Category, Tag


# 根据标签类获取文章列表
def tag(request, pk):
    t = get_object_or_404(Tag, pk=pk)
    post_list = Post.objects.filter(tags=t)
    return render(request, "helloblog/index.html", context={"post_list": post_list})


# 根据文章类别获取文章列表
def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate)
    return render(request, "helloblog/index.html", context={"post_list": post_list})


# 点击归档标签，读取当下归档标签的内容
def archive(request, year, month):
    post_list = Post.objects.filter(created_time__year=year, created_time__month=month)
    return render(request, "helloblog/index.html", context={"post_list": post_list})


# 详情页
def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # 实例化一个Markdown对象
    md = markdown.Markdown(
        extensions=[
            "markdown.extensions.extra",
            "markdown.extensions.codehilite",
            TocExtension(slugify=slugify),
        ]
    )

    post.body = md.convert(post.body)

    m = re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>', md.toc, re.S)

    # 动态给post对象赋值toc属性
    post.toc = m.group(1) if m is not None else ""

    return render(request, "helloblog/detail.html", context={"post": post})


# 首页
def index(request):
    post_list = Post.objects.all()
    return render(request, "helloblog/index.html", context={"post_list": post_list})
