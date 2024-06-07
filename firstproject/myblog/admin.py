from django.contrib import admin
from myblog import models
from .models import Post
from django import forms
# from django_select2.forms import Select2MultipleWidget

admin.site.register(models.Login_User)
admin.site.register(models.Tag)
admin.site.register(models.Post)


# admin.site.register(Post, PostAdmin)

# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = '__all__'
#         widgets = {
#             'tags': Select2MultipleWidget,
#         }