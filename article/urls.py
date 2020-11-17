from django.urls import path
from . import views
# 应用命名空间
app_name='article'

urlpatterns=[
    path('article_list/',views.article_list,name='article_list'),
    path('article_create/',views.article_create,name='article_create'),
    path('article_detail/<int:id>/',views.article_detail,name='article_detail'),
    # 不安全的删除文章
    path('article_delete/<int:id>/',views.article_delete,name='article_delete'),
    # 安全的删除文章
    path('article_safe_delete/<int:id>/',views.article_safe_delete,name='article_safe_delete'),
    path('article_update/<int:id>/',views.article_update,name='article_update'),
]
