from django.urls import re_path
from .views import *

app_name='books'
urlpatterns=[
    re_path(r'^$',index,name='index'),
    re_path(r'^detail/(?P<pk>[0-9]*)/$',BookView.as_view(),name='detail'),
    re_path(r'^collect/(?P<id>[0-9]*)/$',collect_book,name='collect_book'),
    re_path(r'^rank/$',RankView.as_view(),name='rank'),
    re_path(r'^free/$',FreeView.as_view(),name='free'),
    re_path(r'^all/$',AllView.as_view(),name='all'),
]

