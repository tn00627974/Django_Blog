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
from myblog.views import* # 匯入 views.py 裡面的函式 sayhello()


urlpatterns = [
  path('admin/', admin.site.urls), # path(網址, 函式)
   path('', djpost,name='djpost'),
  path('sayhi/<username>',sayhi),
  path('hello3/<username>', hello3), # 加入 path(網址, 函式)
  path('hello4/<username>', hello4), # 加入 path(網址, 函式)
  path('dice/', dice),
  path('show/',show),
  path('djget/<name>/<city>/', djget),  # 將 name 和 city 加入路由中

  path('test/<username>', test), # 加入 path(網址, 函式)

]

