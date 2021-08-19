# passport RF fields drawer

This project randomly generates images with the transparent background from the proposed test, color and fonts generates images. It is used as a top layer for generating of passports.
## Installation

    1) Create virtual environment:
        conda create -n <your_virtual_environment_name> python=3.7 -y
        conda activate <your_virtual_environment_name>
        
    2) Build virtual environment:
        pip install -r requirements.txt

## Prerequisites

 * Installed [Python](https://www.python.org/downloads/) >= 3.6 or [Anaconda](https://www.anaconda.com/products/individual)  >= 4.10.1

## Launch

```
1) By default:
    python main.py
    
2) Change config:
    python main.py --config_path configs/myconfig.json

For more information launch `python main.py -h`. Please also look at `configs/README.md` to get to know about config parameters.

```