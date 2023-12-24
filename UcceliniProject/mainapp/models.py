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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    preset = models.ForeignKey(Preset, on_delete=models.SET_NULL, null=True, blank=True)
    pattern = models.ForeignKey(Pattern, on_delete=models.SET_NULL, null=True, blank=True)
    custom_text = models.CharField(max_length=255, blank=True)
    custom_image = models.ImageField(upload_to='custom_images/', blank=True, null=True)
    faces_in_image = models.BooleanField(default=False)
    paper_size = models.CharField(max_length=10, choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Extra Large')])
    number_of_rolls = models.IntegerField(default=1)
    rotation = models.IntegerField(default=0)
    density = models.IntegerField(default=50)

    def __str__(self):
        return f'Customization for {self.user.username}'

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

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customization = models.ForeignKey(Customization, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=100)  # e.g., 'Pending', 'Shipped', 'Delivered'
    created_at = models.DateTimeField(auto_now_add=True)
    # Additional fields like payment information, shipping address, etc.

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customization = models.ForeignKey(Customization, on_delete=models.CASCADE)
    rating = models.IntegerField()  # Or a choice field
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class ShoppingCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Customization)
    # Additional fields like total cost
