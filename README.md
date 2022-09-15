# ArtGen
## Uses Python to create random generative art a la Art Blocks 

I apologize for the frequencies of the commits - as this is meant to be a portfolio piece, I'm trying to demonstrate the process by which this was built

## DEPENDENCIES:
- Pillow

## USAGE:
# Variables
- **target_size_px** (line 29): adjusts the overall size of the final canvas, in pixels
- **scale** (line 30): changes the scale at which the image is rendered before downsampling for anti-aliasing of final image
- **padding_pct** (line 31): adjusts the margin as a percentage of the total canvas size
- **line_count** (line 32): adjusts the total number of lines used in the piece
- **line_thickness** (line 77): adjusts integer weight of first line; will need to be adjusted as canvas size is changed
- **instance_count** (line 105): adjusts the number of images generated in the Images folder

### TO-DO
- Create better blending for color gradient
- Experiment with different shapes (arcs, polygons, ellipses)
- Include coolors.co compatibility to generate pleasing palettes for the shape