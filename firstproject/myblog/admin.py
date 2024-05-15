from django.contrib import admin
from myblog import models

admin.site.register(models.Login_User)
admin.site.register(models.Tag)
admin.site.register(models.Post)