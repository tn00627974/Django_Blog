from django.core.paginator import Paginator # 顯示文章列表的函式
from django.db.models import Count # 顯示文章總數的函式

# redirect 函式用來導向到其他頁面，例如說當使用者登入成功後，就會導向到首頁。
from django.shortcuts import render, redirect , get_object_or_404 # 引入 render 函式, 這是 Django 內建的函式，用來渲染模板
from django.http import HttpResponse
from django.http import JsonResponse
import random
from datetime import datetime # 引入 datetime 模組
from.models import User,Post,Tag
from .forms import PostForm
import markdown

# 首頁 : 顯示所有文章
def index(request):
    posts = Post.objects.all()
    tags = Tag.objects.all()
    paginator = Paginator(posts, 3)  # 每頁顯示 5 篇文章
    page_number = request.GET.get('page') # 取得頁數
    page_obj = paginator.get_page(page_number) # 取得頁面物件
    page_count = paginator.count # 總共有多少文章
    
    # 預計之後要首頁顯示總文章數量
    tags_with_counts = Tag.objects.annotate(num_posts=Count('post')) # 計算每個 tag 有幾篇文章
    return render(request, 'index.html', 
                  {'posts': posts,
                   'tags':tags,
                   'paginator':paginator,
                   'page_obj':page_obj,'page_count':page_count,
                   'tags_with_counts': tags_with_counts})
    
# 標籤頁面 : 顯示該標籤的所有文章列表
def tag_detail(request,tag_id):
    tag = get_object_or_404(Tag, id=tag_id) # 取得 單一標籤名稱 
    posts = Post.objects.filter(tags=tag) # post 表中標籤名稱 與 tag_id 相同的文章
    tags_with_counts = Tag.objects.annotate(num_posts=Count('post')) # 取得 標籤 : 文章數量
    tags = Tag.objects.all()
    return render(request, 'tag_detail.html', 
                  { "tag" : tag ,
                   'posts': posts,
                #    'tags':tags,
                   'tags_with_counts': tags_with_counts})

# blog 同 index 頁面
# def blog(request):
#     return render(request, 'blog.html')
  
# 作品集
def portfolio(request):
    return render(request, 'portfolio.html')

# 關於我
# def about(request):
#     return render(request, 'about.html')

def about_me(request):
    with open('static/about_me.md', 'r',encoding='utf-8') as f:
        content = f.read()
        html_content = markdown.markdown(content)
    return render(request, 'about_me.html', {'html_content': html_content})

# blog_post_detail 頁面 (顯示單篇文章) , 文章內容會用Markdowne格式轉換
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





