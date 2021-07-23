from rest_framework import serializers
from library.models import Library
def look_email(value):
    if '@' not in value:
        raise serializers.ValidationError("The email address not be allowed.")
class LibrarySerializer(serializers.Serializer):
    '''图书馆的序列化器'''
    id = serializers.IntegerField(label='ID', read_only=True)
    name = serializers.CharField(max_length=48, help_text='图书馆名字')
    c_time = serializers.DateField(required=False, help_text='创建日期')
    u_time = serializers.DateField(required=False, help_text='更新日期')
    address = serializers.CharField(max_length=256, help_text='地址')
    e_mail = serializers.EmailField(required=False, help_text='电子邮件地址',validators=[look_email])
    tel_number = serializers.CharField(max_length=11, required=False, help_text='电话号码')
    img = serializers.ImageField(required=False, help_text='图片', max_length=300)

    def validate_name(self,value):     #对某一个字段进行验证
        if '图书馆' not in value:
            raise serializers.ValidationError("The name not a library name.",code= 501)
        return value
    def validate(self, attrs):        #对attrs多个字段进行验证
        name = attrs['name']
        address = attrs['address']
        if ('图书馆' not in name) or (address not in ['北京','上海','深圳','广州']):
            raise serializers.ValidationError("library name or address not pass valid!",code= 502)
        return attrs

    def create(self, validated_data):
        library = Library.objects.create(**validated_data)
        return library

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name')
        instance.address = validated_data.get('address')
        instance.save()
        return instance