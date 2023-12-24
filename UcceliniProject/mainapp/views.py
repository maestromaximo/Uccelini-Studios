
from django.shortcuts import render
from .models import Pattern, Preset

def home(request):
    return render(request, 'home.html')

from .forms import CustomizationForm, PatternForm, PresetForm
 # if request.method == 'POST':
    #     form = CustomizationForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         customization = form.save(commit=False)
    #         customization.user = request.user
    #         customization.save()
    #         # Redirect or update context as necessary
    # else:
    #     form = CustomizationForm()

    # context = {
    #     'form': form,
    #     # Add other context variables like presets and patterns
    # }
    # return render(request, 'customize.html', context)
def customize(request):
    patterns = Pattern.objects.all()
    presets = Preset.objects.all()
    # Add other queries as needed

    context = {
        'patterns': patterns,
        'presets': presets,
        # Add other context variables as needed
    }
    return render(request, 'customize.html', context)