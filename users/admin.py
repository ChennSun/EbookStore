from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import AuthProfile
# Register your models here.

class AuthProfileInline(admin.StackedInline):
	model = AuthProfile
	extra = 3

class UserAdmin(UserAdmin):
	#AuthProfile在User后台页面编辑
	inlines = (AuthProfileInline,)

admin.site.unregister(User)
admin.site.register(User,UserAdmin)