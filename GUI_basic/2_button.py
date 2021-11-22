from tkinter import *

root = Tk()
# title
root.title("Jang GUI")
btn1 = Button(root, text="버튼1")
# 실제로 포함된다.
btn1.pack()
# padx = button의 x 여백, pady = button의 y 여백
# text가 넓어지면 같이 넓어짐
btn2 = Button(root, padx=5, pady=10, text="버튼2222222")
btn2.pack()
btn3 = Button(root, padx=10, pady=5, text="버튼3")
btn3.pack()
# width와 height는 고정값으로 text가 넓어져도 같이 넓어지지않는다.
btn4 = Button(root, width=10, height=3, text="버튼")
btn4.pack()
# fg 버튼 색 , bg 배경색
btn5 = Button(root, fg="red", bg="yellow", text="버튼5")
btn5.pack()
# Image를 적용시킨다.
photo = PhotoImage(file="./image/img.png")
btn6 = Button(root, image=photo)
btn6.pack()
# 버튼 동작을 넣는다
def btncmd():
    print("버튼이 클릭 되었다.")

btn7 = Button(root, text="동작하는 버튼", command=btncmd)
btn7.pack()
# 창이 닫히지 않게끔 해준다.
root.mainloop()