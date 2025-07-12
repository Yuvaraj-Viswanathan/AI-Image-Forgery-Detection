import os
from PIL import Image, ImageChops, ImageEnhance


def convert_to_ela_image(path, output_path, quality=90):
    # Open and resave image to simulate compression
    original = Image.open(path).convert('RGB')
    original = original.resize((224, 224))

    temp_filename = path + '_temp.jpg'
    original.save(temp_filename, 'JPEG', quality=quality)

    resaved = Image.open(temp_filename)
    ela_image = ImageChops.difference(original, resaved)

    # Enhance the contrast
    enhancer = ImageEnhance.Contrast(ela_image)
    ela_image = enhancer.enhance(10.0)

    # Save ELA image
    ela_image.save(output_path)
    os.remove(temp_filename)
    return ela_image


# Create ELA images for all files in the images/ folder
input_folder = 'images'
output_folder = 'ela_images'
os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.lower().endswith('.jpg') or filename.lower().endswith('.jpeg'):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename.replace('.jpg', '_ELA.jpg'))
        convert_to_ela_image(input_path, output_path)

print("✅ ELA images created successfully!")
