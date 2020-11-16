## 配置Bootstrap 4

Bootstrap**是用于网站开发的开源前端框架（“前端”指的是展现给最终用户的界面）

在项目根目录下新建目录`static/bootstrap/`，用于存放Bootstrap静态文件。**静态文件**通常指那些不会改变的文件。Bootstrap中的css、js文件，就是静态文件。

## 编写模板

在根目录下的`templates/`中，新建三个文件：

- `base.html`是整个项目的模板基础，所有的网页都从它继承；
- `header.html`是网页顶部的导航栏；
- `footer.html`是网页底部的注脚。

> 这三个文件在每个页面中通常都是不变的，独立出来可以避免重复写同样的代码，提高维护性。

首先写`base.html`：

```html
{%  load staticfiles  %}
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    {#预留网站标题位置#}
    <title>{% block title %}{% endblock %}</title>
    {#引入bootstrap#}
    <link rel="stylesheet" href="{% static 'bootstrap/css/bootstrap.min.css' %}">
    {#其他样式文件预留位置#}
    {% block css %}{% endblock %}
</head>
<body>
    {#引入导航栏#}
    {% include "header.html" %}
    {#预留具体页面位置#}
    {% block content %}{% endblock %}
    {#引入注脚#}
    {% include "footer.html" %}

    <!-- bootstrap.js 依赖 jquery.js 和popper.js，因此在这里引入 -->
    <script src="{% static 'jquery/jquery-3.3.1.js' %}"></script>
    <!-- popper.js 采用 cdn 远程引入，在实际的开发中推荐静态文件尽量都使用 cdn 的形式。 -->
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1-lts/dist/umd/popper.min.js"></script>
    <!-- 引入bootstrap的js文件 -->
    <script src="{% static 'bootstrap/js/bootstrap.min.js' %}"></script>
    <!-- 预留自己的js文件-->
    {% block script %}{% endblock %}
</body>
</html>
```

然后是`header.html`：

```html
<!-- 定义导航栏 -->
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
  <div class="container">

    <!-- 导航栏商标 -->
    <a class="navbar-brand" href="#">我的博客</a>

    <!-- 导航入口 -->
    <div>
      <ul class="navbar-nav">
        <!-- 条目 -->
        <li class="nav-item">
          <a class="nav-link" href="#">文章</a>
        </li>
      </ul>
    </div>
  </div>
</nav>
```

其次写入`footer.html`：

```html
{% load staticfiles %}
<!-- Footer -->
<div>
    <br><br><br>
</div>
<footer class="py-3 bg-dark fixed-bottom">
    <div class="container">
        <p class="m-0 text-center text-white">Copyright &copy; www.dusaiphoto.com 2018</p>
    </div>
</footer>
```

最后改写之前的`list.html`：

```html
{% extends 'base.html' %}
{% load staticfiles %}
{% block title %}首页{% endblock %}
{% block content %}
<div class="container">
    <div class="row mt-2">

        {% for article in articles %}
        <!-- 文章内容 -->
        <div class="col-4 mb-4">
        <!-- 卡片容器 -->
            <div class="card h-100">
                <!-- 标题 -->
                <h4 class="card-header">{{ article.title }}</h4>
                <!-- 摘要 -->
                <div class="card-body">
                    <p class="card-text">{{ article.body|slice:'100' }}...</p>
                </div>
                <!-- 注脚 -->
                <div class="card-footer">
                    <a href="#" class="btn btn-primary">阅读本文</a>
                </div>
            </div>
        </div>
        {% endfor %}

    </div>
</div>
{% endblock content %}
```

## 运行服务器

运行开发服务器，在浏览器中输入`http://127.0.0.1:8000/article/article-list/`

一个漂亮的博客界面就这样出现在眼前，非常神奇。

## 总结

本章我们引入了前端框架Bootstrap 4，借助它重新组织了模板的结构，编写了一个漂亮的博客网站的首页。下一章我们将学习编写文章详情页面。

