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
    
    # Create a list of each random points
    endpoints = []
    for _ in range(10):
        random_point = (
            random.randint(0, image_size_px),
            random.randint(0, image_size_px)
        )
        endpoints.append(random_point)
    # Create random lines using previous line's endpoint as subsequent start point
    for i, point in enumerate(endpoints):
        start = point
        if i == len(endpoints) - 1:
            end = endpoints[0]
        else:
            end = endpoints[i + 1]
        line_xy = (start, end)
        line_color = (0, 0, 0)
        draw.line(line_xy, fill = line_color)
    
    image.save("test-image.png")

if __name__ == "__main__":
    generate_art()