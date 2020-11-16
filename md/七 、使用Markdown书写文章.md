## 安装markdown

**Markdown**是一种轻量级的标记语言，它允许人们“使用易读易写的纯文本格式编写文档，然后转换成有效的或者HTML文档。

>  安装markdown也很简单：进入虚拟环境，输入指令`pip install markdown`即可。

## 使用Markdown

为了将Markdown语法书写的文章渲染为HTML文本，首先改写`article/views.py`的`article_detail()`：

```python
# article/views.py

import markdown
def article_detail(request,id ):
    article = Article.objects.get(id=id)
    # 将markdown语法渲染成html样式
    article.body = markdown.markdown(article.body,
         extensions = [
             # 包含 缩写、表格等常用扩展
             'markdown.extensions.extra',
             # 语法高亮扩展
             'markdown.extensions.codehilite',
         ])
    context = {'article': article}
    return render(request,'article/detail.html',context)

```

然后，修改`templates/article/detail.html`中有关文章正文的部分：

```python
# templates/article/detail.html

# 在 article.body 后加上 |safe 过滤器
<p>{{ article.body|safe }}</p>
```

这样就把Markdown语法配置好了。

很好，但是代码块还是不怎么好看。

写技术文章没有代码高亮怎么行。继续努力。

## 代码高亮

在`static`目录中新建一个目录`md_css/`，一会儿放置代码高亮的样式文件。

1. 在terminal中，安装Pygments：`pip install Pygments`
2. 在terminal中，输入Pygments指令：

```bash
pygmentize -S monokai -f html -a .codehilite > monokai.css
```

**这里有一点需要注意, 生成命令中的 -a 参数需要与真实页面中的 CSS Selector 相对应，即`.codehilite`这个字段在有些版本中应写为`.highlight`**。

回车后检查一下，在`md_css`目录中是否自动生成了一个叫`monokai.css`的文件，这是一个深色背景的高亮样式文件。

接下来我们在`base.html`中引用这个文件：

```python
# templates/base.html
<head>
    ...
    <!-- 引入monikai.css -->
    <link rel="stylesheet" href="{% static 'md_css/monokai.css' %}">
</head>
```

重启服务器，顺利的话代码高亮终于现身了。

> 除了Monokai这个深色的样式外，Pygments还内置了很多其他的样式，这个就看喜好选择了。

>  `pygments`的表格样式太难看了，自己从零定制表格样式又太麻烦，怎么办？博主的处理办法偷了个懒，在页面中用`Jquery`动态加载了`Bootstrap`的表格样式

```python
# 这是代码示例
<script src="https://cdn.bootcss.com/jquery/3.3.1/jquery.min.js"></script>
<script>
    $('div#article_body table').addClass('table table-bordered');
    $('div#article_body thead').addClass('thead-light');
</script>
```

## 总结

本章引进了Markdown语法以及代码高亮扩展，从此可以写排版漂亮的文章正文了。

下一章将学习如何创建一篇新的文章。

