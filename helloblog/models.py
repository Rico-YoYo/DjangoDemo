from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
import markdown
from django.utils.html import strip_tags


# Create your models here.


# 创建文章类别
class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "分类"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 标签累
class Tag(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "标签"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 文章类
class Post(models.Model):
    # 标题
    title = models.CharField("标题", max_length=70)
    # 文章正文
    body = models.TextField("正文")
    # 文章创建的时间
    created_time = models.DateTimeField("创建时间", default=timezone.now)
    # 文章最后修改的时间
    modified_time = models.DateTimeField("修改时间")
    # 文章简要
    excerpt = models.CharField("摘要", max_length=200, blank=True)
    # 文章类别
    category = models.ForeignKey(Category, verbose_name="分类", on_delete=models.CASCADE)
    # 文章标签
    tags = models.ManyToManyField(Tag, verbose_name="标签", blank=True)
    # 作者
    author = models.ForeignKey(User, verbose_name="作者", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = verbose_name
        ordering = ["-created_time"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.modified_time = timezone.now()

        # 首先实例化一个 Markdown 类，用于渲染 body 的文本。
        # 由于摘要并不需要生成文章目录，所以去掉了目录拓展。
        md = markdown.Markdown(
            extensions=["markdown.extensions.extra", "markdown.extensions.codehilite"]
        )

        # 先将 Markdown 文本渲染成 HTML 文本
        # strip_tags 去掉 HTML 文本的全部 HTML 标签
        # 从文本摘取前 54 个字符赋给 excerpt
        self.excerpt = strip_tags(md.convert(self.body))[:54]
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("helloblog:detail", kwargs={"pk": self.pk})
