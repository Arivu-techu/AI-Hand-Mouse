import cv2
import mediapipe as mp
import pyautogui
import numpy as np

# 1. Setup
cap = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
drawing_utils = mp.solutions.drawing_utils
screen_w, screen_h = pyautogui.size()

# Smoothing variables (so the cursor doesn't jitter)
smoothening = 7
plocX, plocY = 0, 0
clocX, clocY = 0, 0

print("Script started. Press 'q' to quit.")

while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1) # Mirror view
    frame_h, frame_w, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks

    if hands:
        for hand in hands:
            # Draw landmarks for visual feedback
            drawing_utils.draw_landmarks(frame, hand, mp.solutions.hands.HAND_CONNECTIONS)
            landmarks = hand.landmark
            
            # 2. Get Index Finger Tip (Landmark 8) and Thumb Tip (Landmark 4)
            # We use the Tip of the Index Finger to move the mouse
            index_tip = landmarks[8]
            thumb_tip = landmarks[4]

            # Convert normalized coordinates to pixel coordinates
            x = np.interp(index_tip.x, (0, 1), (0, screen_w))
            y = np.interp(index_tip.y, (0, 1), (0, screen_h))

            # 3. Apply Smoothing
            clocX = plocX + (x - plocX) / smoothening
            clocY = plocY + (y - plocY) / smoothening
            
            pyautogui.moveTo(clocX, clocY)
            plocX, plocY = clocX, clocY

            # 4. Clicking Logic: Distance between Index Tip and Thumb Tip
            # Calculate distance using Pythagoras
            distance = ((index_tip.x - thumb_tip.x)**2 + (index_tip.y - thumb_tip.y)**2)**0.5
            
            # If fingers are touching (distance is small), click!
            if distance < 0.04:
                pyautogui.click()
                pyautogui.sleep(0.2) # Delay to prevent accidental double-clicks

    cv2.imshow('Virtual Hand Mouse', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()