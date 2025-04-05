"""
ASCII Art Generator and Animator

This script provides functions to convert images into ASCII art and animate them.
It uses the PIL library for image processing and asciimatics for animation.

Requires:
- Pillow (PIL)
- asciimatics

Installation:
pip install Pillow asciimatics
"""

from PIL import Image
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError, StopApplication
import time
import os
import random

def image_to_ascii(image_path, width=80):
    """
    Convert an image into ASCII art.

    Parameters:
    - image_path: Path to the image file.
    - width: Desired width of the ASCII art.

    Returns:
    - ASCII art as a string.
    """
    try:
        # Open the image file
        img = Image.open(image_path)
        
        # Resize the image to fit the desired width while maintaining aspect ratio
        aspect_ratio = img.height / img.width
        height = int(width * aspect_ratio)
        img = img.resize((width, height))
        
        # Convert the image to grayscale
        img = img.convert('L')
        
        # Define ASCII characters used to build the output text
        ascii_chars = '@%#*+=-:. '
        
        # Create a string to store the ASCII art
        ascii_str = ''
        
        # Iterate over each pixel in the image
        for y in range(img.height):
            for x in range(img.width):
                # Get the pixel value (grayscale)
                pixel_value = img.getpixel((x, y))
                
                # Map the pixel value to an ASCII character
                ascii_index = int((len(ascii_chars) - 1) * (1 - (pixel_value / 255)))
                ascii_char = ascii_chars[ascii_index]
                
                # Append the ASCII character to the string
                ascii_str += ascii_char
            ascii_str += '\n'
        
        return ascii_str
    
    except FileNotFoundError:
        print(f"Error: The file '{image_path}' was not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def rotate_ascii(ascii_art):
    """
    Rotate the ASCII art 90 degrees clockwise.

    Parameters:
    - ascii_art: ASCII art as a string.

    Returns:
    - Rotated ASCII art as a string.
    """
    lines = ascii_art.split('\n')
    rotated_lines = [''] * len(lines[0])
    
    for line in lines:
        for i, char in enumerate(line):
            rotated_lines[i] = char + rotated_lines[i]
    
    return '\n'.join(rotated_lines)

def animate_ascii(screen, ascii_art, x=0, y=0):
    """
    Animate the ASCII art by moving it across the screen and rotating randomly.

    Parameters:
    - screen: asciimatics Screen object.
    - ascii_art: ASCII art as a string.
    - x: Initial x position.
    - y: Initial y position.
    """
    lines = ascii_art.split('\n')
    screen_height, screen_width = screen.dimensions
    direction = 1  # 1 for right, -1 for left
    rotation_count = 0
    
    while True:
        screen.clear()
        for i, line in enumerate(lines):
            if y + i < screen_height:
                screen.print_at(line, x, y + i)
        
        # Check if the ASCII art hits the edge and reverse direction
        if x + len(max(lines, key=len)) > screen_width or x < 0:
            direction *= -1
        
        # Randomly rotate the ASCII art
        if random.random() < 0.05:
            ascii_art = rotate_ascii(ascii_art)
            lines = ascii_art.split('\n')
        
        # Move the ASCII art
        x += direction
        
        screen.refresh()
        time.sleep(0.1)

def main(screen):
    image_path = './banners/yahoo.png')  # Update this path
    ascii_art = image_to_ascii(image_path)
    
    if ascii_art:
        animate_ascii(screen, ascii_art, x=0, y=0)

def run_animation():
    while True:
        try:
            Screen.wrapper(main)
            break
        except ResizeScreenError:
            pass
        except StopApplication:
            break

if __name__ == "__main__":
    run_animation()
