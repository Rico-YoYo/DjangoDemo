from django.db import models


# 2019.9.01 学习python的数据模型
class Users(models.Model):
    # user
    username = models.CharField('用户名', max_length=4)

    class Meta:
        verbose_name_plural = '客户'

    def __str__(self):
        return self.username
