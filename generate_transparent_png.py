"""
Generate a PNG image with a green border and transparent input areas.
"""

from PIL import Image, ImageDraw


def generate_transparent_png(
    width=800,
    height=600,
    border_width=10,
    border_color=(0, 255, 0),  # Green color (R, G, B)
    input_areas=None,
):
    """
    Generate a PNG image with a green border and transparent input areas.
    
    Args:
        width (int): Width of the image in pixels. Default: 800
        height (int): Height of the image in pixels. Default: 600
        border_width (int): Width of the green border in pixels. Default: 10
        border_color (tuple): RGB color tuple for the border. Default: (0, 255, 0) - green
        input_areas (list): List of tuples defining rectangular input areas as 
                           [(x1, y1, x2, y2), ...]. Default: None
    
    Returns:
        Image: PIL Image object with transparent background, green border, and input areas
    """
    
    # Create a new image with RGBA mode (supports transparency)
    # Start with a transparent background
    image = Image.new("RGBA", (width, height), (255, 255, 255, 0))
    
    draw = ImageDraw.Draw(image)
    
    # Draw the green border
    # Top border
    draw.rectangle(
        [(0, 0), (width, border_width)],
        fill=border_color + (255,)
    )
    # Bottom border
    draw.rectangle(
        [(0, height - border_width), (width, height)],
        fill=border_color + (255,)
    )
    # Left border
    draw.rectangle(
        [(0, 0), (border_width, height)],
        fill=border_color + (255,)
    )
    # Right border
    draw.rectangle(
        [(width - border_width, 0), (width, height)],
        fill=border_color + (255,)
    )
    
    # Draw input areas (transparent rectangles)
    if input_areas:
        for area in input_areas:
            x1, y1, x2, y2 = area
            # Keep these areas transparent by not drawing anything
            # Or optionally draw a subtle outline
            draw.rectangle(
                [(x1, y1), (x2, y2)],
                fill=(255, 255, 255, 0)  # Transparent fill
            )
    
    return image


def save_image(image, filename="output.png"):
    """
    Save the generated image to a file.
    
    Args:
        image (Image): PIL Image object to save
        filename (str): Output filename. Default: "output.png"
    """
    image.save(filename, "PNG")
    print(f"Image saved to {filename}")


def main():
    """Main function to demonstrate image generation."""
    
    # Define some input areas (transparent regions)
    input_areas = [
        (50, 50, 300, 150),      # First input area
        (350, 50, 600, 150),     # Second input area
        (100, 200, 700, 400),    # Large central input area
    ]
    
    # Generate the image
    image = generate_transparent_png(
        width=800,
        height=600,
        border_width=10,
        border_color=(0, 255, 0),  # Green border
        input_areas=input_areas
    )
    
    # Save the image
    save_image(image, "generate_transparent_png.png")


if __name__ == "__main__":
    main()
