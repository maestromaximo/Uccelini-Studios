from rembg import remove
import numpy as np
from PIL import Image
import io

from PIL import Image
import os
from rembg import remove
import io

def remove_background_with_rembg(input_path, output_path):
    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(input_path, 'rb') as file:
        input_bytes = file.read()

    output_bytes = remove(input_bytes)

    # Save the output
    output_image = Image.open(io.BytesIO(output_bytes))
    output_image.save(output_path)
