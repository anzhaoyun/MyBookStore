# Generated by Django 3.2.5 on 2021-07-23 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_alter_library_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='library',
            name='name',
            field=models.CharField(help_text='图书馆名字', max_length=48, unique=True),
        ),
    ]