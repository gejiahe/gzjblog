

## 视图初探 Hello world

首先写一个最简单的**视图函数**，在浏览器中打印出`Hello World!`字符串。

打开`article/views.py`，写出视图函数：

```python
article/views.py
# 导入 HttpResponse 模块
from django.http import HttpResponse

# 视图函数
def article_list(request):
    return HttpResponse("Hello World!")
```

打开`article/urls.py`，写出路由：

```python
article/urls.py
urlpatterns=[
  path('article_list/',views.article_list,name='article_list')
]
```

##  后台 Admin

**网站后台**，有时也称为**网站管理后台**，是指用于管理网站的一系列操作，如：数据的增加、更新、删除等。

### 创建管理员账号（Superuser）

管理员账号（Superuser）是可以进入网站后台，对数据进行维护的账号，具有很高的权限。这里我们需要创建一个管理员账号，以便添加后续的测试数据。

```python
# terminal 虚拟环境中输入，并按提示输入用户名、邮箱、密码
python manage.py createsuperuser
```

打开`article/admin.py`，把模型注册到后台中：

```python
from django.contrib import admin
from .models import Article,Category,Tag
# Register your models here.

admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Article)

```

## 总结

本章初步感受了View的工作模式，创建了Superuser在后台录入了几条测试数据。下一章将编写更有意义的View，准备好后老司机就开车了。

