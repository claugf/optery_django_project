from django.urls import path
from .views import post_list, like_post, hello


app_name = 'social'

urlpatterns = [
    path('', hello),
    path('posts/', post_list),
    path('posts/int:post_id/like/', like_post, name='like_post')
]
