from logger import log
from capture import capture_screen
from detect import detect_ui
from automation import click_button
from state_machine import get_state
from reporter import report_issue
from ocr_module import read_text
import cv2
import time
from json_storage import save_results
import threading

# -----------------------------
# Threaded loop: capture WHILE analyzing
# -----------------------------
def pipeline_loop(run_time=5):
    start = time.time()

    time.sleep(4)

    while time.time() - start < run_time:
        # 1. Capture ONCE per cycle (not nonstop)
        frame = capture_screen(save=False)
        timestamp = int(time.time())
        cv2.imwrite(f"screenshots/before_{timestamp}.png", frame)

        # 2. Analyze the captured frame
        ui = detect_ui(frame)
        for (x, y, w, h) in ui:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 0), 4)
        cv2.imwrite(f"screenshots/after_{timestamp}.png", frame)

        ocr = read_text(frame)
        clicked = click_button()
        state = get_state()
        bug = report_issue("Sample bug")

        # 3. Display the frame
        cv2.imshow("AI Game Tester", frame)
        cv2.waitKey(1)

        # 4. Save results
        result = {
            "ui": ui,
            "ocr": ocr,
            "clicked": clicked,
            "state": state,
            "bug": bug,
            "time": time.time()
        }
        save_results(result)

        # 5. Small delay so it doesn’t spam screenshots
        time.sleep(0.5)


def main():
    log("AI Game Tester started")
    print("AI Game Tester starting...")

    # Run your pipeline in a thread
    t = threading.Thread(target=pipeline_loop, args=(5,))
    t.start()

    t.join()

    cv2.destroyAllWindows()
    print("AI Game Tester finished.")


if __name__ == "__main__":
    main()

