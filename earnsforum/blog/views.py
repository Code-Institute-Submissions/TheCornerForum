from django.http import JsonResponse
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
from .models import Comment
from django.http import HttpResponseForbidden


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
    context_object_name = "all_posts"

    def get_queryset(self):
        queryset = super(AllPostsView, self).get_queryset()
        print(f"Queryset: {queryset}")
        return queryset


class SinglePostView(View):
    def post(self, request, slug):
        # This method will handle POST requests to your SinglePostView
        # Typically, this would be for submitting comments
        post = get_object_or_404(Post, slug=slug)
        comment_form = CommentForm(request.POST or None)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect('blog:post-detail-page', slug=slug)
        else:
            # If form is not valid, render the page with the invalid form
            comments = post.comments.all()
            return render(request, "blog/post-detail.html", {
                "post": post,
                "comments": comments,
                "comment_form": comment_form
            })

    def is_stored_posts(self, request, post_id):
        # Logic to check if a post is in the user's 'read later' list
        stored_posts = request.session.get("stored_posts")
        return post_id in stored_posts if stored_posts else False

    def get(self, request, slug):
        # Display a single post details
        post = get_object_or_404(Post, slug=slug)
        comments = post.comments.all()
        comment_form = CommentForm()
        return render(request, "blog/post-detail.html", {
            "post": post,
            "comments": comments,
            "comment_form": comment_form
        })

@method_decorator(login_required)
def post(self, request, slug):
    # Handle comment submission for a single post
    post = get_object_or_404(Post, slug=slug)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.post = post
        comment.user = request.user
        comment.save()
        return redirect('blog:post-detail-page', slug=slug)
    else:
        comments = post.comments.all()
        return render(request, "blog/post-detail.html", {
            "post": post,
            "comments": comments,
            "comment_form": comment_form
        })

@method_decorator(login_required)
def is_stored_posts(self, request, post_id):
    stored_posts = request.session.get("stored_posts")
    return post_id in stored_posts if stored_posts else False

@method_decorator(login_required, name='dispatch')
def add_comment_to_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.user = request.user
            new_comment.post = post
            new_comment.save()
            return redirect("blog:post-detail-page", slug=post.slug)
    else:
        comment_form = CommentForm()

    return redirect('blog:post-detail-page', slug=post.slug)    

@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id, user=request.user)
    if request.method == "POST":
        comment.text = request.POST.get("text")
        comment.save()
        return redirect("blog:post-detail-page", slug=comment.post.slug)
    else:
        comment_form = CommentForm(instance=comment)

    return render(request, "blog/edit_comment.html", {"comment_form": comment_form, "comment": comment})


@method_decorator(login_required)
def save_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    saved_content = SavedContent.objects.get_or_create(
        user_profile=request.user.userprofile)[0]
    if post in saved_content.posts.all():
        saved_content.posts.remove(post)
    else:
        saved_content.posts.add(post)
    return redirect("post_detail", pk=post_id)



@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if comment.user != request.user:
        return HttpResponseForbidden("You are not allowed to delete this comment.")

    post_id = comment.post.id
    comment.delete()
    return redirect("blog:post-detail-page", slug=comment.post.slug)


class ReadLaterView(LoginRequiredMixin, View):

    def get(self, request):
        # Ensure a UserProfile exists for the user and get its associated SavedContent
        user_profile, created = UserProfile.objects.get_or_create(
            user=request.user)
        saved_content, created = SavedContent.objects.get_or_create(
            user_profile=user_profile)

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
        user_profile, _ = UserProfile.objects.get_or_create(user=request.user)
        saved_content, _ = SavedContent.objects.get_or_create(user_profile=user_profile)

        content_type = request.POST.get("content_type")
        content_id = request.POST.get("content_id")
        is_saved = False  # Default state is not saved

        # Check if it's a post or cartoon and add/remove from saved content
        if content_type == "post":
            post = get_object_or_404(Post, pk=content_id)
            if post in saved_content.posts.all():
                saved_content.posts.remove(post)
            else:
                saved_content.posts.add(post)
                is_saved = True  # Set to true if saved
        elif content_type == "cartoon":
            cartoon = get_object_or_404(Cartoon, pk=content_id)
            if cartoon in saved_content.cartoons.all():
                saved_content.cartoons.remove(cartoon)
            else:
                saved_content.cartoons.add(cartoon)
                is_saved = True  # Set to true if saved

        # If the request is AJAX, return JsonResponse
        if request.is_ajax():
            return JsonResponse({'saved': is_saved})
        
        # If not AJAX, redirect as normal
        return redirect(request.POST.get('next', '/'))

    # def post(self, request):
    #     # Get user's UserProfile and associated SavedContent
    #     user_profile = UserProfile.objects.get(user=request.user)
    #     saved_content = user_profile.saved_content

    #     content_type = request.POST.get("content_type")
    #     content_id = request.POST.get("content_id")

    #     if content_type == "post":
    #         post = get_object_or_404(Post, pk=content_id)
    #         if post in saved_content.posts.all():
    #             saved_content.posts.remove(post)
    #         else:
    #             saved_content.posts.add(post)
    #     elif content_type == "cartoon":
    #         cartoon = get_object_or_404(Cartoon, pk=content_id)
    #         if cartoon in saved_content.cartoons.all():
    #             saved_content.cartoons.remove(cartoon)
    #         else:
    #             saved_content.cartoons.add(cartoon)

    #     return redirect(request.POST.get('next', '/'))


class CartoonDetailView(View):
    def get(self, request, slug):
        cartoon = get_object_or_404(Cartoon, slug=slug)
        cartoon_panels = cartoon.panels.all().order_by('order')

        context = {
            "cartoon": cartoon,
            "cartoon_panels": cartoon_panels,
        }
        return render(request, "blog/cartoon-detail.html", context)


class CartoonView(ListView):
    template_name = "blog/cartoon.html"
    model = Cartoon
    context_object_name = "cartoons"