# Passport RF fields drawer

This project randomly generates images with the transparent background from the proposed test, color and fonts generates images. It is used as a top layer for generating of passports.
## Installation

    1) Create virtual environment:
        conda create -n <your_virtual_environment_name> python=3.7 -y
        conda activate <your_virtual_environment_name>
        
    2) Build virtual environment:
        pip install -r requirements.txt

## Prerequisites

* Installed [Python](https://www.python.org/downloads/) >= 3.6 or [Anaconda](https://www.anaconda.com/products/individual) >= 4.10.1

## Launch

```
1) By default:
    python main.py
    
2) Change config:
    python main.py --config_path configs/myconfig.json

For more information launch `python main.py -h`. Please also look at `configs/README.md` to get to know about config parameters.

```

## Autopep8
[Autopep8](https://pypi.org/project/autopep8/) automatically formats Python code to conform to the PEP 8 style guide. It uses the pycodestyle utility to determine what parts of the code needs to be formatted. autopep8 is capable of fixing most of the formatting issues that can be reported by pycodestyle.

```
1) pip install --upgrade autopep8

    
2) autopep8 --global-config <config_pep> <file>. In project <config_pep> is file 'pep8'.

```