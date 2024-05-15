from django import forms
from.models import User,Post,Tag

class PostForm(forms.ModelForm):
    class Meta :
        model = Post
        fields = ['title','content','tags']