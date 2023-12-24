from django.contrib import admin

from .models import Pattern, Preset, Customization

@admin.register(Pattern)
class PatternAdmin(admin.ModelAdmin):
    list_display = ['name', 'image']

@admin.register(Preset)
class PresetAdmin(admin.ModelAdmin):
    list_display = ['name', 'pattern', 'default_text']

@admin.register(Customization)
class CustomizationAdmin(admin.ModelAdmin):
    list_display = ['user', 'preset', 'pattern', 'custom_text', 'custom_image', 'rotation', 'density']