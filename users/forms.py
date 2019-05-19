import re
from django import forms

#登录表单
class LoginForm(forms.Form):
    email = forms.CharField(
        label='电子邮箱',
        max_length=128,
        widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'})
        )
    password = forms.CharField(
        label='密码',
        max_length=256,
        widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'})
        )
    login_auto=forms.CharField(required=False,widget=forms.CheckboxInput())

#注册表单
class RegisterForm(forms.Form):
    username = forms.CharField(
        label='用户名',
        max_length=128,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'})
        )
    email = forms.CharField(
        label='电子邮箱',
        max_length=128,
        widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'})
        )
    password1 = forms.CharField(
        label='密码',
        max_length=256,
        widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'})
        )
    password2 = forms.CharField(
        label='确认密码',
        max_length=256,
#       validators = [password_validate,],
        widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'})
        )
    code = forms.CharField(
        label='邮箱验证码',
        max_length=128,
        widget=forms.TextInput(attrs={'class':'form-control'})
        )
    def clean(self):
        password1 = self.cleaned_data['password1']
        email = self.cleaned_data['email']
        username = self.cleaned_data['username']
        password2=self.cleaned_data.get('password2')
        if password1 == email or password1 == username:
            #将错误分配给每个字段，raise方法会返回整个表的错误
            self.add_error('password1','密码不能和用户名或邮箱相同')
#        if not re.match(r"^.*(?=.{6,})(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[!@#$%^&*? ]).*$",password1):
#            self.add_error('password1','密码最少6位包括至少1个大写字母，1个小写字母，1个数字，1个特殊字符')
        if password1!=password2:
            self.add_error('password2','两次密码不一致')
        return self.cleaned_data

'''单字段判断时，由于判断时涉及字段较多，password1报错之后会删除数据，导致cleaned_data['password']无法提取，影响后续判断
https://docs.djangoproject.com/en/2.2/ref/forms/validation/#raising-validation-error
    def clean_password2(self):
        password2=self.cleaned_data.get('password2')
        password1=self.cleaned_data.get('password1')
        if password1!=password2:
            raise forms.ValidationError('两次密码不一致')
            print(password2)
        return password2

    def clean_password1(self):
        password1 = self.cleaned_data['password1']
        email = self.cleaned_data['email']
        username = self.cleaned_data['username']
        if password1 == email or password1 == username:
            raise forms.ValidationError('密码不能和用户名或邮箱相同')
        if not re.match(r"^.*(?=.{6,})(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[!@#$%^&*? ]).*$",password1):
            raise forms.ValidationError('密码最少6位包括至少1个大写字母，1个小写字母，1个数字，1个特殊字符')
        return password1
'''


