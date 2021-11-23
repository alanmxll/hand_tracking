import cv2
import time

from hand_tracking_module import HandDetector

p_time = 0
c_time = 0
cap = cv2.VideoCapture(0)
detector = HandDetector()

while True:
    success, img = cap.read()
    img = detector.find_hands(img, draw=True)
    lm_list = detector.find_position(img, draw=False)

    if len(lm_list) != 0:
        print(lm_list[4])

    c_time = time.time()
    fps = 1 / (c_time - p_time)
    p_time = c_time

    cv2.putText(img, str(int(fps)), (10, 70),
                cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
