from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from .models import Post, Like, Comment


@login_required
def post_list(request):
    posts = Post.objects.annotate(num_likes=Count('likes'))
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


@login_required
def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = post.comment_set.all().order_by('-date_posted')
    num_likes = post.likes.count()
    data = {'post': post, 'comments': comments, 'num_likes': num_likes}
    return render(request, 'social/post_detail.html', data)


@require_POST
@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comment_text = request.POST.get('comment')
    if comment_text:
        comment = Comment.objects.create(
            post=post, user=request.user, content=comment_text)
        data = {
            'success': True,
            'comment': {
                'id': comment.id,
                'user': comment.user.username,
                'content': comment.content,
                'date_posted': comment.date_posted.strftime('%b %d, %Y %I:%M %p')
            }
        }
        return JsonResponse(data)
    else:
        return JsonResponse({'success': False})
