#This code demonstrate how to show location of hand landmark
import cv2
import mediapipe as mp


cap = cv2.VideoCapture(0)

#Call hand pipe line module
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

def showtext (n):
    if n == 0 :
        return cv2.putText(img, str("Fist"), (550, 70), cv2.FONT_HERSHEY_PLAIN, 2,
                (500, 100, 0), 3)
    if n == 1 :
        return cv2.putText(img, str("fingers"), (500, 70), cv2.FONT_HERSHEY_PLAIN, 2,
                (500, 100, 0), 3) 
    if n == 2:
        return cv2.putText(img, str("2 fingers"), (500, 70), cv2.FONT_HERSHEY_PLAIN, 2,
                (500, 100, 0), 3)
    if n == 3:
        return cv2.putText(img, str("3 fingers"), (500, 70), cv2.FONT_HERSHEY_PLAIN, 2,
                (500, 100, 0), 3)
    if n == 4:
        return cv2.putText(img, str("4 fingers"), (500, 70), cv2.FONT_HERSHEY_PLAIN, 2,
                (500, 100, 0), 3) 
    if n == 5:
        return cv2.putText(img, str("Plam"), (550, 70), cv2.FONT_HERSHEY_PLAIN, 2,
                (500, 100, 0), 3)
    if n == 6 :
        return cv2.putText(img, str("Thumb"), (10, 450), cv2.FONT_HERSHEY_PLAIN, 2,
                (100, 500, 500), 3) 
    if n == 7:
        return cv2.putText(img, str("Index"), (150, 450), cv2.FONT_HERSHEY_PLAIN, 2,
                (100, 500, 500), 3)
    if n == 8:
        return cv2.putText(img, str("Middle"), (300, 450), cv2.FONT_HERSHEY_PLAIN, 2,
                (100, 500, 500), 3)
    if n == 9:
        return cv2.putText(img, str("Ring"), (450, 450), cv2.FONT_HERSHEY_PLAIN, 2,
                (100, 500, 500), 3) 
    if n == 10:
        return cv2.putText(img, str("Pinky"), (550, 450), cv2.FONT_HERSHEY_PLAIN, 2,
                (100, 500, 500), 3)
    
    if n == 11:
         return cv2.putText(img, str("LeftHand"), (10, 120), cv2.FONT_HERSHEY_PLAIN, 2,
                (200, 500,0), 2)
    if n == 12:
         return cv2.putText(img, str("RightHand"), (10, 120), cv2.FONT_HERSHEY_PLAIN, 2,
                (200, 500,0), 2)
         


while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    Nfing = 0
    #print(results.multi_hand_landmarks)
    

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                #Count finger 
                if id == 4:
                    id4 = int(id)
                    cx4 = cx
                if id == 3:
                    id3 = int(id)
                    cx3 = cx
                if id == 8:
                    id8 = int(id)
                    cy8 = cy
                if id == 7:
                    id7 = int(id)
                    cy7 = cy
                if id == 12:
                    id12 = int(id)
                    cy12 = cy
                if id == 11:
                    id11 = int(id)
                    cy11 = cy
                if id == 16:
                    id16 = int(id)
                    cy16 = cy
                if id == 15:
                    id15 = int(id)
                    cy15 = cy
                if id == 20:
                    id20 = int(id)
                    cy20 = cy
                if id == 19:
                    id19 = int(id)
                    cy19 = cy

                #Sorting L/R 
                if id == 17:
                    id17 = int(id)
                    cx17 =cx
                if id == 5:
                    id5 = int(id)
                    cx5 = cx
                #Defind finger
                if id == 10:
                    id10 = int(id)
                    cy10 =cy
                if id == 14:
                    id14 = int(id)
                    cy14 = cy
                if id == 18:
                    id18 = int(id)
                    cy18 =cy

               
                    
                
            if cx5 < cx17: #Left
                showtext(11)
                if cy20 > cy19:
                        Nfing = 0
                        showtext(0)
                elif cy16 > cy15:
                        Nfing = 1
                        showtext(1)   
                elif cy12 > cy11:      
                        Nfing = 2
                        showtext(2)
                elif cy8 > cy7:
                        Nfing = 3
                        showtext(3)
                elif cx4 > cx3:
                        Nfing = 4
                        showtext(4) 
                else :
                        Nfing = 5
                        showtext(5)

            if cx5 > cx17 : #Right
                showtext(12)
                if cx4 > cx3 : #Finger name
                     Nfing += 1
                     showtext(6)
                if cy8 < cy7:
                    Nfing += 1
                    showtext(7)
                if cy12 < cy10:
                    Nfing += 1
                    showtext(8)
                if cy16 < cy14:
                    Nfing += 1
                    showtext(9)
                if cy20 < cy18:
                    Nfing += 1
                    showtext(10)
                
            
        
                

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cv2.putText(img, str(int(Nfing)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                (500, 500, 0), 3)
    
    cv2.imshow("Image", img)
    cv2.waitKey(1)
#Closeing all open windows
#cv2.destroyAllWindows()