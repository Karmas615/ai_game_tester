from capture import capture_screen
from detect import detect_ui
from automation import click_button
from state_machine import get_state
from reporter import report_issue
from ocr_module import read_text
import cv2
import time

def main():
    print("AI Game Tester starting...")
    
    
    # Run modules
    print(detect_ui())
    print(read_text("src/images/good2.png"))
    print(click_button())
    print(get_state())
    print(report_issue("Sample bug"))

    time.sleep(2)

    #Capture screen
    frame = capture_screen(save=True)
    cv2.imshow("test", frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    

if __name__ == "__main__":
    main()
