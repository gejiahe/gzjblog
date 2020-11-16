**Django 框架主要关注的是模型（Model）、模板（Template）和视图（Views），称为MTV模式。**

## 编写模型

```python
articl/models 
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


class ArticlePost(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    body=models.TextField()
    # 文章点击量
    total_views = models.PositiveIntegerField(default=0)
    # 文章分类的 “一对多” 外键
    category = models.ForeignKey(Category, blank=True, null=True, verbose_name='分类',on_delete=models.DO_NOTHING)
    # 文章标签  “多对多” 外键
    tag = models.ManyToManyField(Tag,verbose_name='标签')
    # 文章标题图
    avatar = models.ImageField(upload_to='article/%Y%m%d/', blank=True)
    create_time=models.DateTimeField(default=timezone.now)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=('-updated',)

    def __str__(self):
        return self.title
```

## 数据迁移

```python
# Terminal中执行
python manage.py makemigrations
python manage.py migrate
```

> 纠错：Article模型中tag的blank=true,null=true删除