from django.shortcuts import render # 引入 render 函式, 這是 Django 內建的函式，用來渲染模板
from django.http import HttpResponse
from datetime import datetime # 引入 datetime 模組
from django.http import JsonResponse
import random

# Create your views here.

# 定義一個 sayhello() 函式，並將其路徑設定為 / 路徑，當使用者瀏覽到網站的根目錄時，就會呼叫此函式並顯示 Hello World! 字串。
def sayhello(request):
    return HttpResponse("Hello django!")

def sayhi(request,username):
    return HttpResponse(f"Hi,歡迎光臨{username}!")

def hello3(request,username):
    now = datetime.now() # 取得現在時間
    # render(傳遞 GET、POST, 模板名稱, 傳遞所有區域變數)
    return render(request,'hello3.html',locals()) # locals() 會將所有的區域變數傳遞到模板中

def hello4(request, username):
    now = datetime.now()
    return render(request, "hello4.html", locals()) 

def dice(request):
  no1 = random.randint(1, 6)
  no2 = random.randint(1, 6)
  no3 = random.randint(1, 6)
  # 使用 locals() 傳遞所有的區域變數
  return render(request, "dice.html", locals())

def show(request):
  person1 = {"name": "Elliot1", "phone": "0912-123456", "age": 30}
  person2 = {"name": "Elliot2", "phone": "0912-123455", "age": 31}
  person3 = {"name": "Elliot3", "phone": "0912-123466", "age": 32}
  persons = [person1, person2, person3]
  return render(request, "show.html", locals())

def djget(request,name,city):
  return render(request, "djget.html",{'name': name, 'city': city})

def djpost(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    if username == 'admin' and password == '123':
      return HttpResponse('歡迎光臨本網站!')
    else:
      return HttpResponse('帳號或密碼錯誤!')
  else:
    return render(request, "djpost.html", locals())

def index(request):
  context = {}
  context['name'] = 'Ulysses'
  return render(request, 'index.html',context)

def index1(request):
  context = {}
  context['name'] = 'Ulysses'
  return render(request, 'index1.html',context)

def index2(request):
  # 變量
  context = {}
  context['name'] = 'Ulysses'
  
  # 列表
  views_list = ["django課程","python課程","C++課程"]
  context["views_list"] = views_list
  
  # 字典
  views_dict = {"name":"程式員小飛","age":28}
  context["views_dict"] = views_dict
  
  # if/else
  score = 89
  context["score"] = score
  
  # empty list
  empty_list = []
  context["empty_list"] = empty_list
  
  return render(request, 'index2.html',context)
 

def index3(request):
     return render(request, 'index3.html')
   
   
  

def test(request,username):
    string = "Hello, " + username + "!"
    mylist = ["apple","banana","orange"]
    return JsonResponse({"string":string,"mylist":mylist})



