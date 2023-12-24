
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
from django.shortcuts import render, redirect
from .models import Pattern, Preset, Customization
from django.contrib.auth.models import User
from .utils import remove_background_with_rembg
import os

def customize(request):
    patterns = Pattern.objects.all()
    presets = Preset.objects.select_related('pattern').all()

    if request.method == 'POST':
        # Process the form data
        user = request.user  # Assuming the user is logged in
        preset_id = request.POST.get('preset')
        pattern_id = request.POST.get('basePattern')
        custom_text = request.POST.get('customText')
        uploaded_image = request.FILES.get('customImage')
        special_instructions = request.POST.get('specialInstructions')

        # Initialize variables for the image paths
        processed_image_path = None

        # Process and save the uploaded image
        if uploaded_image:
            temp_image_path = os.path.join('media', 'temp', uploaded_image.name)
            # In your view
            processed_image_path = os.path.join('custom_images', uploaded_image.name)


            # Ensure the directory exists
            os.makedirs(os.path.dirname(temp_image_path), exist_ok=True)

            with open(temp_image_path, 'wb+') as destination:
                for chunk in uploaded_image.chunks():
                    destination.write(chunk)

            # Call the function to remove background
            remove_background_with_rembg(temp_image_path, processed_image_path)

            # Remove the temporary file
            os.remove(temp_image_path)

        # Create and save the Customization instance
        customization = Customization(
            user=user,
            preset_id=preset_id if preset_id else None,
            pattern_id=pattern_id if pattern_id else None,
            custom_text=custom_text,
            custom_image=processed_image_path if processed_image_path else None,
            special_notes=special_instructions,
            # Add other fields if necessary, like rotation, density, etc.
        )
        customization.save()

        # Redirect to home or another appropriate page
        return redirect('home')

    context = {
        'patterns': patterns,
        'presets': presets,
    }
    return render(request, 'customize.html', context)

def gallery(request):
    context={}
    return render(request, 'gallery.html', context)

def contact_us(request):
    context={}
    return render(request, 'contact_us.html', context)
