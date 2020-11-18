## 改写视图函数

**为了让视图真正发挥作用，**改写`article/views.py`中的`article_list`视图函数：

```python
# article/views.py

from django.shortcuts import render
from .models import Article

# 视图函数
def article_list(request):
    # 取出所有博客文章
    articles = Article.objects.all()
    # 需要传递给模板（templates）的对象
    context = {'articles': articles}
    # render函数：载入模板，并返回context对象
    return render(request, 'article/list.html', context)
```

##  编写模板

```python
# templates/article/list.html

{% for article in articles %}
	<p>{{ article.title }}</p>
{% endfor %}
```

 ## 前提

```python
# 前提一、模板文件配置，基础配置中已配置
gzjblog/settings.py

TEMPLATES = [
    {
        ...
        # 定义模板位置
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        ...
    },
]
# 前提二、路由配置，已配置
from django.urls import path
from . import views
# 应用命名空间
app_name='article'

urlpatterns=[
    path('article_list/',views.article_list,name='article_list')
]
```

成功！虽然简陋，但是已经走通了MTV（model、template、view）环路。

## 总结

> url -> 路由 -> 视图 -> 模板

