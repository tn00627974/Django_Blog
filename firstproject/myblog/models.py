from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
# 使用者登入資訊
class Login_User(models.Model):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    # 驗證是否為機器人
    is_bot = models.BooleanField(default=False)
    
# 部落格文章    
# 文章標題、內容、作者、建立日期、發佈日期、標籤
class Tag(models.Model):
    name = models.CharField(max_length=50)
    # 文章標籤
    def __str__(self): # __str__ 是 Python的魔法方法，它會回傳一個字串，用於在 Django 的 ORM 框架中顯示物件的字串表示
        return self.name 

class Post(models.Model):
    # 定義名為Post的資料庫模型，用於儲存文章相關資訊

    title = models.CharField(max_length=200)  # 文章標題，最大長度為200個字元
    content = models.TextField()  # 文章內容，使用TextField類型
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # 作者，使用外鍵關聯到User模型，當User刪除時刪除相應的文章
    created_date = models.DateTimeField(default=timezone.now)  # 創建日期，默認為當前時間
    published_date = models.DateTimeField(blank=True, null=True)  # 發佈日期，可以為空，允許為空值
    tags = models.ManyToManyField(Tag)  # 標籤，與Tag模型使用多對多關係

    def publish(self):
        # 定義一個名為publish的方法，用於將文章發佈，將發佈日期設置為當前時間並保存
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        # 定義當前資料模型的字串表示形式，返回文章標題
        return self.title
    
