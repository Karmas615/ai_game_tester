from capture import capture_screen
from detect import detect_ui
from ocr import read_text
from automation import click_button
from state_machine import get_state
from reporter import report_issue

def main():
    print("AI Game Tester starting...")
    print(capture_screen())
    print(detect_ui())
    print(read_text())
    print(click_button())
    print(get_state())
    print(report_issue("Sample bug"))

if __name__ == "__main__":
    main()
