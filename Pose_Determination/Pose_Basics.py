import cv2
import mediapipe as mp
import time
import re
import sys
import os
import numpy as np
 
def controlVolume():
    cap = cv2.VideoCapture(0)
    cv2.startWindowThread()
    mpHands = mp.solutions.hands
    hands = mpHands.Hands()
    mpDraw = mp.solutions.drawing_utils
    
    pTime = 0
    cTime = 0
    thumbsUp = True
    thumbsDown = True
    notQuit = True
    openThumb = False
    openPointer = False
    openMiddle = False
    openRing = False
    openPinky = False
    coordinateValues = np.zeros(21)

    #display window to bring camera to front
    cv2.namedWindow("GetFocus", cv2.WINDOW_NORMAL)
    pic = np.zeros(10000)
    cv2.imshow("GetFocus", pic)
    cv2.setWindowProperty("GetFocus", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.waitKey(1)
    cv2.setWindowProperty("GetFocus", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_NORMAL)
    cv2.destroyWindow("GetFocus")


    while notQuit:
        success, img = cap.read()
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(imgRGB)
        # print(results.multi_hand_landmarks)
        thumbHt = 0
        pinkyHt = 0
        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                for id, lm in enumerate(handLms.landmark):
                    # print(id, lm)
                    h, w, c = img.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    print(id, cx, cy)
                    coordinateValues[id-1] = cy
                    if id == 4:
                        thumbHt = cy
                    if id == 20:
                        pinkyHt = cy
                    cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
    
                mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        text= ""
        if thumbHt < pinkyHt:
            text = "Thumbs Up"
            #thumbsUp = False
            os.system("cliclick kp:volume-up")
        if thumbHt > pinkyHt:
            text = "Thumbs Down"
            os.system("cliclick kp:volume-down")
            #thumbsDown = False

        if(coordinateValues[2] < coordinateValues[1] and coordinateValues[3] < coordinateValues[1]):
            openThumb = True
        if(coordinateValues[6] < coordinateValues[5] and coordinateValues[7] < coordinateValues[5]):
            openPointer = True
        if(coordinateValues[10] < coordinateValues[9] and coordinateValues[11] < coordinateValues[9]):
            openMiddle = True
        if(coordinateValues[14] < coordinateValues[13] and coordinateValues[15] < coordinateValues[13]):
            openRing = True
        if(coordinateValues[18] < coordinateValues[17] and coordinateValues[19] < coordinateValues[17]):
            openPinky = True

        if(openThumb and openPointer and openMiddle and openRing and openPinky):
            notQuit = False
            text = "Stop"
        #check if true or false here and then set the string text like fps
        #cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                    #(255, 0, 255), 3)
        cv2.putText(img, text, (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                    (255, 0, 255), 3)

        cv2.imshow("Image", img)
        cv2.waitKey(1)
    
    cv2.waitKey(1)
    cv2.destroyAllWindows()
    cv2.waitKey(1)