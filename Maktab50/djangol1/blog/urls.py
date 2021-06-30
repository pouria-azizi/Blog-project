from django.urls import path
from django.views.decorators.cache import cache_page

from . import views

app_name = 'blog'

urlpatterns = [
    path('blog/<int:code>/', cache_page(60 * 15)(views.show_all_posts)),
    path('home/', views.show_all_posts, name='show-all-posts'),
    path('create/', views.create_post, name='create-post'),
    path('create-category/', views.CreateCategory.as_view(), name='create-category'),
    path('update-category/<int:pk>', views.UpdateCategory.as_view(), name='update-category'),
    path('like-post/<int:id>', views.like_post, name='like-post'),
    path('edit/<int:pk>', views.edit_post, name='edit'),
    path('post/<int:pk>', views.ViewPost.as_view(), name='detail'),
    path('category/<slug:category_slug>/', views.FilterPostByCategory.as_view(), name='post-by-category'),
]
