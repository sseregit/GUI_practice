import time
import keyboard
from PIL import ImageGrab

def screenshot():
    # 2020년 6월 1일 10시 20분 30초 => _20200601_102030
    curr_time = time.strftime("_%Y%m%d_%H%M%S")
    img = ImageGrab.grab()
    img.save(f"image_{curr_time}.png")

# 사용할 Key 지정 , 함수
# 복합키도 가능 "ctrl+shift+s"등등..
keyboard.add_hotkey("F9", screenshot)
# 사용자가 esc를 누를때 까지 프로그램 수행
keyboard.wait("esc")