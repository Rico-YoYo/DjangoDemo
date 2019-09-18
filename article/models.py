from email.quoprimime import body_check

from django.db import models
# 导入内检模型User
from django.contrib.auth.models import User
# timezone 用于处理时间相关事务
from django.utils import timezone


# 博客文章的数据模型
class ArticlePost(models.Model):
    # 文章作者 参数on_delete用于指定数据的删除方式
    author = models.ForeignKey(User, verbose_name='作者', on_delete=models.CASCADE)
    # 文章标题 models.CharField 为字符串字段，用于保存较短的字符，比如标题
    title = models.CharField('标题', max_length=100)
    # 文章正文 保存大量文本，使用TextField
    body = models.TextField('正文')
    # 文章创建时间。参数default=timezone.now 指定再创建数据时将默认写入当前时间
    created = models.DateTimeField('创建时间', default=timezone.now)
    # 文章更新时间。参数auto_now = True 指定每次数据更新时自动写入当前时间
    update = models.DateTimeField('修改时间', auto_now=True)

    # 内部类  用于给model定义元数据
    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ('-created',)

    # 函数__str__定义当调用对象的str()方法时，返回值的内容
    def __str__(self):
        # 将文章标题返回
        return self.title

