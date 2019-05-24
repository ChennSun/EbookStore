from django.urls import re_path
from .views import *

app_name='users'
urlpatterns=[
    re_path(r'^login/$',auth_login,name='auth_login'),
    re_path(r'^register/$',register,name='register'),
    re_path(r'^send_code/$',send_code,name='send_code'),
    re_path(r'^logout/$',auth_logout,name='auth_logout'),
    re_path(r'^profile/(?P<pk>[0-9]*)/$',ProfileView.as_view(),name='auth_profile'),
]

