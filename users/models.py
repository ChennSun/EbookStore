from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class AuthProfile(models.Model):
    SEX_CHOICES=[
        #(数据库存储字段，用户可读字段)
        (0,'girl'),
        (1,'boy')
        ]
    user = models.OneToOneField(
        User,
        on_delete = models.CASCADE,
        verbose_name = '用户'
        )
    sex = models.BooleanField(
        max_length = 4,
        choices = SEX_CHOICES,
        default = 1,
        verbose_name = '性别'
        )
    birthday = models.DateField(
#       auto_now_add = True,
        default='2019-05-20',
        verbose_name = '生日'
        )
    user_ico = models.ImageField(
        upload_to='ico/%Y/%m/%d',
        default='ico/default.jpg',
#       height=20,
#       width=20,
        verbose_name = '用户头像'
        )

    class Meta:
        verbose_name = '用户资料'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.username

#使用django的signal实现创建用户自动生成用户资料,与Flask中db.event.listen有些相似。
@receiver(post_save,sender=User)
def update_profile(sender,instance=None,created=False,**kwargs):
#   instance:保存的新User实例
#    sender: 模型类
#    created：创建了新纪录则为True，admin登录后台界面时也会有post_save信号量产生
#             如果不进行created判断的话reciver就会创建一个新实例，若数据库中已
#             经有依赖admin的实例，则与OneToOneField冲突，导致服务器崩溃。
#    update_fields:Model.save()要更新的字段集，如果没有传递则为None

    if created:
        auth_profile=AuthProfile(user=instance)
        print('receive!')
        auth_profile.save()