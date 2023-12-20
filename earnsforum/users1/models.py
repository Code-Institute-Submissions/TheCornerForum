from django.db import models
from django.contrib.auth.models import User
from django.apps import apps
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        SavedContent = apps.get_model('blog', 'SavedContent')
        saved_content, _ = SavedContent.objects.get_or_create(user_profile=instance.userprofile)

