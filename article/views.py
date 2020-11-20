from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Article
from .forms import ArticleForm
from userprofile.models import User
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q

import markdown
# Create your views here.

# 视图函数
def article_list(request):
    search = request.GET.get('search')
    order = request.GET.get('order')
    # 用户搜索逻辑
    if search:
        if order == 'total_views':
            # 用 Q对象 进行联合搜索
            articles = Article.objects.filter(
                Q(title__icontains=search) |
                Q(body__icontains=search)
            ).order_by('-total_views')
        else:
            articles = Article.objects.filter(
                Q(title__icontains=search) |
                Q(body__icontains=search)
            )
    else:
        # 将 search 参数重置为空
        search = ''
        if order == 'total_views':
            articles = Article.objects.all().order_by('-total_views')
        else:
            articles = Article.objects.all()

    # 每页显示3篇文章
    paginator=Paginator(articles,3)
    # 获取url中的页码
    page=request.GET.get("page")
    # 分页对象包含的文章返回
    articles=paginator.get_page(page)

    # 需要传递给模板（templates）的对象
    context = {'articles': articles,"order":order,'search': search }
    # render函数：载入模板，并返回context对象
    return render(request, 'article/list.html',context)


def article_detail(request,id ):
    article = Article.objects.get(id=id)
    # 浏览量 +1
    article.total_views += 1
    article.save(update_fields=['total_views'])
    # 将markdown语法渲染成html样式
    # article.body = markdown.markdown(article.body,
    #     extensions=[
    #         # 包含 缩写、表格等常用扩展
    #         'markdown.extensions.extra',
    #         # 语法高亮扩展
    #         'markdown.extensions.codehilite',
    #         # 目录扩展
    #         'markdown.extensions.TOC',
    #     ])
    # context = {'article': article}

    # 修改 Markdown 语法渲染
    md = markdown.Markdown(
        extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
        ]
    )
    article.body = md.convert(article.body)

    # 新增了md.toc对象
    context = { 'article': article, 'toc': md.toc }

    return render(request,'article/detail.html',context)


@ login_required(login_url='/userprofile/login/')
def article_create(request):
    if request.method=="POST":
        # 将提交的数据赋值到表单实例中
        article_form=ArticleForm(data=request.POST)
        # 判断提交的数据是否满足模型的要求
        if article_form.is_valid():
            # 保存数据，但暂时不提交到数据库中
            new_article=article_form.save(commit=False)
            # 指定数据库中 id=1 的用户为作者
            # new_article.author=User.objects.get(id=1)
            new_article.author=User.objects.get(id=request.user.id)

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
@ login_required(login_url='/userprofile/login/')
def article_safe_delete(request,id):
    if request.method == "POST":
        article=Article.objects.get(id=id)
        # 过滤非作者的用户
        if request.user != article.author:
            return HttpResponse("抱歉，你无权修改这篇文章。")
        article.delete()
        return redirect("article:article_list")
    else:
        return HttpResponse("仅允许POST请求")

# 更新文章
@ login_required(login_url='/userprofile/login/')
def article_update(request,id):
    article=Article.objects.get(id=id)
    # 过滤非作者的用户
    if request.user != article.author:
        return HttpResponse("抱歉，你无权修改这篇文章。")
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

