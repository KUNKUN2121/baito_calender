import cv2


def onMouse(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, y)


img = cv2.imread('calender.jpg')
cv2.imshow('Window', img)
cv2.setMouseCallback('Window', onMouse)
cv2.waitKey(0)