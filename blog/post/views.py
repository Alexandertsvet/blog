from django.shortcuts import render, get_list_or_404
from django.http import Http404

from post.models import Post

def post_list(request):
    posts = Post.published.all()
    return render(request,
                  'post/list.html',
                  {'posts':posts}
    )

def post_detail(request, id):
    post = get_list_or_404(Post, id=id, status=Post.Status.PUBLISHED)
    """post = Post.published.get(id=id)"""
    return render(request,
                  'post/detail.html',
                  {'post': post}
    )