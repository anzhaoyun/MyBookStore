# Generated by Django 3.2.5 on 2021-07-21 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='图书馆名字', max_length=48)),
                ('c_time', models.DateField(auto_now_add=True, help_text='创建日期')),
                ('u_time', models.DateField(auto_now=True, help_text='更新日期')),
                ('address', models.CharField(help_text='地址', max_length=256)),
                ('e_mail', models.EmailField(blank=True, default=None, help_text='电子邮件地址', max_length=254, unique=True)),
                ('tel_number', models.CharField(blank=True, default=None, help_text='电话号码', max_length=11)),
                ('img', models.ImageField(blank=True, default=None, help_text='图片', upload_to='')),
            ],
        ),
    ]