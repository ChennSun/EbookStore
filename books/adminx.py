import xadmin
from .models import Book

#创建注册类
class BookAdmin(object):
    pass

xadmin.site.register(Book, BookAdmin)