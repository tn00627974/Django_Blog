from django.shortcuts import render # 引入 render 函式, 這是 Django 內建的函式，用來渲染模板
from django.http import HttpResponse
from datetime import datetime # 引入 datetime 模組
from django.http import JsonResponse
import random

# Create your views here.

# 定義一個 sayhello() 函式，並將其路徑設定為 / 路徑，當使用者瀏覽到網站的根目錄時，就會呼叫此函式並顯示 Hello World! 字串。
def test(request):
    return HttpResponse("Hello django!")

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



