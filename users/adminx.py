import xadmin
from .models import AuthProfile
from django.contrib.auth.models import User

#创建注册类
class AuthProfileAdmin(object):
    pass

xadmin.site.register(AuthProfile, AuthProfileAdmin)