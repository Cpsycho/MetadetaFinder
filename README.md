# MetadetaFinder
This  script serves as a versatile tool for managing image metadata, offering both insight into the technical details of image capture and a means to protect user privacy by removing potentially sensitive information from image files.



# Image Metadata Handler

This Python script provides functionalities to handle metadata within image files, including viewing Exif data and removing metadata for privacy and security.

## Features:

- **View Exif Data**: Displays detailed Exif metadata stored within an image file, offering insights into camera settings, date and time of capture, and more.

- **Remove Metadata from Image**: Removes all metadata from an image file, ensuring the removal of potentially sensitive information such as location details or camera model.

## Usage:

1. **View Exif Data**:
    - Select option 1 when prompted.
    - Enter the path to the image file you want to analyze.
    - Exif data will be displayed, providing valuable information about the image's creation.

2. **Remove Metadata from Image**:
    - Select option 2 when prompted.
    - Enter the path to the image file from which you want to remove metadata.
    - Metadata will be stripped from the image, and the modified image will be saved to a specified location.

## Installation:
$ pkg install python-pip
$ pip install exif
$ git clone https://github.com/Cpsycho/MetadetaFinder.git
