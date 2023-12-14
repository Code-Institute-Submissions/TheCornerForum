from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']  # Only include the fields that are submitted by the form
        widgets = {
            "text": forms.Textarea(attrs={"class": "form-control"}),
        }