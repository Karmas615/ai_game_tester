import mss
import numpy as np
import cv2
import time
import os

def capture_screen(save=False):
    with mss.mss() as sct:
        monitor = sct.monitors[1]  # full screen
        frame = sct.grab(monitor)

        # Convert BGRA → BGR
        img = np.array(frame)
        img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)

        # Auto-save screenshot if enabled
        if save:
            os.makedirs("screenshots", exist_ok=True)
            filename = f"screenshots/{int(time.time())}.png"
            cv2.imwrite(filename, img)

        return img
