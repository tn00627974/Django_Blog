from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# 定義一個 sayhello() 函式，並將其路徑設定為 / 路徑，當使用者瀏覽到網站的根目錄時，就會呼叫此函式並顯示 Hello World! 字串。
def sayhello(request):
    return HttpResponse("Hello django!")

def sayhi(request,username):
    return HttpResponse(f"Hi,歡迎光臨{username}!")

