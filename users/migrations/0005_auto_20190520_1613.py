# Generated by Django 2.2 on 2019-05-20 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20190520_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authprofile',
            name='sex',
            field=models.BooleanField(choices=[(0, 'girl'), (1, 'boy')], default=1, max_length=4, verbose_name='性别'),
        ),
    ]
