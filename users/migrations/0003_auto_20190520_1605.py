# Generated by Django 2.2 on 2019-05-20 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190520_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authprofile',
            name='birthday',
            field=models.DateField(verbose_name='生日'),
        ),
        migrations.AlterField(
            model_name='authprofile',
            name='sex',
            field=models.CharField(choices=[(1, 'girl'), (2, 'boy')], max_length=4, verbose_name='性别'),
        ),
    ]
