from django.urls import path
from . import views
# 应用命名空间
app_name='article'

urlpatterns=[
    path('article_list/',views.article_list,name='article_list')
]
