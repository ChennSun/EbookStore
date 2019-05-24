from django.shortcuts import render,render_to_response,redirect,reverse,HttpResponse
from django.template import loader
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.views import generic
from django.utils.decorators import method_decorator
from celery_tasks.tasks import celery_send_code
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from .forms import LoginForm,RegisterForm
import random

# Create your views here.

#使用login作为视图函数名称会使django自带的login失效
def auth_login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            email = login_form.cleaned_data.get('email')
            password = login_form.cleaned_data.get('password')
            login_auto = login_form.cleaned_data.get('login_auto')

            try:
                user=User.objects.get(email=email)
            except User.DoesNotExist:
                user=None
            if user is None:
                messages.add_message(request, messages.INFO, '用户名不存在')
                return render(request,'users/login.html',{'form':login_form})

            username=user.username
            #用户认证
            user=authenticate(request,username=username,password=password)
            if user is None:
                messages.add_message(request, messages.INFO, '密码错误')
                return render(request,'users/login.html',{'form':login_form})

            #checkbox返回值为'False',非布尔值False
            if login_auto == 'False':
                request.session.set_expiry(3600)
            login(request,user)
            #登录成功之后跳转next_url，默认首页
            next_url = request.GET.get('next', reverse('books:index'))
            return redirect(next_url)
    login_form = LoginForm()
    return render(request,'users/login.html',{'form':login_form})

def register(request):
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        #检查数据是否可用并获取数据
        if register_form.is_valid():
            username = register_form.cleaned_data.get('username')
            email = register_form.cleaned_data.get('email')
            password1 = register_form.cleaned_data.get('password1')
            password2 = register_form.cleaned_data.get('password2')
            code = register_form.cleaned_data.get('code')

            #校验email是否重复
            try:
                user1 = User.objects.get(email=email)
            except User.DoesNotExist:
                user1 = None
            if user1 is not None:
                messages.add_message(request, messages.INFO, 'email已存在')

            #校验用户名是否重复
            try:
                user2 = User.objects.get(username=username)
            except User.DoesNotExist:
                user2 = None
            if user2 is not None:
                messages.add_message(request, messages.INFO, '用户名已存在')

            #验证码时效性正确性校验
#            send_code = request.session.get('code',None)
            send_code = cache.get('send_code',None)
            if send_code is None:
                messages.add_message(request, messages.INFO, '验证码已过期')
            elif code != send_code:
                messages.add_message(request, messages.INFO, '验证码错误')

            #验证通过创建用户
            if user1 is None and user2 is None:
                User.objects.create_user(username=username,email=email,password=password1)
                return redirect(reverse('users:auth_login'))
        else:
            return render(request,'users/register.html',{'form':register_form})
    #get请求返回空白表单
    register_form = RegisterForm()
    return render(request,'users/register.html',{'form':register_form})

def auth_logout(request):
    logout(request)
    return redirect(reverse('books:index'))


class ProfileView(generic.DetailView):
    model=User
    template_name='users/profile.html'

    @method_decorator(login_required,cache_page(60 * 15))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

def send_code(request):
    email_to=request.POST.get('email',None)
    #生成激活码
    code=random.randint(1000,9999)
    code=str(code)
    #存入cache
    cache.set('send_code',code,60)
    title = "注册验证码--sunの书屋"
    content_html =loader.render_to_string('users/email/email.html',{'code':code})
    email_from = settings.DEFAULT_FROM_EMAIL
    reciever = [
        email_to
    ]
    celery_send_code.delay(title,content_html,email_from,reciever)
    response=HttpResponse('验证码已发送至您的邮箱')
    return response