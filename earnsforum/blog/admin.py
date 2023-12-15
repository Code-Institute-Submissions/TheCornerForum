from django.contrib import admin
from .models import Cartoon, CartoonPanel
from .models import Author, Post, Tag, Comment


class PostAdmin(admin.ModelAdmin):
    list_filter = ("author", "tags", "date",)
    list_display = ("title", "date", "author",)
    prepopulated_fields = {"slug": ("title",)}


class CommentAdmin(admin.ModelAdmin):
    list_display = ("user", "post", "text", "date")
    list_filter = ("user", "post", "date")

class CartoonPanelInline(admin.TabularInline):
    model = CartoonPanel
    extra = 1

@admin.register(Cartoon)
class CartoonAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    inlines = [CartoonPanelInline]
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Author)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)
