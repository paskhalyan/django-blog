from django.shortcuts import render, get_object_or_404

from . import models


def home(request):
    posts = models.Post.objects.order_by('pub_date')
    return render(request, 'posts/home.html', {'posts': posts})


def post_details(request, post_id):
    post = get_object_or_404(models.Post, pk=post_id)
    return render(request, 'posts/post_detail.html', {'post': post})
