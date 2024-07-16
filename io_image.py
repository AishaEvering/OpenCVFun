import cv2
import os

path = "data"

image_path = os.path.join(path, 'bird.jpg')

# Read
img = cv2.imread(image_path)
print(img.shape)

# Write
cv2.imwrite(os.path.join(path, 'bird_out.jpg'), img)

# Visualize
cv2.imshow('image', img)
cv2.waitKey(0)
