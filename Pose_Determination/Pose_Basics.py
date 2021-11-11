import cv2
import mediapipe as mp
import time
 
cap = cv2.VideoCapture(0)
 
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
 
pTime = 0
cTime = 0
 
while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)
    thumbsUp = False
    thumbsDown = False
    thumbsUpCount = []
    thumbsDownCount = []
    thumbHt = 0
    pinkyHt = 0
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                # print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                #cx is dot width , cy is dot height
                if (cx>600 and cx<800 and cy <700 and cy >600):
                    thumbsUpCount.append(True)
                if (cx>700 and cx<900 and cy <600 and cy >250):
                    thumbsDownCount.append(True)
                print(id, cx, cy)
                if id == 4:
                    thumbHt = cy
                if id == 20:
                    pinkyHt = cy
                cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
 
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
            """
            if thumbHt < pinkyHt:
                thumbsUp = True
            if all(thumbsDownCount):
                thumbsDown = True
            """
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    text= ""
    if thumbHt < pinkyHt:
        text = "Thumbs Up"
    if thumbHt > pinkyHt:
        text = "Thumbs Down"
    #check if true or false here and then set the string text like fps
    #cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                #(255, 0, 255), 3)
    cv2.putText(img, text, (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 255), 3)
 
    cv2.imshow("Image", img)
    cv2.waitKey(1)