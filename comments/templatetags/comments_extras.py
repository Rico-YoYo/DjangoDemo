__author__ = 'Rico'
__date__ = '2019/9/16 13:47'

from django import template
from ..forms import CommentForm

register = template.Library()


@register.inclusion_tag('comments/inclusions/_form.html', takes_context=True)
def show_comment_form(context, post, form=None):
    if form is None:
        form = CommentForm()
    return {
        'form': form,
        'post': post,
    }


# 显示评论列表
@register.inclusion_tag('comments/inclusions/_list.html', takes_context=True)
def show_comments(context, post):
    comment_list = post.comment_set.all()
    comment_count = comment_list.count()
    return {
        'comment_count': comment_count,
        'comment_list': comment_list
    }
