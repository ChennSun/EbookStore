from django.urls import path
from .views import *

app_name='users'
urlpatterns=[
    path('login/',auth_login,name='auth_login'),
    path('register/',register,name='register'),
    path('send_code/',send_code,name='send_code'),
    path('logout/',auth_logout,name='auth_logout'),
    path('profile/<int:pk>',ProfileView.as_view(),name='auth_profile'),
]

