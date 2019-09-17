from django.contrib import admin
from .models import Post


# Register your models here.


# 自定义Post显示类
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'pub_date')


# 注册自己的models模块到admin管理界面中
admin.site.register(Post, PostAdmin)
