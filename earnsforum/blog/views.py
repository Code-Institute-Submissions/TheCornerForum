from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post, Cartoon, CartoonPanel
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
        stored_contents = request.session.get("stored_contents", {})

        posts = Post.objects.filter(id__in=stored_contents.get("posts", []))
        cartoons = Cartoon.objects.filter(id__in=stored_contents.get("cartoons", []))

        context = {
            "posts": posts,
            "cartoons": cartoons,
            "has_contents": bool(posts or cartoons)
        }
        return render(request, "blog/stored-posts.html", context)

    def post(self, request):
        stored_contents = request.session.get("stored_contents", {"posts": [], "cartoons": []})

        content_type = request.POST.get("content_type")
        content_id = int(request.POST["content_id"])

        if content_type == "post":
            if content_id not in stored_contents["posts"]:
                stored_contents["posts"].append(content_id)
            else:
                stored_contents["posts"].remove(content_id)
        elif content_type == "cartoon":
            if content_id not in stored_contents["cartoons"]:
                stored_contents["cartoons"].append(content_id)
            else:
                stored_contents["cartoons"].remove(content_id)
        
        referer_url = request.META.get('HTTP_REFERER', '/')
        return HttpResponseRedirect(referer_url)

class CartoonView(ListView):
    template_name = "blog/cartoon.html"
    model = Cartoon
    context_object_name = "cartoons"

def cartoon_detail(request, slug): 
    cartoon = get_object_or_404(Cartoon, slug=slug)
    cartoon_panels = cartoon.panels.all().order_by('order')
    return render(request, "blog/cartoon-detail.html", {
        "cartoon": cartoon,
        "cartoon_panels": cartoon_panels,
    })
