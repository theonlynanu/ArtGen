from PIL import Image, ImageDraw
import random

def generate_art():
    print("Working...")
    
    # Generate base image
    image_size_px = 128
    image_bg_color = (255, 255, 255)
    image = Image.new(
        "RGB", 
        (image_size_px, image_size_px), 
        image_bg_color
    )
    
    # Draw lines over base image
    draw = ImageDraw.Draw(image)
    
    for _ in range(10):
        random_point_one = (
            random.randint(0, image_size_px), 
            random.randint(0, image_size_px)
        )
        random_point_two = (
            random.randint(0, image_size_px), 
            random.randint(0, image_size_px)
        )
        
        line_xy = (random_point_one, random_point_two)
        line_color = (0, 0, 0)
        draw.line(line_xy, fill = line_color)
    
    image.save("test-image.png")

if __name__ == "__main__":
    generate_art()