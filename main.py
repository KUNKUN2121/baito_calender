import cv2
import datetime as dt
import locale
import calendar
locale.setlocale(locale.LC_TIME, 'ja_JP.UTF-8')

year = 2023
mounth = 4

def onMouse(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, y)


date = dt.date(year, mounth, 1)
print("曜日数" + str(date.weekday()))
print("曜日" + str(date.strftime('%A')))
print("一ヶ月の日数" + str(calendar.monthrange(year, mounth)[1]))

img = cv2.imread('calender.jpg')

height, width = img.shape[:2]
print(height)  # 1241
print(width)  # 1754

leftWidth = int(width / 16)
rightWidth = int(width - leftWidth)
upHeight = int(height / 4.15)
downHeight = int(height - (height / 20))

width7 = int((rightWidth - leftWidth) / 7)
height7 = int((downHeight - upHeight) / 6)

tempWidth = leftWidth
tempHeight = upHeight + height7




#まず最初の左の座標取得
temp1x = int(leftWidth)
temp1y = int(upHeight)
temp2x = int(temp1x + width7)
temp2y =  int(temp1y + height7)
counuter = 0

# 6回たて回す
for i in range(6):
    for n in range(7):
        if (counuter > calendar.monthrange(year, mounth)[1] + date.weekday()):
            break
        else :
            if counuter >  date.weekday():
                # 描画     
                cv2.rectangle(img,
                    pt1=(temp1x, temp1y),
                    pt2=(temp2x, temp2y),
                    color=(0, 25, 0),
                    thickness=10,
                    lineType=cv2.LINE_4,
                    shift=0)
                cv2.putText(img,
                    text=str(n),
                    org=(temp1x, temp1y),
                    fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                    fontScale=1.0,
                    color=(0, 255, 0),
                    thickness=2,
                    lineType=cv2.LINE_4) 
            temp1x = temp1x + width7
            temp2x = temp2x + width7
            counuter = counuter+ 1

    temp1x = int(leftWidth)
    temp1y = int(temp1y + height7)
    temp2x = int(temp1x + width7)
    temp2y = int(temp1y + height7)

cv2.imshow('Window', img)
cv2.setMouseCallback('Window', onMouse)
cv2.waitKey(0)