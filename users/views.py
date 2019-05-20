import random
from django.shortcuts import render,render_to_response,redirect,reverse,HttpResponse
from .forms import LoginForm,RegisterForm
from django.template import loader
from django.core.mail import send_mail,EmailMessage
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.views import generic
from django.utils.decorators import method_decorator

# Create your views here.

#使用login作为视图函数名称会使django自带的login失效
def auth_login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            email = login_form.cleaned_data.get('email')
            password = login_form.cleaned_data.get('password')
            try:
                user=User.objects.get(email=email)
            except User.DoesNotExist:
                user=None
            if user is None:
                messages.add_message(request, messages.INFO, '用户名不存在')
                return render(request,'users/login.html',{'form':login_form})
            username=user.username
            user=authenticate(request,username=username,password=password)
            if user is None:
                messages.add_message(request, messages.INFO, '密码错误')
                return render(request,'users/login.html',{'form':login_form})
            login(request,user)
            return redirect(reverse('books:index'))
    login_form = LoginForm()
    return render(request,'users/login.html',{'form':login_form})

def register(request):
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        #检查数据是否可用
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
            #查询code是否正确
            if user1 is None and user2 is None:
                User.objects.create_user(username=username,email=email,password=password1)
                return redirect(reverse('users:auth_login'))
        else:
            return render(request,'users/register.html',{'form':register_form})
    register_form = RegisterForm()
    return render(request,'users/register.html',{'form':register_form})

def auth_logout(request):
    logout(request)
    return redirect(reverse('books:index'))


class ProfileView(generic.DetailView):
    model=User
    template_name='users/profile.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

def send_code(request):
    recive=request.POST.get('email',None)
    print(recive)
    code=random.randint(1000,9999)
    code=str(code)
    title = "注册验证码--sunの书屋"
    content_html =loader.render_to_string('users/email/email.html',{'code':code})
    email_from = settings.DEFAULT_FROM_EMAIL
    reciever = [
        recive
    ]
    msg=EmailMessage(title,content_html,email_from,reciever)
    msg.content_subtype='html'
    msg.send()
    return HttpResponse('验证码已发送至您的邮箱')