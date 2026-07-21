from capture import capture_screen
from detect import detect_ui
from ocr import read_text
from automation import click_button
from state_machine import get_state
from reporter import report_issue
import cv2

def main():
    print("AI Game Tester starting...")
    frame = capture_screen(save=True)
    cv2.imshow("test", frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print(detect_ui())
    print(read_text())
    print(click_button())
    print(get_state())
    print(report_issue("Sample bug"))

if __name__ == "__main__":
    main()
