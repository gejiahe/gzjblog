from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Article
from .forms import ArticleForm
from django.contrib.auth.models import User
import markdown
# Create your views here.

# 视图函数
def article_list(request):
    # 取出所有博客文章
    articles = Article.objects.all()
    # 需要传递给模板（templates）的对象
    context = {'articles': articles}
    # render函数：载入模板，并返回context对象
    return render(request, 'article/list.html',context)
    # return render(request, 'base.html')


def article_detail(request,id ):
    article = Article.objects.get(id=id)
    # 将markdown语法渲染成html样式
    article.body = markdown.markdown(article.body,
                                     extensions=[
                                         # 包含 缩写、表格等常用扩展
                                         'markdown.extensions.extra',
                                         # 语法高亮扩展
                                         'markdown.extensions.codehilite',
                                     ])
    context = {'article': article}
    return render(request,'article/detail.html',context)


def article_create(request):
    if request.method=="POST":
        # 将提交的数据赋值到表单实例中
        article_form=ArticleForm(data=request.POST)
        # 判断提交的数据是否满足模型的要求
        if article_form.is_valid():
            # 保存数据，但暂时不提交到数据库中
            new_article=article_form.save(commit=False)
            # 指定数据库中 id=1 的用户为作者
            new_article.author=User.objects.get(id=1)
            # 将新文章保存到数据库中
            new_article.save()
            return redirect("article:article_list")
        else:
            return HttpResponse("表单内容有误，请重新填写")
    else:
        article_form=ArticleForm()
        context = {"article_form":article_form}
        return render(request,"article/create.html",context)

# 普通不安全的删除方式
def article_delete(request,id):
    # 根据ID获取需要删除的文章
    article=Article.objects.get(id=id)
    # 调用.delete()方法删除文章
    article.delete()
    # 完成删除后返回文章列表
    return redirect("article:article_list")

# 安全的删除方式
def article_safe_delete(request,id):
    if request.method == "POST":
        article=Article.objects.get(id=id)
        article.delete()
        return redirect("article:article_list")
    else:
        return HttpResponse("仅允许POST请求")

# 更新文章
def article_update(request,id):
    article=Article.objects.get(id=id)
    if request.method== 'POST':
        article_form=ArticleForm(data=request.POST)
        if article_form.is_valid():
            article.title=request.POST.get('title')
            article.body=request.POST.get('body')
            article.save()
            return redirect("article:article_detail",id=id)
        else:
            return HttpResponse("表单内容有误，请重新填写。")
    else:
        # article_form=ArticleForm()
        # context={"article":article,"article_form":article_form}
        # article_form前端没有使用,不用传到前台
        context={"article":article}
        return render(request,"article/update.html",context)

