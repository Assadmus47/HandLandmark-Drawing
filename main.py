import cv2 
import mediapipe as mp 

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,700)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,700)
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)

while True :
    sucess ,frame = cap.read()  
    if sucess:
        RGB_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(frame)
        if results.multi_hand_landmarks:
            indexTip = results.multi_hand_landmarks[0].landmark[8]       
            mp_drawing.draw_landmarks(frame,results.multi_hand_landmarks[0],mp_hands.HAND_CONNECTIONS)
            print(indexTip)
        
        
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) == ord('q') :
            break  
        
        
        
cv2.destroyAllWindows()
