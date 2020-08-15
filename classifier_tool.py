from PIL import Image
import shutil
import os

import matplotlib.pyplot as plt
import numpy as np

category = []
plt.ion()

def get_images():
    all_images = [f for f in os.listdir('./') if os.path.isfile(f) and f[-2:]!='py']
    return all_images


def open_img_as_array(image_filename):
    PIL_image = Image.open(image_filename)
    PIL_image.load()
    img_array = np.asarray(PIL_image, dtype='int32')
    return img_array


def show_image(image_array):
    plt.imshow(img_array)
    plt.pause(0.05)


def first_options():
    folders = [f for f in os.listdir('./') if os.path.isdir(f)]
    return folders


def show_options(folders):
    print("===========================================================")
    print("Pastas existentes:")
    for n,folder in enumerate(folders):
        print(f"({n}) {folder}")
    print("===========================================================")

def get_option(options):   
    print("Digite [c]reate ou o número da pasta")
    choice = input("Código da Pasta: ")

    if choice == 'c':
        folder = input("Nome da Pasta: ")
    else:
        possible_choices = [str(option) for option in range(len(options))]
        assert choice in possible_choices, "Escolha impossível"
        folder = options[int(choice)]

    return folder


def define_folder(image_filename, options):
    show_options(options)
    folder = get_option(options)
    if folder not in options:
        os.mkdir(folder)
        options.append(folder)
    shutil.move(image_filename, folder)


all_images = get_images()
folders = first_options()

for i, image in enumerate(all_images):
    img_array = open_img_as_array(image)
    show_image(img_array)
    define_folder(image, folders)
