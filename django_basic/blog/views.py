from django.shortcuts import render, get_object_or_404
from .models import Post
from .form import HeadlineSearch

# Create your views here.
def index_view(request):
    form = HeadlineSearch()
    post_list = Post.objects.order_by('-pub_date')

    if request.method == 'POST':
        form = HeadlineSearch(request.POST)

        if form.is_valid():
            headline = form.cleaned_data['post_headline']
            post_list = Post.objects.filter(headline__contains=headline)
            context = {'post_list': post_list, 'form': form}
            return render(request, 'blog/index.html', context)
    else:
        context = {'post_list': post_list, 'form': form}
        return render(request, 'blog/index.html', context)
    return render(request, 'blog/index.html', context)

def post_detail_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/post.html', {'post': post})