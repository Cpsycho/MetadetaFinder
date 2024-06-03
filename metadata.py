from PIL import Image
from PIL.ExifTags import TAGS
import time
import os

# ANSI color codes
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
END = "\033[0m"
WATERMARK = "Cʀᴇᴀᴛᴇᴅ ʙʏ Cʏʙᴇʀ⁻ᴘsʏᴄʜᴏ "

def get_exif_data(image_path):
    try:
        image = Image.open(image_path)
        exif_data = image._getexif()
        if exif_data:
            exif_info = {}
            for tag, value in exif_data.items():
                tag_name = TAGS.get(tag, tag)
                exif_info[tag_name] = value
            return exif_info
        else:
            print("No Exif data found.")
            return None
    except Exception as e:
        print(f"{RED}Error:{END}", e)
        return None

def view_exif_data(image_path):
    exif_info = get_exif_data(image_path)
    if exif_info:
        print(f"{YELLOW}Exif Data:{END}")
        for tag, value in exif_info.items():
            print(f"{GREEN}{tag}:{END} {value}")
    else:
        print("No Exif data available.")

def remove_metadata(image_path):
    try:
        image = Image.open(image_path)
        image_without_exif = Image.new(image.mode, image.size)
        image_without_exif.putdata(list(image.getdata()))
        download_folder = os.path.expanduser("~/storage/downloads/")
        output_path = os.path.join(download_folder, "rm_metadata_" + os.path.basename(image_path))
        image_without_exif.save(output_path)
        print(f"{GREEN}Metadata removed and image saved to {output_path} successfully!{END}")
    except Exception as e:
        print(f"{RED}Error:{END}", e)

def animate_loading():
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(0.5)
    print()

if __name__ == "__main__":
    os.system("clear")
    print(f"\033[1;35m{'='*40}\n{' '*10}Welcome{' '*10}\n{'='*40}\033[0m")
    animate_loading()
    print(f"{YELLOW}1. View Exif data{END}")
    print(f"{YELLOW}2. Remove metadata from image{END}")
    print(f"{WATERMARK}")
    choice = input(f"{GREEN}Enter your choice (1 or 2):{END} ")

    if choice == '1':
        image_path = input(f"{GREEN}Enter the path to the image file:{END} ")
        view_exif_data(image_path)
    elif choice == '2':
        image_path = input(f"{GREEN}Enter the path to the image file:{END} ")
        remove_metadata(image_path)
    else:
        print(f"{RED}Invalid choice. Please enter either 1 or 2.{END}")