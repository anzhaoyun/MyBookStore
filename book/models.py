from django.db import models
from library.models import Library
# Create your models here.

class Book(models.Model):
    STATE_CHOICES = (
        (0,'未上架'),
        (1,'已上架')
    )
    id = models.AutoField(primary_key=True)
    name = models.CharField(db_index=True,max_length=64,help_text='图书名字')
    c_time = models.DateTimeField(auto_now_add=True,blank=True,help_text='创建时间')
    u_time = models.DateTimeField(auto_now=True,blank=True,help_text='修改时间')
    author = models.CharField(max_length=32,help_text='图书作者')
    library = models.ForeignKey(to=Library,null=True,on_delete=models.CASCADE,help_text='关联图书馆')
    publish = models.CharField(max_length=64,help_text='出版社')
    pub_time = models.DateField(help_text='出版时间')
    ISBN_code = models.CharField(max_length=36,help_text='ISBN唯一码')
    price = models.DecimalField(max_digits=5,decimal_places=2,help_text='价格')
    state = models.IntegerField(choices=STATE_CHOICES,help_text='图书状态')
