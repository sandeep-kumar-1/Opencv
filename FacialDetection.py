import cv2
import os

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('facial.jpeg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 2, 3)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)


try:
    if not os.path.exists('frames'):
        os.makedirs('frames')
except OSError:
    print ('Error: Creating directory of data')
cv2.imwrite('./frames/pic.jpeg', img)
cv2.waitKey()
