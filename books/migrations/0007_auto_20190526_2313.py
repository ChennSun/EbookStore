# Generated by Django 2.2 on 2019-05-26 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_auto_20190526_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='summary',
            field=models.CharField(max_length=70, verbose_name='摘要'),
        ),
    ]
