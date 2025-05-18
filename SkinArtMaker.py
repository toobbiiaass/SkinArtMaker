from PIL import Image
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from colorama import init, Fore
import os

init(autoreset=True)
root = Tk()
root.withdraw()
print(f"{Fore.MAGENTA}+-----------------------------------------------------------+")
print(f"{Fore.MAGENTA}|                    SkinArt Maker by vuacy                 |")
print(f"{Fore.MAGENTA}|-----------------------------------------------------------|")
print(f"{Fore.MAGENTA}| Discord Server: https://discord.gg/ExGSqUT6qk             |")
print(f"{Fore.MAGENTA}|                                                           |")
print(f"{Fore.MAGENTA}|                                                           |")
print(f"{Fore.MAGENTA}|                      Press Enter to Start                 |")
print(f"{Fore.MAGENTA}+-----------------------------------------------------------+")
input()
output_folder = input(f"{Fore.MAGENTA}Enter the name of the output folder: ").strip()

if os.path.exists(output_folder):
    print(f"{Fore.MAGENTA}The folder '{output_folder}' already exists. The program will exit.")
    exit()
else:
    os.makedirs(output_folder)
    print(f"{Fore.MAGENTA}The folder '{output_folder}' has been created.")

file_path = askopenfilename(title="Select an image", filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
if not file_path:
    print(f"{Fore.MAGENTA}No file selected. Exiting the program.")
    exit()

image = Image.open(file_path)

orig_width, orig_height = image.size

target_width = 72
target_height = 24
target_aspect_ratio = target_width / target_height
original_aspect_ratio = orig_width / orig_height

def align_image():
    print(f"\n{Fore.MAGENTA}How should the image be positioned?")
    print(f"{Fore.MAGENTA}1: Aligned to the top")
    print(f"{Fore.MAGENTA}2: Aligned to the center")
    print(f"{Fore.MAGENTA}3: Aligned to the bottom")
    choice = input(f"{Fore.MAGENTA}Choose an option (1/2/3): ").strip()

    if original_aspect_ratio > target_aspect_ratio:
        new_width = int(orig_height * target_aspect_ratio)
        new_height = orig_height
        left = (orig_width - new_width) // 2
        top = 0
    else:
        new_width = orig_width
        new_height = int(orig_width / target_aspect_ratio)
        left = 0

        if choice == "1":
            top = 0
        elif choice == "2":
            top = (orig_height - new_height) // 2
        elif choice == "3":
            top = orig_height - new_height
        else:
            print(f"{Fore.MAGENTA}Invalid input. Default: Center align.")
            top = (orig_height - new_height) // 2

    right = left + new_width
    bottom = top + new_height

    cropped_image = image.crop((left, top, right, bottom))
    cropped_image.show()

    response = input(f"{Fore.MAGENTA}Does the cropped area look good? (yes/no): ").strip().lower()
    return response, cropped_image

response, cropped_image = align_image()

while response != "yes":
    response, cropped_image = align_image()

resized_image = cropped_image.resize((target_width, target_height), Image.Resampling.NEAREST)

template_path = "template/skinTemplate.png"
template = Image.open(template_path)

chunk_size = 8

template_x_start = 8
template_y_start = 8

skin_number = 1

for y in range(target_height - chunk_size, -1, -chunk_size):
    for x in range(target_width - chunk_size, -1, -chunk_size):
        cropped_part = resized_image.crop((x, y, x + chunk_size, y + chunk_size))

        skin_copy = template.copy()

        skin_copy.paste(cropped_part, (template_x_start, template_y_start))

        output_path = os.path.join(output_folder, f"skin{skin_number}.png")
        skin_copy.save(output_path)

        skin_number += 1

print(f"{Fore.MAGENTA}All {skin_number - 1} skins have been successfully saved to '{output_folder}'!")