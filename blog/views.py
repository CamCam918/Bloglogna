from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    TemplateView,
    UpdateView
)
from django.views.generic.edit import (
    CreateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Post

# Create your views here.


class HomePageView(TemplateView):
    template_name = "home.html"


class PostListView(ListView):
    model = Post
    template_name = "post_list.html"


class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"


class PostCreateView(CreateView):
    model = Post
    template_name = "post_new.html"
    fields = ["title", "body", "author"]


class PostUpdateView(UpdateView):
    model = Post
    template_name = "post_edit.html"
    fields = ["title", "body"]


class PostDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")
