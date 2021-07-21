from django.db import models
# Create your models here.

class Library(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 48,help_text='图书馆名字')
    c_time = models.DateField(auto_now_add = True,blank=True,help_text='创建日期')
    u_time = models.DateField(auto_now = True,blank=True,help_text='更新日期')
    address = models.CharField(max_length=256,help_text='地址')
    e_mail = models.EmailField(unique=True,blank=True,null=True,default=None,help_text='电子邮件地址')
    tel_number = models.CharField(max_length= 11,null=True,blank=True,default=None,help_text='电话号码')
    img = models.ImageField(blank=True,null=True,default=None,help_text='图片',max_length=300)