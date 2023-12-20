from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.apps import apps
from users1.models import UserProfile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=UserProfile)
def create_or_get_saved_content(sender, instance, created, **kwargs):
    if created:
        SavedContent = apps.get_model('blog', 'SavedContent')
        SavedContent.objects.get_or_create(user_profile=instance)