import cv2
import numpy as np
from pyzbar.pyzbar import decode


def img_mode(path):
    img = cv2.imread(path)
    for code in decode(img):
        data = code.data.decode('utf-8')
    return data

# img = cv2.imread("rk.png")
# img = cv2.imread('qrcode_img.jpg')
# img = cv2.resize(img, (240,240))

def video_mode():
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)

    while True:

        success, img = cap.read()

        for code in decode(img):
            data = code.data.decode('utf-8')
            print(data)
            pts = np.array([code.polygon], np.int32)
            pts = pts.reshape((-1, 1, 2))
            pts2 = code.rect
            cv2.polylines(img, [pts], True, (255, 0, 255), 5)
            cv2.putText(img, data, (pts2[0], pts2[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 255), 2)

        cv2.imshow("Image", img)
        cv2.waitKey(1)
