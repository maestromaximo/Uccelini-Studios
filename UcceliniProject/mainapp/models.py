from django.db import models
from django.contrib.auth.models import User 
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

class Pattern(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='patterns/')

class Preset(models.Model):
    name = models.CharField(max_length=100)
    pattern = models.ForeignKey(Pattern, on_delete=models.CASCADE)
    default_text = models.CharField(max_length=255, blank=True)

class Customization(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # If you have user accounts
    preset = models.ForeignKey(Preset, on_delete=models.SET_NULL, null=True, blank=True)
    pattern = models.ForeignKey(Pattern, on_delete=models.SET_NULL, null=True, blank=True)
    custom_text = models.CharField(max_length=255, blank=True)
    custom_image = models.ImageField(upload_to='custom_images/', blank=True, null=True)
    rotation = models.IntegerField(default=0)
    density = models.IntegerField(default=50)

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    preferred_name = models.CharField(max_length=100, blank=True)
    address = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    # Additional fields as needed

    def __str__(self):
        return self.user.username

# Signal to create or update the user profile automatically whenever the user object is created or saved.
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()