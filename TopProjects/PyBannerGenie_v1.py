#!/usr/bin/env python3.12
#For Stability
#PyBannerGenie_Pr0

""" A versatile and User-Friendly Python Tool Designed To Generate High Quality Square Banner From Text """
""" With Options To Creat Custom Professional Banners Tailored To  YOUR Specific NEEDs """
"""BY IRMIYA MALGWI @VILLIAGE_CODER"""

#Imports Used
import pyfiglet
from colorama import init, Fore, Back, Style
from PIL import Image, ImageDraw, ImageFont
import time
import sys

# Initialize Colorama for colored terminal output (cross-platform)
init(autoreset=True)

# Available color choices
COLORS = {
    "red": Fore.RED,
    "green": Fore.GREEN,
    "yellow": Fore.YELLOW,
    "blue": Fore.BLUE,
    "cyan": Fore.CYAN,
    "magenta": Fore.MAGENTA,
    "white": Fore.WHITE
}

# Available fonts for fancy banners
FONTS = ["slant", "block", "standard", "big", "banner3", "digital"]

def banner():
    banner = r"""                                                           
 _____       ____                               _____            _          
|  __ \     |  _ \                             / ____|          (_)         
| |__) |   _| |_) | __ _ _ __  _ __   ___ _ __| |  __  ___ _ __  _  ___     
|  ___/ | | |  _ < / _` | '_ \| '_ \ / _ \ '__| | |_ |/ _ \ '_ \| |/ _ \    
| |   | |_| | |_) | (_| | | | | | | |  __/ |  | |__| |  __/ | | | |  __/    
|_|    \__, |____/ \__,_|_| |_|_| |_|\___|_|   \_____|\___|_| |_|_|\___|    
        __/ |                                                               
       |___/ CODED BY: IRMIYA MALGWI||EMAIL: godofnoor@protonmail.com       
                                                                            
                       https://github.com/XchixoGhostHatkX                  
                                                                            
                       https://facebook.com/irmiya.malgwi                   
                   """
    print(banner)
    
    

def banner_info(text, length=74):
    print("#" + "=" * (length - 2) + "#")
    print(f"=<{text}>".center(length, '='))
    print("#" + "=" * (length - 2) + "#")


def get_color_choice():

    """Asks the user for a color choice."""
    print("\nAvailable colors: " + ", ".join(COLORS.keys()))
    while True:
        color_choice = input("Choose a color: ").strip().lower()
        if color_choice in COLORS:
            return COLORS[color_choice]
        print(Fore.RED + "Invalid color choice. Please choose again.")


def save_banner_to_file(user_text):

    """Saves the generated banner to a text file."""
    save_option = input("Would you like to save this banner to a file? (y/n): ").strip().lower()
    if save_option == 'y':
        filename = input("Enter the filename (without extension): ").strip()
        with open(f"{filename}.txt", "w", encoding="utf-8") as file:
            file.write(user_text)
        print(Fore.GREEN + f"Banner saved as '{filename}.txt' successfully!")
    elif save_option == 'n':
        print(Fore.RED + "Skipping Banner Saving To Text File.")
    else:
        print(Fore.YELLOW + "Error: Please Enter y or n...")
        print(Fore.RED + "Banner Not Saved.")
        

def save_banner_as_image(text: str):
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
    elif save_option == 'n':
        print(Fore.RED + "Skipping Banner Saving As Image.")
    else:
        print(Fore.YELLOW + "Error: Please Enter y or n...")
        print(Fore.RED + "Banner Not Saved.")


def display_square_basic_banner(text: str, color):
    """Displays a basic square banner with a simple border."""
    length = max(20, len(text) + 4)  # Ensures a minimum width
    border = "#" * length

    print(color + border)
    print(color + "#" + " " * (length - 2) + "#")
    print(color + f"# {text.center(length - 4)} #")
    print(color + "#" + " " * (length - 2) + "#")
    print(color + border)
    save_banner_to_file(text)
    save_banner_as_image(text)
    
    
def display_square_fancy_banner(text: str, color):
    """Displays a fancy ASCII-art banner using pyfiglet."""
    print("\nAvailable fonts: " + ", ".join(FONTS))

    while True:
        font_choice = input("Choose a font: ").strip().lower()
        if font_choice in FONTS:
            break
        print(Fore.RED + "Invalid font choice. Please choose again.")

    banner = pyfiglet.figlet_format(text, font=font_choice)
    lines = banner.splitlines()
    max_length = max(len(line) for line in lines)
    border = "#" * (max_length + 4)

    print(color + border)
    for line in lines:
        print(color + f"# {line.ljust(max_length)} #")
    print(color + border)
    save_banner_to_file(banner)
    save_banner_as_image(banner)

    
def display_square_colored_banner(text: str, color):
    """Displays a colorful square framed banner."""
    display_square_basic_banner(text, color)
    save_banner_to_file(text)
    save_banner_as_image(text)


def get_user_choice():
    """Handles user input for menu selection with validation."""
    while True:
        print("\nPlease Choose The Type of Square Banner YOU Want or Exit:\n")
        print("1. Basic Square ASCII Banner")
        print("2. Fancy Square ASCII Art Banner")
        print("3. Colorful Square Framed Banner")
        print("4. Exit From Tool\n")

        choice = input("Enter YOUR Choice (1/2/3/4): ").strip()
        if choice in {'1', '2', '3', '4'}:
           return choice
        print(Fore.RED + "Invalid input. Please enter 1, 2, 3, or 4.")

def get_user_text():
    """Ensures the user provides non-empty input for the banner text."""
    while True:
        text = input("Enter the text for your banner: ").strip()
        if text:
          return text
        print(Fore.RED + "Error: Text cannot be empty. Please try again.")

def main():
    """Main program loop for generating square banners."""
    print(Style.BRIGHT + Fore.MAGENTA + "\nHello World! Welcome To The Python Square Banner Generator Magic!")
    print(Style.BRIGHT + Fore.MAGENTA + "Introducing MySelf!...")
    time.sleep(2)
    #Banner_Info
    #And Banner_Hero
    banner()
    banner_info(".PYBANNERGENIE. ELEVATING ASCII ART: PRECISION, CREATIVITY & CODE.")
    print(Style.BRIGHT + Fore.MAGENTA + "A User-Friendly Python Tool, Designed To Creat High Quality,\nProfessional Costum Banner, Tailored To  YOUR Specific NEEDs.")
    print(Style.BRIGHT + Fore.MAGENTA + "YOU Can Copy Banner Text, Save To File Or Save To Image")
    while True:
    
        choice = get_user_choice()

        if choice == '4':
            confirm_exit = input(Fore.MAGENTA + "Rethink!... Are you sure you want to exit? (y/n): ").strip().lower()
            if confirm_exit == 'y':
                print(Style.BRIGHT + Fore.RED + "Exiting the program. See You Latter! Thanks!.")
                sys.exit()
                break
            if confirm_exit == 'n':
                continue
            else:
                print(Fore.MAGENTA + "Invalid Choice. Please Enter y or n ...")
                continue
        

        user_text = get_user_text()
        user_color = get_color_choice()

        if choice == '1':
            display_square_basic_banner(user_text, user_color)
            
        elif choice == '2':
            display_square_fancy_banner(user_text, user_color)
            
        elif choice == '3':
            display_square_colored_banner(user_text, user_color)

if __name__ == "__main__":
    main()