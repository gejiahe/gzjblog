from django import forms
# from django.contrib.auth.models import User
from .models import User
# 用户登录表单
class UserLoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()

# 用户注册表单
class UserRegisterForm(forms.ModelForm):
    password=forms.CharField()
    password2=forms.CharField()

    class Meta:
        model=User
        fields=["username","email"]

    # 对两次输入的密码是否一致进行检查
    def clean_password2(self):
        data=self.cleaned_data
        if data.get("password") == data.get("password2"):
            return data.get("password")
        else:
            raise forms.ValidationError("两次密码输入不一致，请重试。")

# 用户编辑表单
class UserEditForm(forms.ModelForm):
    class Meta:
        model=User
        fields=("phone",'avatar',"desc","org")
