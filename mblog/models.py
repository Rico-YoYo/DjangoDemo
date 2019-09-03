from django.db import models
from django.utils import timezone


# Create your models here.

class Post(models.Model):
    # 文章标题
    title = models.CharField('标题', max_length=200)
    # 文章网址
    slug = models.CharField('标识', max_length=200)
    # 文章内容
    body = models.TextField()
    # 文章发表日期
    pub_date = models.DateTimeField('发表日期', default=timezone.now)

    class Meta:
        ordering = ('-pub_date',)
        verbose_name_plural = '文章'

    def __str__(self):
        return self.title
