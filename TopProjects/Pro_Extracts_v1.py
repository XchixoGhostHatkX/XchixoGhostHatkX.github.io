import pyfiglet
from colorama import init, Fore, Back, Style
from PIL import Image, ImageDraw, ImageFont

# Initialize Colorama for colored terminal output (cross-platform)
init(autoreset=True)

# Available text colors
TEXT_COLORS = {
    "red": Fore.RED, "green": Fore.GREEN, "yellow": Fore.YELLOW,
    "blue": Fore.BLUE, "cyan": Fore.CYAN, "magenta": Fore.MAGENTA, "white": Fore.WHITE
}

# Available background colors
BG_COLORS = {
    "red": Back.RED, "green": Back.GREEN, "yellow": Back.YELLOW,
    "blue": Back.BLUE, "cyan": Back.CYAN, "magenta": Back.MAGENTA, "white": Back.WHITE
}

# Available border styles
BORDER_STYLES = ["#", "*", "=", "-"]
# Available fonts for fancy banners
FONTS = ["slant", "block", "standard", "big", "banner3", "digital"]

# Available text alignments
ALIGNMENTS = ["left", "center", "right"]


def save_banner_to_file(banner_text):
    """Saves the generated banner to a text file."""
    save_option = input("Would you like to save this banner to a file? (y/n): ").strip().lower()
    if save_option == 'y':
        filename = input("Enter the filename (without extension): ").strip()
        with open(f"{filename}.txt", "w", encoding="utf-8") as file:
            file.write(banner_text)
        print(Fore.GREEN + f"Banner saved as '{filename}.txt' successfully!")


def save_banner_as_image(text):
    """Saves the fancy ASCII banner as a PNG image."""
    save_option = input("Would you like to save this banner as an image? (y/n): ").strip().lower()
    if save_option == 'y':
        filename = input("Enter the filename (without extension): ").strip()
        font = ImageFont.load_default()
        image_size = (600, 200)  # Adjust based on text size
        img = Image.new("RGB", image_size, "black")
        draw = ImageDraw.Draw(img)
        draw.text((10, 10), text, font=font, fill="white")
        img.save(f"{filename}.png")
        print(Fore.GREEN + f"Banner saved as '{filename}.png' successfully!")

def display_banner(text, length=44):
    print("#" + "=" * (length - 2) + "#")
    print(f"<{text}>".center(length, '='))
    print("#" + "=" * (length - 2) + "#")

# Example usage
display_banner("Welcome to My Python Script")
save_banner_to_file(banner_text)
save_banner_as_image(banner_text)