# ArtGen
##Uses Python to create random generative art a la Art Blocks 

I apologize for the frequencies of the commits - as this is meant to be a portfolio piece, I'm trying to demonstrate the process by which this was built

##DEPENDENCIES:
- Pillow

##USAGE:
#Variables
- **image_size_px** (line 29): adjusts the overall size of the canvas, in pixels
- **padding_pct** (line 30): adjusts the margin as a percentage of the total canvas size
- **line_count** (line 31): adjusts the total number of lines used in the piece
- **line_thickness** (line 75): adjusts integer weight of first line; will need to be adjusted as canvas size is changed
- **instance_count** (line 102): adjusts the number of images generated in the Images folder

### TO-DO
- Create better blending for color gradient
- Anti-aliasing for smaller canvas sizes
- Experiment with different shapes (arcs, polygons, ellipses)
- Include coolors.co compatibility to generate pleasing palettes for the shape