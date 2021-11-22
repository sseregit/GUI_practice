import time
from PIL import ImageGrab

# 5초 대기
time.sleep(5)

for i in range(1,11):
    # 현재 스크린 이미지를 가져온다.
    img = ImageGrab.grab()
    img.save("D:/GUI_practice/image/img{}.png".format(i))
    time.sleep(2)