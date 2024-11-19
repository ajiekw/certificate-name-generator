from PIL import Image, ImageDraw, ImageFont
import os

# Configuration
TEMPLATE_PATH = "sertifikat.png"  # Directory Template
FONT_PATH = "Study_Clash.otf"  # Direktory font
OUTPUT_DIR = "certificates"  # Direktori untuk output sertifikat
FONT_SIZE = 200  # Konfigurasi size font
# NAME_COORDINATES = (1300, 1050)  # Koordinat X, Y nama sertifikat
TEXT_COLOR = (66, 135, 245)  # Code warna

# Dimensi untuk ukuran A4, 300 DPI
A4_WIDTH = 3500  # Lebar, pixels
A4_HEIGHT = 2300  # Tinggi, pixels

os.makedirs(OUTPUT_DIR, exist_ok=True)

def generate_certificate(name):
    template = Image.open(TEMPLATE_PATH)
    draw = ImageDraw.Draw(template)

    try:
        font = ImageFont.truetype(FONT_PATH, FONT_SIZE)
    except IOError:
        print("Font file not found. Please ensure the font path is correct.")
        return

    text_bbox = draw.textbbox((0, 0), name, font=font) 
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]


    x_position = (A4_WIDTH - text_width) // 2  
    y_position = (A4_HEIGHT - text_height) // 2  

    draw.text((x_position, y_position), name, fill=TEXT_COLOR, font=font)

    output_path = os.path.join(OUTPUT_DIR, f"{name}_certificate.png")
    template.save(output_path)
    print(f"Certificate for {name} saved at {output_path}")

students = [
            "List nama, bisa pakai csv"
            ]

# running script
for student in students:
    generate_certificate(student)

