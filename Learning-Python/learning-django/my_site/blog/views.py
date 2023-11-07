from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DeleteView

from .models import Post
from .forms import CommentForm


# Create your views here.

class StartingPageView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"
    
    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data


# the class on the top instead of functional view for the one i just commented 

# def starting_paeg(request):
#     latest_posts = Post.objects.all().order_by("-date")[:3]
#     return render(request, "blog/index.html", {
#         "posts": latest_posts
#     })

class AllPostsView(ListView):
    template_name="blog/all-posts.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "all_posts"

# the class on the top instead of the functional view down here 

# def posts(request):
#     all_posts = Post.objects.all().order_by("-date")[:3]
#     return render(request, "blog/all-posts.html", {
#         "all_posts": all_posts
#     })

class SinglePostView(DeleteView):
    template_name = "blog/post-detail.html"
    model = Post

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["post_tags"] = self.object.tags.all()
        context["comment_form"] = CommentForm()
        return context

# the class on the top instead of the functional view down here 

# def post_detail(request, slug):
#     identified_post = get_object_or_404(Post, slug=slug)
#     return render(request, "blog/post-detail.html", {
#         "post": identified_post, 
#         "post_tags": identified_post.tags.all()
#     })
