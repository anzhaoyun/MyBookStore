# Generated by Django 3.2.5 on 2021-07-21 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_auto_20210721_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='library',
            name='img',
            field=models.ImageField(blank=True, default=None, help_text='图片', max_length=300, null=True, upload_to=''),
        ),
    ]
