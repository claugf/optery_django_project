from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from .models import Post, Like


@login_required
def post_list(request):
    posts = Post.objects.annotate(num_likes=Count('like'))
    return render(request, 'social/post_list.html', {'posts': posts})


@require_POST
@login_required
def like_post(request, post_id):
    if request.method == 'POST':
        post = get_object_or_404(Post, pk=post_id)
        user = request.user

        if Like.objects.filter(post=post, user=user).exists():
            Like.objects.filter(post=post, user=user).delete()
            like_added = False
        else:
            Like.objects.create(post=post, user=user)
            like_added = True

        likes_count = Like.objects.filter(post=post).count()
        return JsonResponse({'likes_count': likes_count, 'like_added': like_added})
