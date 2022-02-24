from django.shortcuts import render
from .models import Post

# Create your views here.
def index_view(request):
    post_list = Post.objects.order_by('-pub_date')
    return render(request, 'blog/index.html', {'post_list': post_list})

def post_detail_view(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'blog/post.html', {'post': post})