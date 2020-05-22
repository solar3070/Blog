from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog

def home(request):
    blogs = Blog.objects
    return render(request, 'home.html', {'blogs':blogs})

def detail(request, blog_id):
    details = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'detail.html', {'details':details})

def new(request): 
    return render(request, 'new.html')

def create(request): # 입력받은 내용을 DB에 넣어주는 함수
    blog = Blog() # Blog클래스로부터 blog객체 생성
    blog.image = request.FILES['image']
    blog.title = request.POST['title']
    blog.musician = request.POST['musician'] 
    blog.body = request.POST['body']
    blog.pub_date = timezone.datetime.now()
    blog.save() 
    return redirect('/blog/'+str(blog.id)) 