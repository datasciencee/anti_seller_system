from django import forms
from django.db import models

class UserForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=128)
    password = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    gender = (
        ('male', "男"),
        ('female', "女"),
    )
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="确认密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="邮箱地址", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    sex = forms.ChoiceField(label='性别', choices=gender)


# class conventional_field(models.Model):
#     id = models.AutoField(int(32), primary_key=True)
#     user_id = models.CharField(max_length=255)
#
#     use_name = UserForm()
#     create_data = models.DateField(auto_now_add=True)
#     updata = models.DateField(auto_now=True)
#     logic_delete = models.BooleanField(default=False, verbose_name='逻辑删除', help_text='逻辑删除')
#
# class reverse_to_sell(models.Model):
#     wechat_id = models.CharField(max_length=255)
#     content = models.ForeignKey(conventional_field, on_delete=models.CASCADE, default='')





