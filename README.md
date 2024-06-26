# 這是一個使用Django架設部落格的Blog網站

- 提供了HTML、CSS、JS的頁面呈現，
- 可以自動新增與更新網頁文章的數量和標籤內容，
- 提供作品集及自我介紹的頁面。

![image](https://github.com/tn00627974/Django_Blog/assets/139155210/e64f4ea8-ad43-4b56-a9d0-52913475593b)
![image](https://github.com/tn00627974/Django_Blog/assets/139155210/3947b116-7590-4777-80c3-1c0e4760f51b)

---
# Django Blog 目標開發 

- [x] 先測試部落格功能 
- [ ] 未來首頁功能是? `目前跟Blog為同一頁`
- [x] 介面優化及設計
- [x] 作品集
- [x] 關於我
- [ ] 佈署Azure or PythonAnywhere

# Django Blog 功能開發

- [x] Django連結template 用HTML ,CSS ,Bootstrap 美化介面 
- [x] 建立Mysql資料庫表格(本地端)
- [x] 部落格新增文章 or 刪除文章 (admin後台)
- [x] 發文日期,會員名稱
- [x] HTML新增文章後,要怎麼自動多一頁HTML
- [x] HTML文章上傳圖片url
- [x] HTML新增程式碼框 (Pygments的CodeHilite擴展)
- [x] 文章內容支援為Markdown語法
- [x] Markdown程式碼區域複製功能
- [x] 部落格文章五頁以上要換頁 [1,2,3,4,5...好幾頁]
- [x] 部落格文章 分類標籤
- [x] 右側顯示 標籤名稱 和 標籤總數量
- [x] tags_with_counts 之後要顯示所有文章的數量 & 分類文章的數量

# Bug fix

- [x] 分頁書籤 會多一個空白
- [x] 標籤連結 篩選只有 該標籤的內容
- [x] 作品集 css樣板有衝突
- [x] 關於我 內容要更新

# 建立 Django 專案與設定指引

## 1. 確認環境與安裝 Django

```
python --version
pip install --upgrade pip
pip install django
pip list
```
## 2. 建立 Django 專案與應用程式
```bash
django-admin startproject firstproject
cd firstproject
```
```
python manage.py startapp myblog
```
## 3. 專案目錄結構
```
firstproject/
├── manage.py
└── firstproject/
    ├── __init__.py
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
└── myblog/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── migrations/
    ├── models.py
    ├── tests.py
    └── views.py
```
## 4. 建立 templates 與 static 目錄
```python
mkdir templates
mkdir static
```
## 5. 設定 Django 環境
settings.py 設定
```
LANGUAGE_CODE = 'zh-hant'
TIME_ZONE = 'Asia/Taipei'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

DEBUG = True
```

## 6.在settings.py加入TEMPLATES資料夾 
```python
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"], # 加上 templates 目錄
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
```

## 7.引入 bootstap 到Django

- 下載 https://getbootstrap.com/docs/5.3/getting-started/download/
![image](https://github.com/tn00627974/Django_Blog/assets/139155210/734bf08e-5791-4596-b99b-38e574828e15)


- 點選 Docs > Download  > bootstrap-5.3.3-dist解壓縮後放至以下<pluguns資料夾路徑>
- H:\我的雲端硬碟\Github專案\Django_Blog\firstproject\static\pluguns

將bootstrap.css加入在HTML呈現CSS
```html
<head>
  <meta charset='utf-8'>
  <title>{{name}}</title>
  <link rel="stylesheet" href="/static/pluguns/bootstrap-5.3.3-dist/css/bootstrap.css">
</head>
```

## 8. 啟動Django資料庫
創建表格結構資料庫
```
python manage.py migrate
```
從firstproject\TestModel\models.py的class創建資料型態 , (此時還沒有建立表格)
```
python manage.py makemigrations  
```
創建資料型態後 , 以下以下指令就可以使用 Django 創建Mysql Table
```
python manage.py migrate TestModel
```
