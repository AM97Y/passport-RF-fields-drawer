ttf-main README.md

# passport RF fields drawer

This project is randomly from the proposed test, color and fonts generates images with a transparent background.
This is used as a top layer when generating passports.
## Installation

    1) Create virtual environment:
        conda create -n gen_img python=3.7 -y
        conda activate gen_img
        
    2) Build virtual environment:
        pip install -r requirements.txt

## Launch

```
1) Edit file config.py
    
text - a document with texts
    colors - text colors
    fronts - types of fonts
    
    size_fronts_min - minimum font size
    size_fronts_max - maximum font size
    
    color_img - background color, last number is transparency
    size_image - image size
    
    height - the height of the upper left corner of the signature
    weight - the width of the upper left corner of the signature
    
    output_path - folder where the result is saved

2) python main.py

```