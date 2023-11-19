import cv2
import os

path = './data/'

def load_images_from_folder(path):
    images = []
    for filename in os.listdir(path):
        img = cv2.imread(os.path.join(path,filename))
        if img is not None:
            images.append(img)
    return images

# array of cats
cats = []

cats = load_images_from_folder(path)

for i in cats:
    print(i)