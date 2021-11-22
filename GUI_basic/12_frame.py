from tkinter import *

root = Tk()
root.title("GUI")
root.geometry("1024x768")

Label(root, text="메뉴를 선택해 주세요.").pack(side="top")

Button(root, text="주문하기").pack(side="bottom")

# relief : 테두리 관련 옵션 / bd : 외곽선 표시 옵션
frame_burger = Frame(root, relief="solid", bd=1)
# side 위치지정 , fill="both" 그공간을 꽉채움, expand=True 옆으로 꽉채움
frame_burger.pack(side="left", fill="both", expand=True)

Button(frame_burger, text="햄버거").pack()
Button(frame_burger, text="치즈버거").pack()
Button(frame_burger, text="치킨버거").pack()

# LabelFrame은 제목이 있는 프레임
frame_drink = LabelFrame(root, text="음료")
Button(frame_drink, text="콜라").pack()
Button(frame_drink, text="사이다").pack()
frame_drink.pack(side="right", fill="both", expand=True)

root.mainloop()
