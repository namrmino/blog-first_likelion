from django.shortcuts import render, get_object_or_404
from .models import Blog

def home(request):
    blogs = Blog.objects
    # blogs : Blog 클래스 안에 있는 쿼리셋을 담아놓은 것
    # 쿼리셋 : 모델로부터 전달받은 객체 목록
    # .objects : 쿼리셋을 받을 수 있다.
    # 메소드 : 쿼리셋을 기능하거나 정렬해주는 방법
    return render(request, 'home.html', {'blogs':blogs})


# 쿼리셋과 메소드의 형식 : 모델.쿼리셋(objects).메소드

def detail(request, blog_id):
    # blog_detail = 이용자가 원하는 몇 번 블로그 객체
    blog_detail = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'detail.html', {'blog':blog_detail})
