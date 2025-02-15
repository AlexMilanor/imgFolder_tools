# ImgFolder-Tools

![Status Badge](https://img.shields.io/badge/status-nice-green?style=plastic)
![Roadmap Badge](https://img.shields.io/badge/roadmap-existant-blue?style=plastic)


---
Since I love comics and drawing, I commonly save lots and lots of pictures in my images folder.

With time it gets really hard to keep track of them, as I end up with many duplicate images and it's often hard finding a specific image.

Thus, I wrote the codes here to help me with these problems while improving my programming skills.

Sure, I could try and use something like google photos, but where is the fun in that?

# Utilities
---
So far, the tools only do the following (it does not do any of those at this time):
- Check for duplicate images in the folder and show them to the user.<br>
To do so it calculates the RMSE between the two pixel arrays (after the images are resized to the same width and height).<br>
- Move the images to a user defined folder.<br>
It just automates the act of opening, closing and moving files, but that's already a lot of help.<br>

# How to Use
---
These are only ".py" files, so you need to have a Python compiler to run them. Copy the code to the folder you want to use them on, and use them there.

The main entry point is the `app.py` file. Using the python compiler, you can use that file as a CLI (similar to git? something like that).

The project is written in Python 3.12.8 and the required libraries are:
- ruamel.yaml (0.18.10)
- pillow (11.1.0)
- numpy (2.2.2)
- matplotlib (3.10.0)
- pytest (8.3.4)