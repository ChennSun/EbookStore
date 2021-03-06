# Generated by Django 2.2 on 2019-05-22 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='书名'),
        ),
        migrations.AlterField(
            model_name='book',
            name='tag',
            field=models.CharField(choices=[('Python', 'Python相关书籍'), ('linux', 'linux相关书籍'), ('Java', 'Java相关书籍'), ('Redis', 'Redis相关书籍'), ('Mysql', 'Mysql相关书籍'), ('Docker', 'Docker相关书籍'), ('Html_css_javascript', 'html+css+javascript相关书籍')], db_index=True, max_length=10, verbose_name='书籍类型'),
        ),
    ]
