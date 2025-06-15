from django.shortcuts import render, get_object_or_404
from .models import Blog
# Create your views here.
def blogs(request):
    blogs = Blog.objects.all()
    param = {
        'blogs': blogs,
    }
    return render(request, 'blogs.html', param)


def blog_detail(request, id):
    blog = get_object_or_404(Blog, id=id)
    return render(request, 'blog_detail.html', {'blog': blog})