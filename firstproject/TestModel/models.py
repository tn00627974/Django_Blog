from django.db import models

# Create your models here.

# TeseModel 資料表
class Test(models.Model):
    name = models.CharField(max_length=20) # 名字
    age = models.IntegerField() # 年齡
    email = models.EmailField() # 電子郵件

# 使用者登入資訊
class User(models.Model):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    # 驗證是否為機器人
    # is_bot = models.BooleanField(default=False)

# 新建資料庫
# class 



