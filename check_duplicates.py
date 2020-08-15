from PIL import Image
import os

import matplotlib.pyplot as plt
import numpy as np


IMG_EXTENSIONS = ['bmp','jpg','jpeg','png'] 
def get_all_images():
    imageFiles = [f for f in os.listdir('./') if (os.path.isfile(f) \
                  and os.path.splitext(f)[1][1:] in IMG_EXTENSIONS) ]
    return imageFiles

def get_image(imageFileName):
    PIL_image = Image.open(imageFileName).convert('RGB')
    return PIL_image

def get_image_array(PIL_image):
    img_array = np.asarray(PIL_image, dtype="int32")
    return img_array

def standardize_size(PIL_image1, PIL_image2):

    width1, height1 = PIL_image1.size
    width2, height2 = PIL_image2.size

    width = min([width1, width2])
    height = min([height1, height2])

    new_size = (width, height)

    PIL_image1_resized = PIL_image1.resize(new_size)
    PIL_image2_resized = PIL_image2.resize(new_size)

    return PIL_image1_resized,PIL_image2_resized

def show_images(img_array_1, img_array_2):
    fig, ax = plt.subplots(1,2,figsize=(20,20),dpi=150)
    ax[0].imshow(img_array_1)
    ax[1].imshow(img_array_2)
    plt.show()
    plt.pause(0.05)


count = 0
imageFiles = get_all_images()
for n,imageFile1 in enumerate(imageFiles):
    image1 = get_image(imageFile1)
    for imageFile2 in imageFiles[n+1:]:
        image2 = get_image(imageFile2)

        if image1.size != image2.size:
            image1,image2 = standardize_size(image1, image2)

        img_array_1 = get_image_array(image1)
        img_array_2 = get_image_array(image2)

        if np.sqrt(((img_array_1 - img_array_2)**2.0).mean()) < 80:
            print(f'Esquerda:{imageFile1}, Direita:{imageFile2}')
            show_images(img_array_1, img_array_2)
