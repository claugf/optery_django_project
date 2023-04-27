from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages

from django.contrib.auth.models import User
from django.db.models import Count
from .models import Post, Like, Comment


@login_required
def post_list(request):
    posts = Post.objects.annotate(num_likes=Count('likes'))
    return render(request, 'social/post_list.html', {'posts': posts})


@require_POST
@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    user = request.user

    if Like.objects.filter(post=post, user=user).exists():
        Like.objects.filter(post=post, user=user).delete()
    else:
        Like.objects.create(post=post, user=user)

    num_likes = post.likes.count()
    return HttpResponse(num_likes)


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
        Comment.objects.create(
            post=post, user=request.user, content=comment_text)
    else:
        messages.warning(request, "Please enter a comment!")

    comments = post.comment_set.all().order_by('-date_posted')
    return render(request, 'partials/_comment_list.html', {'comments': comments})


@login_required
def search_view(request):
    query = request.GET.get('q')

    if query:
        users = User.objects.filter(username__icontains=query)
        posts = Post.objects.filter(title__icontains=query)
    else:
        users = None
        posts = None

    context = {
        'users': users,
        'posts': posts,
        'query': query,
    }

    return render(request, 'social/search.html', context)
