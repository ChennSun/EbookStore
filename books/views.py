from django.shortcuts import render,redirect,reverse
from django.views import generic
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Book

# Create your views here.
def index(request):
    hot_book_list = Book.objects.order_by("-collect_user")[:4]
    book_list = Book.objects
    book_tag_list = {
        'Python':book_list.filter(tag = 'python'),
        'Linux':book_list.filter(tag = 'linux'),
        'Java':book_list.filter(tag = 'Java'),
        'Redis':book_list.filter(tag = 'Redis'),
        'Mysql':book_list.filter(tag = 'Mysql'),
        'Docker':book_list.filter(tag = 'Docker'),
        'Html+css+javascript':book_list.filter(tag = 'Html_css_javascript')
        }
    context = {
        "hot_book_list":hot_book_list,
        "book_tag_list":book_tag_list
        }
    return render(request,'books/index.html',context)

class RankView(generic.ListView):
    template_name = 'books/rank.html'
    context_object_name = 'rank_list'

    def get_queryset(self):
        return Book.objects.order_by('-collect_user')[:4]

class FreeView(generic.ListView):
    template_name = 'books/free.html'
    context_object_name = 'free_list'

    def get_queryset(self):
        return Book.objects.filter(free=1)

class AllView(generic.ListView):
    template_name = 'books/all.html'
    context_object_name = 'all_list'

    def get_queryset(self):
        books=Book.objects.all()
        paginator = Paginator(books,5)

        page=self.request.GET.get('page')
        book = paginator.get_page(page)
        return book

class BookView(generic.View):

    @method_decorator(login_required)
    def get(self,request,pk):
        book = Book.objects.get(pk=pk)
        return redirect(book.book_file.url)

@login_required
def collect_book(request,id):
    user=request.user
    book = Book.objects.get(pk=id)
    if user in book.collect_user.all():
        book.collect_user.remove(user)
        messages.add_message(request, messages.INFO, '取消收藏')
    else:
        book.collect_user.add(user)
        messages.add_message(request, messages.INFO, '收藏成功')
    return redirect(reverse('books:index'))


