import os
import cv2

path = "data"
image_path = os.path.join(path, 'bird.jpg')


# resizing
def resize(path: str = image_path):

    img = cv2.imread(path)
    print(f'Before: {img.shape}')

    resize_img = cv2.resize(img, (180, 270))
    print(f'After: {resize_img.shape}')

    cv2.imshow('img', img)
    cv2.imshow('resized img', resize_img)
    cv2.waitKey(0)


def crop(path: str = image_path):

    img = cv2.imread(path)
    print(f'Image: {img.shape}')

    cropped_img = img[200:360, 100:540]

    cv2.imshow('img', img)
    cv2.imshow('cropped_img', cropped_img)
    cv2.waitKey(0)

crop()