# 建立 Django 專案與設定指引

## 1. 確認環境與安裝 Django

```bash
python3 --version
brew install python
```
```
python3 --version
pip3 --version
pip3 install --upgrade pip
pip3 install django==3.1.7
pip3 list
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
markdown降價
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
