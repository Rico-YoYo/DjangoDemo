from django.shortcuts import render, redirect
import markdown
from django.http import HttpResponse
from .models import ArticlePost
# 引入刚才定义的ArticlePostForm表单类
from .forms import ArticlePostForm
# 引入Django内置的User模型
from django.contrib.auth.models import User


# 更新的文章
def article_update(request, id):
    # 获取需要更改信息的具体对象
    article = ArticlePost.objects.get(id=id)
    if request.method == 'POST':
        article_post_form = ArticlePostForm(data=request.POST)
        if article_post_form.is_valid():
            article.title = request.POST['title']
            article.body = request.POST['body']
            article.save()
            return redirect('article:article_detail', id=id)
        else:
            return HttpResponse('表单内容有误，请重新填写。')
    else:
        article_post_form = ArticlePostForm()
        context = {'article':article,'article_post_form':article_post_form}
        return render(request,'article/update.html', context)


# 安全的删除文章
def article_safe_delete(request,id):
    if request.method == "POST":
        article = ArticlePost.objects.get(id=id)
        article.delete()
        return redirect('article:article_list')
    else:
        return HttpResponse('仅限于Post请求！')


# 删除文章
def article_delete(request, id):
    # 根据Id获取文章
    article = ArticlePost.objects.get(id=id)
    # 调用.delete()方法删除文章
    article.delete()
    # 完成后返回文章列表
    return redirect('article:article_list')


# 写文章
def article_create(request):
    # 判断用户是否提交数据
    if request.method == 'POST':
        # 将提交的数据赋值道表单实例中
        article_post_form = ArticlePostForm(data=request.POST)
        # 判断提交的数据是否满足数据模型
        if article_post_form.is_valid():
            # 保存数据，但暂时不提交到数据库中
            new_article = article_post_form.save(commit=False)
            # 指定数据库中 id=1 的用户是为作者
            # 如果你进行过删除数据表的操作，可能会找不到id=1的用户
            # 此时请重新创建用户，并传入此用户的Id
            new_article.author = User.objects.get(id=1)
            # 将新文章保存到数据库中
            new_article.save()
            # 完成后返回文章列表
            return redirect("article:article_list")
        # 如果数据不合法，返回错误信息
        else:
            return HttpResponse('表单内容有误，请重新填写！')
    # 如果用户请求获取数据
    else:
        # 创建表单实例
        article_post_form = ArticlePostForm()
        # 赋值上下文
        context = {'article_post_form': article_post_form}
        # 返回模版
        return render(request, 'article/create.html', context)


# 获取文章详情
def article_detail(request, id):
    article = ArticlePost.objects.get(id=id)
    # 将markdown语法渲染成html样式
    article.body = markdown.markdown(article.body,
                                     extensions=[
                                         # 包含表格、缩写等常用扩展
                                         'markdown.extensions.extra',
                                     ])
    context = {'article': article}
    return render(request, 'article/detail.html', context)


# 获取文章列表
def article_list(request):
    # 取出所有文章
    articles = ArticlePost.objects.all()
    # 需要传递给模版的对象
    context = {'articles': articles}
    return render(request, 'article/list.html', context)