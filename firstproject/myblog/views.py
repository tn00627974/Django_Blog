# redirect 函式用來導向到其他頁面，例如說當使用者登入成功後，就會導向到首頁。

from django.shortcuts import render, redirect # 引入 render 函式, 這是 Django 內建的函式，用來渲染模板
from django.http import HttpResponse
from datetime import datetime # 引入 datetime 模組
from django.http import JsonResponse
import random
from.models import User,Post,Tag
from .forms import PostForm
import markdown

# 首頁 : 顯示所有文章
def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})

# blog 同 index 頁面
# def blog(request):
#     return render(request, 'blog.html')
  
# 作品集
def portfolio(request):
    return render(request, 'portfolio.html')

# 關於我
def about(request):
    return render(request, 'about.html')

# blog_post_detail 頁面 (顯示單篇文章) 
def blog_post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    md = markdown.Markdown(extensions=["fenced_code","codehilite"])
    post.content = md.convert(post.content)
    return render(request, 'blog_post_detail.html', {'post': post})


def new_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PostForm()
    return render(request, 'new_post.html', {'form': form})


# from pytube import YouTube
# def youtube_music(request):
#     # yt = YouTube(youtube_url)
#     # audio = yt.streams.filter(only_audio=True).first()
    
#     # # 設定檔案名稱
#     # response = HttpResponse(content_type="audio/mpeg")
    
#     # # 將音訊資料寫入 response
#     # # response.write(audio.stream.stream())
#     # response.write(audio.stream.read())
#     return render (request, 'youtube_music.html')

# def markdown_content_view(request):
#     md = markdown.Markdown(extensions=["fenced_code"])
#     markdown_content = MarkdownContent.objects.first()
#     markdown_content.content = md.convert(markdown_content.content)
#     context = {"markdown_content": markdown_content}
#     return render(
#         request,
#         "post_detail.html",
#         context=context
#     )





