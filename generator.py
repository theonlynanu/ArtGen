from PIL import Image, ImageDraw
import random
# # Potentially manage colors with Coolors.co?
# from coolors import coolor

def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def color_interpolation(start, end, factor:float):
    reciprocal = 1 - factor
    return (
        int(start[0] * reciprocal + end[0] * factor),
        int(start[1] * reciprocal + end[1] * factor),
        int(start[2] * reciprocal + end[2] * factor)
    )

def generate_art():
    print("Working...")
    
    # Generate base image
    image_size_px = 512
    image_bg_color = (255, 255, 255)
    padding_pct = 0.2
    start_color = random_color()
    end_color = random_color()
    image = Image.new(
        "RGB", 
        (image_size_px, image_size_px), 
        image_bg_color
    )
    
    # Draw lines 
    draw = ImageDraw.Draw(image)
    
    # Create a list of each random points
    endpoints = []
    for _ in range(10):
        random_point = (
            random.randint(int(padding_pct * image_size_px), image_size_px - int(image_size_px * padding_pct)),
            random.randint(int(padding_pct * image_size_px), image_size_px - int(image_size_px * padding_pct))
        )
        endpoints.append(random_point)
    # Connects each point with its following point
    line_thickness = 1
    point_count = len(endpoints)- 1
    for i, point in enumerate(endpoints):
        start = point
        
        # Checks if starting point is at the end of the list; if so, connects to first point
        if i == point_count:
            end = endpoints[0]
        else:
            end = endpoints[i + 1]
        
        # Draws line
        line_xy = (start, end)
        color_factor = i / point_count
        line_color = color_interpolation(start_color, end_color, color_factor)
        line_thickness += 1
        draw.line(line_xy, fill = line_color, width = line_thickness)
    
    image.save("test-image.png")

if __name__ == "__main__":
    generate_art()