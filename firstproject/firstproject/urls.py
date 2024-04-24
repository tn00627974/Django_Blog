"""
URL configuration for firstproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myblog.views import sayhello 
from django.http import HttpResponse

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',sayhello)
]

# 定義一個 sayhello() 函式，並將其路徑設定為 / 路徑，當使用者瀏覽到網站的根目錄時，就會呼叫此函式並顯示 Hello World! 字串。
def sayhello(request):
    return HttpResponse("Hello django!")