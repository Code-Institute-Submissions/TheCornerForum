from django.db.models.signals import post_save
from django.dispatch import receiver
from django.apps import apps

@receiver(post_save, sender='users1.UserProfile')
def create_or_get_saved_content(sender, instance, created, **kwargs):
    if created:
        SavedContent = apps.get_model('blog', 'SavedContent')
        SavedContent.objects.get_or_create(user_profile=instance)