from django import forms
from .models import Customization, Pattern, Preset

class CustomizationForm(forms.ModelForm):
    class Meta:
        model = Customization
        fields = ['preset', 'pattern', 'custom_text', 'custom_image', 'rotation', 'density']
        widgets = {
            'preset': forms.Select(attrs={'class': 'block appearance-none w-full bg-white border border-gray-400 hover:border-gray-500 px-4 py-2 pr-8 rounded shadow leading-tight'}),
            'pattern': forms.Select(attrs={'class': 'block appearance-none w-full bg-white border border-gray-400 hover:border-gray-500 px-4 py-2 pr-8 rounded shadow leading-tight'}),
            # Add other widgets as necessary
        }

class PatternForm(forms.ModelForm):
    class Meta:
        model = Pattern
        fields = ['name', 'image']

class PresetForm(forms.ModelForm):
    class Meta:
        model = Preset
        fields = ['name', 'pattern', 'default_text']
