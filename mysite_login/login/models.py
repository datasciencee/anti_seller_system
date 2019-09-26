from django.db import models

# Create your models here.

class User(models.Model):
    '''用户表'''

    gender = (
        ('male', '男'),
        ('female', '女'),
    )

    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32, choices=gender, default='男')
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['c_time']
        verbose_name = '用户'
        verbose_name_plural = '用户'

class conventional_field(models.Model):
    id = models.AutoField(int(32), primary_key=True)
    user_id = models.CharField(max_length=255)
    use_name = models.CharField(max_length=128, unique=True)
    create_data = models.DateField(auto_now_add=True)
    updata = models.DateField(auto_now=True)
    logic_delete = models.BooleanField(default=False, verbose_name='逻辑删除', help_text='逻辑删除')

class reverse_to_sell(models.Model):
    wechat_id = models.CharField(max_length=255)
    content = models.ForeignKey(conventional_field, on_delete=models.CASCADE, default='')
    content1 = models.CharField(default=0, max_length=255)

