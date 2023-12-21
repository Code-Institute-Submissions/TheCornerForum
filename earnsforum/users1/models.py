from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from cloudinary.models import CloudinaryField

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='users1_profile')
    is_admin = models.BooleanField(default=False)
    is_moderator = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)
    profile_picture = CloudinaryField('image', blank=True, null=True)  # Cloudinary image field
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def mark_as_deleted(self):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

class DeletedAccountLog(models.Model):
    user_id = models.IntegerField()
    deletion_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Deleted account {self.user_id} on {self.deletion_date}"