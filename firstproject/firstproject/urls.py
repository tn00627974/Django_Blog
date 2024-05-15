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

# 設定路徑 對應到 views.py 中的函式
urlpatterns = [
    path('admin/', admin.site.urls), # path(網址, 函式)
    path('', index,name='index'), # 首頁 顯示所有文章
    path('blog/',blog,name='blog'), # 文章 顯示所有文章 
    path('Portfolio/',portfolio,name='portfolio'), # 文章 顯示所有文章 
    path('about/',about,name='about'), # 文章 顯示所有文章 
    
    # Blog 文章
    path('post_detail/<int:post_id>/',post_detail,name='post_detail'),
    path('new_post/',post_detail,name='new_post'),
#   re_path(r'db/add$', testdb.add), #  新增資料庫資料 
]



