from logger import log
import mss
import cv2
import numpy as np
import os
import time

def capture_screen(save=False):
    log("Capturing screen")

    with mss.mss() as sct:
        screenshot = sct.grab(sct.monitors[1])
        img = np.array(screenshot)

        if save:
            os.makedirs("screenshots", exist_ok=True)
            filename = f"screenshots/{int(time.time())}.png"
            cv2.imwrite(filename, img)
            log(f"Screenshot saved to {filename}")

    log("Screen capture complete")
    return img
