import cv2
import numpy as np
from scipy.stats import itemfreq


def get_dominant_color(image, n_colors):
    pixels = np.float32(image).reshape((-1, 3))  # reshape придает массиву новую форму без изменения его данных.
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 200, .1)
    flags = cv2.KMEANS_RANDOM_CENTERS
    flags, labels, centroids = cv2.kmeans(
        pixels, n_colors, None, criteria, 10, flags)
    palette = np.uint8(centroids)
    return palette[np.argmax(itemfreq(labels)[:, -1])]


clicked = False

lower_blue = np.array([110, 50, 50])
upper_blue = np.array([130, 255, 255])
lower_red = np.array([160,100,20])
upper_red = np.array([179,255,255])
cameraCAP = cv2.VideoCapture(0)
cv2.namedWindow("cam")

success, frame = cameraCAP.read()

flag, img = cameraCAP.read()

while success and not clicked:
    cv2.waitKey(1)
    success, frame = cameraCAP.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    image = cv2.medianBlur(gray, 37)
    circles = cv2.HoughCircles(image, cv2.HOUGH_GRADIENT, 1, 50, param1=120, param2=40)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    maskb = cv2.inRange(hsv, lower_blue, upper_blue)
    maskr = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame, frame, mask=maskb)
    res2 = cv2.bitwise_and(frame, frame, mask=maskr)
    res3 = res + res2
    cv2.imshow("res2", res3)


    if not circles is None:
        circles = np.int16(np.around(circles))
        print(circles[:, :, 2][0])
        maxrad, minrad = 0, 0
        for i in range(len(circles[:, :, 2][0])):
            if circles[:, :, 2][0][i] > 50 and circles[:, :, 2][0][i] > maxrad:
                print(circles[:, :, 2][0])
                max_i = i
                maxrad = circles[:, :, 2][0][i]
        x, y, z = circles[:, :, :][0][minrad]
        if y > z and x > z:
            squ = frame[y - z:y + z, x - z:z + x]

            most_color = get_dominant_color(squ, 2)
            if most_color[2] > 100:
                print("stop")
            elif most_color[0] > 80:
                zone_0 = squ[squ.shape[0] * 3 // 8:squ.shape[0] * 5 // 8, squ.shape[1] * 1 // 8:squ.shape[1] * 3 // 8]
                cv2.imshow('Zone0', zone_0)
                zone_0_color = get_dominant_color(zone_0, 1)
                zone_1 = squ[squ.shape[0] * 1 // 8:squ.shape[0] * 3 // 8, squ.shape[1] * 3 // 8: squ.shape[1] * 5 // 8]
                cv2.imshow('Zone1', zone_1)
                zone_1_color = get_dominant_color(zone_1, 1)
                zone_2 = squ[squ.shape[0] * 3 // 8:squ.shape[0] * 5 // 8, squ.shape[1] * 5 // 8:squ.shape[1] * 7 // 8]
                cv2.imshow('Zone2', zone_2)
                zone_2_color = get_dominant_color(zone_2, 1)
                if zone_1_color[2] < 60:
                    if sum(zone_1_color) > sum(zone_2_color):
                        print("left")
                    else:
                        print("RIGHT")

                    if sum(zone_1_color) > sum(zone_0_color) and sum(zone_1_color) > sum(zone_2_color):
                        print("FORWARD")
                    elif sum(zone_0_color) > sum(zone_2_color):
                        print("FORWARD AND LEFT")
                    else:
                        print("FORWARD AND RIGHT")
            else:
                print("N/A")

        for i in circles[0, :]:
            cv2.circle(frame, (i[0], i[1]), i[2], (0, 255, 0), 2)
            cv2.circle(frame, (i[0], i[1]), 2, (0, 0, 255), 3)

    cv2.imshow('camera', frame)

cv2.destroyAllWindows()
cameraCAP.release()
