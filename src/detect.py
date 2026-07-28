import cv2
import numpy as np

ui_template = cv2.imread("Templates/menu.png", cv2.IMREAD_COLOR)
print("detect.py loaded")
print("Template loaded:", ui_template is not None)

def detect_ui(frame):
    print("detect_ui called")

    # Convert BGRA → BGR if needed
    if frame.shape[2] == 4:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)

    print("Frame shape:", frame.shape)
    print("Template shape:", ui_template.shape)

    ui_boxes = []

    res = cv2.matchTemplate(frame, ui_template, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(res)

    print("Match confidence:", max_val)

    if max_val > 0.5:
        x, y = max_loc
        w = ui_template.shape[1]
        h = ui_template.shape[0]
        ui_boxes.append((x, y, w, h))

    return ui_boxes
