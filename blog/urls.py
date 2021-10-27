from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    HomePageView,
    PostCreateView,
    PostUpdateView
)


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('post/', PostListView.as_view(), name='all_posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name="post_new"),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name="post_edit"),
]
