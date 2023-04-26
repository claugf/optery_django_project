from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.db.models import Count
from .models import Post, Like


def post_list(request):
    posts = Post.objects.annotate(num_likes=Count('like'))
    return render(request, 'social/post_list.html', {'posts': posts})


@csrf_exempt
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
        return JsonResponse({'likes_count': likes_count})
