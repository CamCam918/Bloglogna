from django.urls import path
from .views import PostListView, PostDetailView, HomePageView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('posts/', PostListView.as_view(), name='all_posts'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
]
