from django.urls import path
from .views import *

app_name='users'
urlpatterns=[
    path('login/',auth_login,name='auth_login'),
    path('register/',register,name='register'),
    path('send_code/',send_code,name='send_code'),
]

