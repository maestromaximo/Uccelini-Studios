from django.contrib import admin
from .models import Pattern, Preset, Customization, Profile, Order, Review, ShoppingCart

@admin.register(Pattern)
class PatternAdmin(admin.ModelAdmin):
    list_display = ['name', 'image']
    search_fields = ['name']

@admin.register(Preset)
class PresetAdmin(admin.ModelAdmin):
    list_display = ['name', 'pattern', 'default_text']
    list_filter = ['pattern']
    search_fields = ['name', 'default_text']

@admin.register(Customization)
class CustomizationAdmin(admin.ModelAdmin):
    list_display = ['user', 'preset', 'pattern', 'custom_text', 'paper_size', 'number_of_rolls']
    list_filter = ['preset', 'pattern', 'paper_size']
    search_fields = ['custom_text']

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'preferred_name', 'phone_number']
    search_fields = ['user__username', 'preferred_name', 'phone_number']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'customization', 'status', 'created_at', 'total_cost', 'payment_status']
    list_filter = ['status', 'payment_status']
    search_fields = ['user__username', 'status']

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'customization', 'rating', 'created_at']
    list_filter = ['rating']
    search_fields = ['user__username', 'comment']

@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ['user', 'total_cost']
    search_fields = ['user__username']
    filter_horizontal = ['items']  # For many-to-many field

