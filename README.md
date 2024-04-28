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


