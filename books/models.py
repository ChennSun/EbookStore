from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Book(models.Model):
    TAG_CHOICES = [
    ('Python','Python相关书籍'),
    ('linux','linux相关书籍'),
    ('Java','Java相关书籍'),
    ('Redis','Redis相关书籍'),
    ('Mysql','Mysql相关书籍'),
    ('Docker','Docker相关书籍'),
    ('Html_css_javascript','html+css+javascript相关书籍')
    ]
    FREE_CHOICES = [
    (1,'免费'),
    (0,'收费')
    ]
    name = models.CharField(
        max_length = 50,
        unique = True,
        db_index = True,
        verbose_name='书名'
        )
    author = models.CharField(
        max_length = 10,
        verbose_name='作者'
#       index
        )
    summary = models.CharField(
        max_length = 70,
        verbose_name='摘要'
        )
    publish = models.CharField(
        max_length = 50,
        verbose_name ='出版社'
        )
    free = models.BooleanField(
        choices = FREE_CHOICES,
        default = 1,
        verbose_name = '是否免费'
        )
    tag = models.CharField(
        max_length = 20,
        choices = TAG_CHOICES,
        db_index = True,
        verbose_name = '书籍类型'
        )
    collect_user = models.ManyToManyField(
        User,
        verbose_name='收藏者'
        )
    collect_num = models.IntegerField(
        default=0,
        verbose_name='收藏数'
        )
    test_read = models.TextField(
        verbose_name='试读部分'
        )
    book_cover = models.ImageField(
        upload_to='cover/%Y/%m/%d',
        verbose_name = '封面',
        blank=True,
        default = 'cover/default.jpg'
        )
    book_file = models.FileField(
        upload_to='file/%Y/%m/%d',
        default = 'file/default.txt',
        blank=True,
        verbose_name = '书籍主体'
        )

    class Meta:
        verbose_name = '书籍'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


