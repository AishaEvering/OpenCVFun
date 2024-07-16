import cv2
import os

path = "data"

video_path = os.path.join(path, 'monkey.mp4')

# Read
video = cv2.VideoCapture(video_path)

# Visualize
ret = True

while ret:
  ret, frame = video.read()

  if ret:
    cv2.imshow('frame', frame)
    cv2.waitKey(40)

video.release()
cv2.destroyAllWindows()