import cv2
import numpy as np

colors = [(0,0,255), (0,128,255), (0,255,255), (0,255,0), (255,255,0), (255,0,0), (255,0,127), (255,51,255), (255,255,255)]
colorIndex = 0
windowHeight = 900
windowWidth = 1500
sizeOfColorChoices = 100
sizeOfmenuWindow = 170
sizeOfCalculator = 700
sizeOfCalButtons = 150
choice = "Calculator"

img = np.zeros((windowHeight,windowWidth,3), np.uint8)

def setMenu():
	cv2.rectangle(img,(windowWidth-sizeOfmenuWindow,0),(windowWidth, 100),(255,255,255),-1)
	cv2.putText(img, "Paint", (windowWidth-sizeOfmenuWindow+30,50), cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2,cv2.LINE_AA)

	cv2.rectangle(img,(windowWidth-sizeOfmenuWindow,110),(windowWidth, 210),(255,255,255),-1)
	cv2.putText(img, "Piano", (windowWidth-sizeOfmenuWindow+30,170), cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2,cv2.LINE_AA)

	cv2.rectangle(img,(windowWidth-sizeOfmenuWindow,220),(windowWidth, 320),(255,255,255),-1)
	cv2.putText(img, "Calculator", (windowWidth-sizeOfmenuWindow,280), cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2,cv2.LINE_AA)

def setColors():
    for i in range(9):
        cv2.rectangle(img,(0,sizeOfColorChoices*i),(sizeOfColorChoices, sizeOfColorChoices*i+sizeOfColorChoices), colors[i] ,-1)

def setCalculator():
    cv2.rectangle(img,(int(windowWidth/2-sizeOfCalculator/2), 0),(int(windowWidth/2+sizeOfCalculator/2), windowHeight-50),(0,255,0),2)
    cv2.rectangle(img,(int(windowWidth/2-sizeOfCalculator/2)+20, 20),(int(windowWidth/2+sizeOfCalculator/2)-20, sizeOfCalButtons),(0,255,0),2)

    n = int(windowWidth/2-sizeOfCalculator/2)
    
    for y in range(4):
        for x in range(4):
            cv2.rectangle(img, (sizeOfCalButtons*x+20+(20*x)+n, sizeOfCalButtons*y+10+(20*y)+sizeOfCalButtons),(sizeOfCalButtons*x+sizeOfCalButtons+20+(20*x)+n, sizeOfCalButtons*y+sizeOfCalButtons+20+(20*y)+sizeOfCalButtons),(0,255,0),2)

    for i in range(3):
        cv2.putText(img, str(i+1), (n+50+sizeOfCalButtons*i+10+(20*i), sizeOfCalButtons*2-10), cv2.FONT_HERSHEY_SIMPLEX,3,(0,255,255),2,cv2.LINE_AA)

    cv2.putText(img, "+", (n+50+sizeOfCalButtons*3+5+(20*3), sizeOfCalButtons*2-30), cv2.FONT_HERSHEY_SIMPLEX,3,(0,255,255),2,cv2.LINE_AA)

    for i in range(3):
        cv2.putText(img, str(i+4), (n+50+sizeOfCalButtons*i+10+(20*i), sizeOfCalButtons*3+10), cv2.FONT_HERSHEY_SIMPLEX,3,(0,255,255),2,cv2.LINE_AA)

    cv2.putText(img, "-", (n+50+sizeOfCalButtons*3+5+(20*3), sizeOfCalButtons*3-10), cv2.FONT_HERSHEY_SIMPLEX,3,(0,255,255),2,cv2.LINE_AA)

    for i in range(3):
        cv2.putText(img, str(i+7), (n+50+sizeOfCalButtons*i+10+(20*i), sizeOfCalButtons*4+15), cv2.FONT_HERSHEY_SIMPLEX,3,(0,255,255),2,cv2.LINE_AA)

    cv2.putText(img, "*", (n+50+sizeOfCalButtons*3+20+(20*3), sizeOfCalButtons*4+15), cv2.FONT_HERSHEY_SIMPLEX,3,(0,255,255),2,cv2.LINE_AA)

    cv2.putText(img, "-/+", (n+20, sizeOfCalButtons*5+30), cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,255),2,cv2.LINE_AA)
    cv2.putText(img, "0", (n+85+sizeOfCalButtons*1, sizeOfCalButtons*5+30), cv2.FONT_HERSHEY_SIMPLEX,3,(0,255,255),2,cv2.LINE_AA)
    cv2.putText(img, "=", (n+95+sizeOfCalButtons*2, sizeOfCalButtons*5+30), cv2.FONT_HERSHEY_SIMPLEX,3,(0,255,255),2,cv2.LINE_AA)

    cv2.putText(img, "/", (n+95+sizeOfCalButtons*3, sizeOfCalButtons*5+40), cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,255),2,cv2.LINE_AA)

def move(event,x,y,flags,param):
   
    global colorIndex
    global img
    global choice

    if x > windowWidth - sizeOfmenuWindow and y < 320:
        if y < 100:
            choice = "paint"
            img = np.zeros((windowHeight,windowWidth,3), np.uint8)
            setColors()
        elif y < 210:
            choice = "piano"
            img = np.zeros((windowHeight,windowWidth,3), np.uint8)
        elif y < 320:
            choice = "calculator"
            img = np.zeros((windowHeight,windowWidth,3), np.uint8)
            setCalculator()

        setMenu()
    
    if choice is "paint":
        if x < sizeOfColorChoices:
        
            for i in range(9):
                if y < sizeOfColorChoices * i + sizeOfColorChoices:
                    colorIndex = i
                    break

        if event == cv2.EVENT_MOUSEMOVE:
            cv2.circle(img,(x,y),12, colors[colorIndex], -1)


cv2.namedWindow('image')
cv2.setMouseCallback('image',move)
setMenu()
setColors()

while(1):
    
    cv2.imshow('image',img)
    
    if cv2.waitKey(20) & 0xFF == 113:
        break

cv2.destroyAllWindows()
