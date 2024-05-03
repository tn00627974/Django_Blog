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
from django.urls import path , include ,re_path
from myblog.views import* # 匯入 views.py 裡面的所有函式
from firstproject import testdb

# 設定路徑 對應到 views.py 中的函式
urlpatterns = [
  path('admin/', admin.site.urls), # path(網址, 函式)
   path('', djpost,name='djpost'), # 首頁 顯示所有文章
  path('sayhi/<username>',sayhi),
  path('hello3/<username>', hello3), 
  path('hello4/<username>', hello4), 
  path('dice/', dice),
  path('show/', show),
  path('djget/<name>/<city>/', djget),  
  path('index/', index), 
  path('index1/', index1),
  path('index2/', index2),
  path('index3/', index3),
  path('test/<username>', test), 
  re_path(r'db/add$', testdb.add), #  Test function to add data to database
]



