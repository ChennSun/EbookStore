import xadmin
from .models import AuthProfile
from django.contrib.auth.models import User

#创建注册类
class AuthProfileInline(object):
    model = AuthProfile
    extra = 3

class UserAdmin(object):
    inlines = [AuthProfileInline,]

xadmin.site.unregister(User)
xadmin.site.register(User, UserAdmin)