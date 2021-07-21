from rest_framework import serializers
from library.models import Library
class LibrarySerializer(serializers.Serializer):
    '''图书馆的序列化器'''
    id = serializers.IntegerField(label='ID',read_only=True)
    name = serializers.CharField(max_length=48, help_text='图书馆名字')
    c_time = serializers.DateField(auto_now_add=True, blank=True, help_text='创建日期')
    u_time = serializers.DateField(auto_now=True, blank=True, help_text='更新日期')
    address = serializers.CharField(max_length=256, help_text='地址')
    e_mail = serializers.EmailField(unique=True, allow_blank=True, default=None, help_text='电子邮件地址')
    tel_number = serializers.CharField(max_length=11, allow_blank=True, default=None, help_text='电话号码')
    img = serializers.ImageField(allow_null=True, default=None, help_text='图片')