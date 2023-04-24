from django.shortcuts import render
from django.http import JsonResponse
from .models import Post, Like


def hello(request):
    return render(request, 'index.html')


def post_list(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'post_list.html', context)


def like_post(request, post_id):
    if request.method == 'POST':
        post = Post.objects.get(pk=post_id)
        like, created = Like.objects.get_or_create(
            user=request.user, post=post)
        if not created:
            like.delete()
        likes_count = post.like_set.count()
        data = {'likes_count': likes_count}
        return JsonResponse(data)
    else:
        return JsonResponse({'error': 'Invalid post'})
