from django.contrib import admin
from .models import Post, Like, Comment


class LikeInline(admin.TabularInline):
    model = Like


class CommentInline(admin.StackedInline):
    model = Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [LikeInline, CommentInline]
    list_display = ('title', 'author', 'date_posted')
    list_filter = ('author', 'date_posted')
    search_fields = ('title', 'content')
    ordering = ('-date_posted',)


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('post', 'user')
    list_filter = ('user', 'post')
    ordering = ('post', 'user')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'date_posted')
    list_filter = ('post', 'user', 'date_posted')
    search_fields = ('content',)
    ordering = ('-date_posted',)
