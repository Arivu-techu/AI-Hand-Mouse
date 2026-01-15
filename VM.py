import cv2
import mediapipe as mp
import pyautogui
import numpy as np
cap = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
screen_w, screen_h = pyautogui.size()
current_mode = "Navigation" # Toggle between Nav and Scroll

while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    h_cam, w_cam, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    res = hand_detector.process(rgb_frame)
    
    if res.multi_hand_landmarks:
        for hand_lms in res.multi_hand_landmarks:
            lms = hand_lms.landmark
            ix, iy = int(lms[8].x * w_cam), int(lms[8].y * h_cam)
            mx, my = int(lms[12].x * w_cam), int(lms[12].y * h_cam)
            tx, ty = int(lms[4].x * w_cam), int(lms[4].y * h_cam)
            mode_dist = np.hypot(ix - mx, iy - my)
            
            if mode_dist < 40:
                current_mode = "Scroll"
                color = (0, 255, 0) # Green
            else:
                current_mode = "Navigation"
                color = (255, 0, 0) # Blue
            if current_mode == "Navigation":
                # Standard Mouse Movement
                nx = np.interp(ix, (100, w_cam-100), (0, screen_w))
                ny = np.interp(iy, (100, h_cam-100), (0, screen_h))
                pyautogui.moveTo(nx, ny)
                
                # Pinch to click
                if np.hypot(ix - tx, iy - ty) < 30:
                    pyautogui.click()
            
            elif current_mode == "Scroll":
                scroll_amount = (iy - (h_cam // 2)) // 5
                pyautogui.scroll(-scroll_amount)
                cv2.putText(frame, f"MODE: {current_mode}", (10, 50), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
            mp.solutions.drawing_utils.draw_landmarks(frame, hand_lms, mp.solutions.hands.HAND_CONNECTIONS)

    cv2.imshow("Innovation Demo", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
