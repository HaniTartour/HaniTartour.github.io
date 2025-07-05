# 🔁 Batch Image OCR
# Extracts text from all image files in a folder and saves each result to a .txt file.

import os
from PIL import Image
import pytesseract

# Optional: Set path to Tesseract executable
#pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# 📁 Folder containing images
input_folder = 'images'  # Update this folder name
output_folder = 'output_texts'

# ✅ Supported image formats
image_extensions = ['.png', '.jpg', '.jpeg', '.tiff', '.bmp']

# 🔧 Make output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 🔍 Loop through image files in the folder
for filename in os.listdir(input_folder):
    name, ext = os.path.splitext(filename)
    if ext.lower() in image_extensions:
        image_path = os.path.join(input_folder, filename)
        output_txt_path = os.path.join(output_folder, f"{name}.txt")

        try:
            img = Image.open(image_path)
            text = pytesseract.image_to_string(img)

            with open(output_txt_path, 'w', encoding='utf-8') as f:
                f.write(text)

            print(f"✅ Saved: {output_txt_path}")
        except Exception as e:
            print(f"❌ Error with {filename}: {e}")
