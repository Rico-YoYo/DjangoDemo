__author__ = 'Rico'
__date__ = '2019/9/15 22:08'

from django import template
from ..models import Post, Category, Tag
# 实例化了一个 template.Library 类
register = template.Library()

# 分类标签模版
@register.inclusion_tag('helloblog/inclusions/_categories.html', takes_context=True)
def show_categories(context):
    return {
        'category_list': Category.objects.all(),
    }

# 标签云模版
@register.inclusion_tag('helloblog/inclusions/_tags.html', takes_context=True)
def show_tags(context):
    return {
        'tag_list': Tag.objects.all(),
    }

# 归档模版标签
@register.inclusion_tag('helloblog/inclusions/_archives.html', takes_context=True)
def show_archives(context):
    return {
        'date_list': Post.objects.dates('created_time', 'month', order='DESC')
    }


# 最新文章模版标签
@register.inclusion_tag('helloblog/inclusions/_recent_posts.html', takes_context=True)
def show_recent_posts(context, num=5):
    return {
        'recent_post_list': Post.objects.all()[:num],
    }
