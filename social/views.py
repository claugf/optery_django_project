from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from django.db.models import Count
from .models import Post, Like


@login_required(login_url='accounts:login')
def post_list(request):
    posts = Post.objects.annotate(like_count=Count('like')).all()
    context = {'posts': posts}
    return render(request, 'social/post_list.html', context)


@require_POST
@login_required(login_url='accounts:login')
def like_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    user = request.user

    if Like.objects.filter(post=post, user=user).exists():
        Like.objects.filter(post=post, user=user).delete()
        like_added = False
    else:
        Like.objects.create(post=post, user=user)
        like_added = True

    likes_count = Like.objects.filter(post=post).count()
    data = {'likes_count': likes_count, 'like_added': like_added}
    return JsonResponse(data)
