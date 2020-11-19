from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Org(models.Model):
    # 单位名称
    name=models.CharField(max_length=50)

    class Meta:
        verbose_name="单位"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.name

class User(AbstractUser):
    # 电话号码字段
    phone = models.CharField(max_length=20, blank=True)
    # 头像
    avatar = models.ImageField(upload_to='avatar/%Y%m%d/', blank=True)
    # 个人简介
    desc = models.TextField(max_length=500, blank=True)
    # 所属单位
    org=models.ForeignKey('Org',null=True,on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
