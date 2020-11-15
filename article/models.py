from django.db import models
from django.utils import  timezone
from django.contrib.auth.models import User

# Create your models here.
# tag（标签模型）
class Tag(models.Model):
    name = models.CharField(max_length=30, verbose_name='标签')

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
# 分类模型
class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name='分类')
    index = models.IntegerField(default=999,verbose_name='分类的排序')

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name
        ordering = ['index']

    def __str__(self):
        return self.name


class Article(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    body=models.TextField()
    # 文章点击量
    total_views = models.PositiveIntegerField(default=0)
    # 文章分类的 “一对多” 外键
    category = models.ForeignKey(Category, blank=True, null=True, verbose_name='分类',on_delete=models.DO_NOTHING)
    tag = models.ManyToManyField(Tag, verbose_name='标签')
    # 文章标题图
    avatar = models.ImageField(upload_to='article/%Y%m%d/', blank=True)
    created=models.DateTimeField(default=timezone.now)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        # '-created' 表明数据应该以倒序排列
        ordering=('-updated',)

    def __str__(self):
        return self.title
