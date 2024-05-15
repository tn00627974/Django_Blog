# redirect 函式用來導向到其他頁面，例如說當使用者登入成功後，就會導向到首頁。

from django.shortcuts import render, redirect # 引入 render 函式, 這是 Django 內建的函式，用來渲染模板
from django.http import HttpResponse
from datetime import datetime # 引入 datetime 模組
from django.http import JsonResponse
import random
from.models import User,Post,Tag
from .forms import PostForm

# Create your views here.

# 定義一個 sayhello() 函式，並將其路徑設定為 / 路徑，當使用者瀏覽到網站的根目錄時，就會呼叫此函式並顯示 Hello World! 字串。
def index(request):
  context = {}
  context['name'] = 'Ulysses'
  return render(request, 'index.html',context)

def blog(request):
    return render(request, 'blog.html')
  
def portfolio(request):
    return render(request, 'portfolio.html')

def about(request):
    return render(request, 'about.html')



# Blog Funtion
def index(request):
    posts = Post.objects.all()
    return render(request, 'index1.html', {'posts': posts})

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'post_detail.html', {'post': post})

def new_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PostForm()
    return render(request, 'new_post.html', {'form': form})





