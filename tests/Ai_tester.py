import pyautogui

def test_pyautogui_setup():
    assert isinstance(pyautogui.position(), tuple)
