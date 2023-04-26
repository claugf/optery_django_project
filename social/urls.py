from django.urls import path
from .views import post_list, like_post, post_detail, add_comment


app_name = 'social'

urlpatterns = [
    path('posts/', post_list, name='posts'),
    path('posts/<int:post_id>/', post_detail, name='post_detail'),
    path('posts/<int:post_id>/like/', like_post, name='like_post'),
    path('posts/<int:post_id>/add_comment/', add_comment, name='add_comment'),
]
