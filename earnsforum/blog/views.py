from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post
from .form import CommentForm

class StartingPageView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ['-date']
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]  # Display only the top 3 posts on the starting page
        return data

class AllPostsView(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    ordering = ['-date']
    context_object_name = "all_posts"  # Contains all posts for the 'all-posts' page

class SinglePostView(View):
    def is_stored_posts(self, request, post_id):
        # Logic to check if a post is in the user's 'read later' list
        stored_posts = request.session.get("stored_posts")
        return post_id in stored_posts if stored_posts else False
    
    def get(self, request, slug):
        # Display a single post details
        post = get_object_or_404(Post, slug=slug)
        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": CommentForm(),
            "comments": post.comments.all().order_by('-id'),
            "saved_for_later": self.is_stored_posts(request, post.id)
        }
        return render(request, "blog/post-detail.html", context)

    @method_decorator(login_required)
    def post(self, request, slug):
        # Handle comment submission for a single post
        comment_form = CommentForm(request.POST)
        post = get_object_or_404(Post, slug=slug)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("blog:post-detail-page", args=[slug]))

        # Re-render the page with existing context and the invalid form
        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": comment_form,
            "comments": post.comments.all().order_by('-id'),
        }
        return render(request, "blog/post-detail.html", context)

class ReadLaterView(LoginRequiredMixin, View):
    def get(self, request):
        stored_posts = request.session.get("stored_posts")
        print("Stored posts:", stored_posts)

        context = {}

        if stored_posts is None or len(stored_posts) == 0:
            context["posts"] = []
            context["has_posts"] = False
        else:
            posts = Post.objects.filter(id__in=stored_posts)
            context["posts"] = posts
            context["has_posts"] = True

        print("Debug test", context)
        return render(request, "blog/stored-posts.html", context)
    

    def post(self, request):
        stored_posts = request.session.get("stored_posts")

        if stored_posts is None:
            stored_posts = []

        post_id = int(request.POST["post_id"])

        if post_id not in stored_posts:
            stored_posts.append(post_id)
        else:
            stored_posts.remove(post_id)
            
        request.session["stored_posts"] = stored_posts    

        return HttpResponseRedirect("/")