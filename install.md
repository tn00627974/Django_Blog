# Django 專案建立與設定指引

## 1. 安裝 Django

確保你已經安裝了    和 pip。然後使用以下指令安裝 Django：

```bash
pip install django==3.1.7
2. 建立 Django 專案
使用以下命令創建一個新的 Django 專案：

bash
 
django-admin startproject firstproject
3. 建立應用程式
在專案目錄中，使用以下命令建立一個新的應用程式：

bash
 
cd firstproject
   manage.py startapp myblog
4. 設定資料庫
在 firstproject/firstproject/settings.py 文件中，設置資料庫：

  
 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}
5. 設定靜態檔案
在 firstproject/firstproject/settings.py 文件中，設置靜態檔案：

  
 
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
6. 設定時區和語言
在 firstproject/firstproject/settings.py 文件中，設置時區和語言：

  
 
LANGUAGE_CODE = 'zh-hant'
TIME_ZONE = 'Asia/Taipei'
7. 開啟開發者模式
在 firstproject/firstproject/settings.py 文件中，將 DEBUG 設置為 True：

  
 
DEBUG = True
8. 建立 templates 和 static 目錄
在專案目錄中，建立 templates 和 static 目錄，用於存放模板文件和靜態檔案。

9. 設定密碼加密
在 firstproject/firstproject/settings.py 文件中，設置密碼加密方式：


PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.MD5PasswordHasher',
    'django.contrib.auth.hashers.CryptPasswordHasher',
]


10. 設定 URL 路由
在 firstproject/firstproject/urls.py 文件中，設定 URL 路由：


