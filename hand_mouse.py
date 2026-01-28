import cv2
import numpy as np
import pyautogui
import time

pyautogui.FAILSAFE = False

cap = cv2.VideoCapture(0)
screen_w, screen_h = pyautogui.size()

# Skin color range (HSV)
lower_skin = np.array([0, 20, 70])
upper_skin = np.array([20, 255, 255])

last_click_time = 0
click_delay = 1.0  # seconds
paused = False

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, lower_skin, upper_skin)
    mask = cv2.GaussianBlur(mask, (7, 7), 0)
    mask = cv2.dilate(mask, None, iterations=2)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours and not paused:
        cnt = max(contours, key=cv2.contourArea)
        area = cv2.contourArea(cnt)

        if area > 3000:
            top = tuple(cnt[cnt[:, :, 1].argmin()][0])
            cv2.circle(frame, top, 10, (0, 0, 255), -1)

            x = np.interp(top[0], [0, frame.shape[1]], [0, screen_w])
            y = np.interp(top[1], [0, frame.shape[0]], [0, screen_h])
            pyautogui.moveTo(x, y, duration=0.08)

        elif 800 < area < 2000:
            current_time = time.time()
            if current_time - last_click_time > click_delay:
                pyautogui.click()
                last_click_time = current_time
                cv2.putText(frame, "CLICK", (50, 80),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.putText(frame, f"Paused: {paused}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    cv2.imshow("Gesture Mouse (Python 3.14)", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break
    elif key == ord('p'):
        paused = not paused

cap.release()
cv2.destroyAllWindows()
