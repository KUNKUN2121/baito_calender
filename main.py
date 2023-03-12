import cv2


def onMouse(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, y)


img = cv2.imread('calender.jpg')

height, width = img.shape[:2]
print(height)  # 1241
print(width)  # 1754

half_height = int(height / 2)
half_width = int(width / 2)



cv2.line(img,
    pt1=(half_width, 0),
    pt2=(half_width, height),
    color=(0, 255, 0),
    thickness=3,
    lineType=cv2.LINE_4,
    shift=0)


leftWidth = int(width / 16)
rightWidth = int(width - leftWidth)
upHeight = int(height / 5)
downHeight = int(height - (height / 20))

cv2.rectangle(img,
              pt1=(leftWidth,upHeight),
              pt2=(rightWidth,downHeight),
              color=(0, 22, 20),
              thickness=3,
              lineType=cv2.LINE_4,
              )

cv2.imshow('Window', img)
cv2.setMouseCallback('Window', onMouse)
cv2.waitKey(0)