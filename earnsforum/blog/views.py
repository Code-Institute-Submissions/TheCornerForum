from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render, get_object_or_404
from .models import Post, Cartoon, CartoonPanel, SavedContent
from .form import CommentForm
from users1.models import UserProfile


class StartingPageView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ['-date']
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        # Display only the top 3 posts on the starting page
        data = queryset[:3]
        return data


class AllPostsView(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    ordering = ['-date']
    context_object_name = "all_posts"  # Contains all posts for the 'all-posts' page


class SinglePostView(View):
    def is_stored_posts(self, request, post_id):
        stored_posts = request.session.get("stored_posts")
        return post_id in stored_posts if stored_posts else False

    def get(self, request, slug):
        try:
            post = get_object_or_404(Post, slug=slug)
            context = {
                "post": post,
                "post_tags": post.tags.all(),
                "comment_form": CommentForm(),
                "comments": post.comments.all().order_by('-id'),
                "saved_for_later": self.is_stored_posts(request, post.id)
            }
            return render(request, "blog/post-detail.html", context)
        except Http404:
            return render(request, "user1/404.html", {"message": "Post not found."})
        except Exception as e:
            # Log the error here if you have logging setup
            return render(request, "user1/error.html", {"message": "An unexpected error occurred."})

    @method_decorator(login_required)
    def post(self, request, slug):
        # Handle comment submission for a single post
        post = get_object_or_404(Post, slug=slug)
        comment_form = CommentForm(request.POST)
        

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("blog:post-detail-page", args=[slug]))

        # Re-render the page with existing context and the invalid form
        context = {
            post": post,
        "post_tags": post.tags.all(),
        "comment_form": comment_form,
        "comments": post.comments.all().order_by('-id'),
        "saved_for_later": self.is_stored_posts(request, post.id)
        }
        return render(request, "blog/post-detail.html", context)
    
@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id, user=request.user)
    if request.method == "POST":
        comment.text = request.POST.get("text")
        comment.save()
        return redirect("blog:post-detail-page", slug=comment.post.slug)
    return render(request, "blog/edit_comment.html", {"comment": comment})

@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id, user=request.user)
    if request.method == "POST":
        comment.text = request.POST.get("text")
        comment.save()
        return redirect("post_detail", pk=comment.post.id)
    return render(request, "blog/edit_comment.html", {"comment": comment})

@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id, user=request.user)
    post_id = comment.post.id
    comment.delete()
    return redirect("post_detail", pk=post_id)

@login_required
def save_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    saved_content = SavedContent.objects.get_or_create(user_profile=request.user.userprofile)[0]
    if post in saved_content.posts.all():
        saved_content.posts.remove(post)
    else:
        saved_content.posts.add(post)
    return redirect("post_detail", pk=post_id)

class ReadLaterView(LoginRequiredMixin, View):

    def get(self, request):
        # Ensure a UserProfile exists for the user and get its associated SavedContent
        user_profile, created = UserProfile.objects.get_or_create(user=request.user)
        saved_content, created = SavedContent.objects.get_or_create(user_profile=user_profile)

        # Get the saved posts and cartoons
        posts = saved_content.posts.all()
        cartoons = saved_content.cartoons.all()

        context = {
            "posts": posts,
            "cartoons": cartoons,
            "has_contents": bool(posts or cartoons)
        }
        return render(request, "blog/stored-posts.html", context)

    def post(self, request):
        # Get user's UserProfile and associated SavedContent
        user_profile = UserProfile.objects.get(user=request.user)
        saved_content = user_profile.saved_content

        content_type = request.POST.get("content_type")
        content_id = request.POST.get("content_id")

        if content_type == "post":
            post = get_object_or_404(Post, pk=content_id)
            if post in saved_content.posts.all():
                saved_content.posts.remove(post)
            else:
                saved_content.posts.add(post)
        elif content_type == "cartoon":
            cartoon = get_object_or_404(Cartoon, pk=content_id)
            if cartoon in saved_content.cartoons.all():
                saved_content.cartoons.remove(cartoon)
            else:
                saved_content.cartoons.add(cartoon)

        return redirect(request.POST.get('next', '/'))

class CartoonDetailView(View):
    def get(self, request, slug):
        cartoon = get_object_or_404(Cartoon, slug=slug)
        cartoon_panels = cartoon.panels.all().order_by('order')

        context = {
            "cartoon": cartoon,
            "cartoon_panels": cartoon_panels,
        }
        return render(request, "blog/cartoon-detail.html", context)
# class CartoonView(ListView):
#     template_name = "blog/cartoon.html"
#     model = Cartoon
#     context_object_name = "cartoons"


# def cartoon_detail(request, slug):
#     cartoon = get_object_or_404(Cartoon, slug=slug)
#     cartoon_panels = cartoon.panels.all().order_by('order')
#     return render(request, "blog/cartoon-detail.html", {
#         "cartoon": cartoon,
#         "cartoon_panels": cartoon_panels,
#     })
