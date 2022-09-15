from PIL import Image, ImageDraw, ImageChops
import random
import colorsys
# # Potentially manage colors with Coolors.co?
# from coolors import coolor

def random_color():
    # Creates random hue for HSV color (keeps saturation of colors)
    h = random.random()
    s = 1
    v = 1
    
    # Convert HSV to RGB
    rgb_float = colorsys.hsv_to_rgb(h,s,v)
    rgb = [int(i *255) for i in rgb_float]
    
    return tuple(rgb)

def color_interpolation(start, end, factor:float):
    reciprocal = 1 - factor
    return (
        int(start[0] * reciprocal + end[0] * factor),
        int(start[1] * reciprocal + end[1] * factor),
        int(start[2] * reciprocal + end[2] * factor)
    )

def generate_art(path: str):    
    # Generate base image
    target_size_px = 512
    scale = 4
    padding_pct = 0.2
    line_count = 10
    image_size_px = target_size_px * scale
    image_bg_color = (0, 0, 0)
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
    for _ in range(line_count):
        random_point = (
            random.randint(int(padding_pct * image_size_px), image_size_px - int(image_size_px * padding_pct)),
            random.randint(int(padding_pct * image_size_px), image_size_px - int(image_size_px * padding_pct))
        )
        endpoints.append(random_point)

#Centering of image 
    # Define and #(draw bounding box for all points)
    min_x = min([p[0] for p in endpoints])
    max_x = max([p[0] for p in endpoints])
    min_y = min([p[1] for p in endpoints])
    max_y = max([p[1] for p in endpoints])
    # draw.rectangle((min_x, min_y, max_x, max_y), outline = (255, 0, 0))
    
    # Center the image
    delta_x = (image_size_px - max_x) - min_x
    delta_y = (image_size_px - max_y) - min_y
    for i, point in enumerate(endpoints):
        endpoints[i] = (point[0] + delta_x // 2, point[1] + delta_y // 2)
        
    # # Define and draw bounding box for all new points to show movement
    # min_x = min([p[0] for p in endpoints])
    # max_x = max([p[0] for p in endpoints])
    # min_y = min([p[1] for p in endpoints])
    # max_y = max([p[1] for p in endpoints])
    # draw.rectangle((min_x, min_y, max_x, max_y), outline = (0, 255, 0))
    
    # Connects each point with its following point
    line_thickness = 1
    point_count = len(endpoints)- 1
    for i, point in enumerate(endpoints):
        
        # Create canvas overlay
        overlay_image = Image.new("RGB", (image_size_px, image_size_px), image_bg_color)
        overlay_draw = ImageDraw.Draw(overlay_image)
        
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
        line_thickness += scale
        overlay_draw.line(line_xy, fill = line_color, width = line_thickness)
        image = ImageChops.add(image, overlay_image)
    
    image = image.resize((target_size_px, target_size_px), resample = Image.ANTIALIAS)    
    image.save(path)
    print("Done!")

instance_count = 10

if __name__ == "__main__":
    for i in range(instance_count):
        print(f"Creating image {i + 1}...")
        generate_art(f"Images/test-image-{i}.png")