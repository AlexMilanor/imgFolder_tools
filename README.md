Tools to help organize an image folder.<br>

Teste2
# ImgFolder-Tools
---
Since I love comics and drawing, I commonly save lots and lots of pictures in my images folder.<br>
With time it gets really hard to keep track of them, as I end up with many duplicate images and it's often hard finding a specific image.

Thus, I wrote the codes here to help me with these problems while improving my programming skills.<br>
Sure, I could try and use something like google photos, but where is the fun in that?<br>

# Utilities
---
So far, the tools only do the following:
- Check for duplicate images in the folder and show them to the user.<br>
To do so it calculates the RMSE between the two pixel arrays (after the images are resized to the same width and height).<br>
- Move the images to a user defined folder.<br>
It just automates the act of opening, closing and moving files, but that's already a lot of help.<br>

# How to Use
---
These are only ".py" files, so you need to have a Python compiler to run them. Copy the code to the folder you want to use them on, and compile them there.<br>
They are wroten in Python 3.7.2 and the non-default libraries used are:
- matplotlib 3.0.2
- numpy 1.16.2
- pillow 5.4.1

# Roadmap
---
Since this was a simple project that I did in a couple of hours and it was only to help me with something specific, it is missing lots of stuff. Also, I spent 90% of that time messing around and having fun with adding noise to images and checking for duplicates while reflecting what it meant for two images to be "duplicates". My concept of fun is kinda weird.<br>
The main problems here are that:
- The code structure leaves MUCH to be desired. Well, it actually doesn't exist.
- Missing a requirements.txt file.
- The code doesn't follow any practices for object oriented programming development. Sorry Uncle Bob.
- It doesn't have documentation.
- It doesn't have unit tests.

Ok, basically it have barely anything beyond a proof of concept. This is actually one of the reasons I'm putting it on github, to try and keep developing it while I learn!<br>
Besides, well, saving the code somewhere other than my computer folder hell.
