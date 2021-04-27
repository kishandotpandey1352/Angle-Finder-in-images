import cv2
import math

path = 'test.jpg'
img = cv2.imread(path)
pointsList = []

#to capture left mouse button click and get x & y cordinate values
def mousePoints(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:          #event used and called when clicked
        size = len(pointsList)
        if size != 0 and size % 3 != 0:
            cv2.line(img, tuple(pointsList[round((size - 1) / 3) * 3]), (x, y), (0, 0, 255), 2)
        cv2.circle(img, (x, y), 5, (0, 0, 255), cv2.FILLED)                     #size of the pointer being made
        pointsList.append([x, y])                                               #drawn ppoint added to list


def gradient(pt1, pt2):
    return (pt2[1] - pt1[1]) / (pt2[0] - pt1[0])                        #slope = (y2-y1)/(x2-x1)


def getAngle(pointsList):
    pt1, pt2, pt3 = pointsList[-3:]                                     #getting last 3 elements
    m1 = gradient(pt1, pt2)
    m2 = gradient(pt1, pt3)
    angR = math.atan((m2 - m1) / (1 + (m2 * m1)))     #radians                  theta =taninverse(ma1-m2)/(1+m1.m2)
    angD = round(math.degrees(angR))
    if angD <=0:         #degrees
        angD = angD+90   #negative angle handling
    cv2.putText(img, str(angD), (pt1[0] - 40, pt1[1] - 20), cv2.FONT_HERSHEY_COMPLEX,
                1.5, (0, 255,0), 2)


while True:                                                             #Runs always
    if len(pointsList) % 3 == 0 and len(pointsList) != 0:               #Angle can be calculated between 3 points only
        getAngle(pointsList)

    cv2.imshow('Image', img)
    cv2.setMouseCallback('Image', mousePoints)
    if cv2.waitKey(1) &  0xFF == ord('q'):
        pointsList = []
        img = cv2.imread(path)