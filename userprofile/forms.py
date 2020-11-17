from django import forms

# 用户登录表单
class UserLoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()
