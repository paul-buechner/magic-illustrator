import numpy as np
import cv2
import imutils

from imutils import contours
from skimage.filters import threshold_local


def scan(image):
    cv2.imwrite("assets/processing/preprocessed.jpg", image)
    # convert the image to grayscale, blur it, and find edges
    # in the image
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3, 3), 0)
    edged = cv2.Canny(blur, 75, 160)  # 200 default for y

    # show the original image and the edge detected image
    '''
    print("STEP 1: Edge Detection")
    cv2.imshow("Image", imutils.resize(image, height=650))
    cv2.imshow("Blur", imutils.resize(blur, height=650))
    cv2.imshow("Edged", imutils.resize(edged, height=650))
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    '''
    # save them...
    # '''
    cv2.imwrite("assets/processing/gray.jpg", gray)
    cv2.imwrite("assets/processing/blured.jpg", blur)
    cv2.imwrite("assets/processing/edged.jpg", edged)
    # '''

    # find the contours in the edged image, keeping only the
    # largest ones, and initialize the screen contour
    cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST,
                            cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:5]

    # loop over the contours
    for c in cnts:
        # approximate the contour
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)
        # if our approximated contour has four points, then we
        # can assume that we have found our screen
        if len(approx) == 4:
            screenCnt = approx
            # print(screenCnt[2])
            break

    # show the contour (outline) of the piece of paper
    '''
    print("STEP 2: Find contours of paper")
    cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 2)
    cv2.imshow("Outline", imutils.resize(image, height=650))
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    '''
    # save it...
    # '''
    cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 2)
    cv2.imwrite("assets/processing/outline.jpg", image)
    # '''

    return screenCnt, gray
