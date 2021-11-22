import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("GUI")
root.geometry("1024x768")

values = [str(i) + "일" for i in range(1,32)]
# values = list를 보내준다. height 목록이 보이는 수
combobox = ttk.Combobox(root, height=5, values=values)
combobox.pack()
# 최초 목록의 제목
combobox.set("카드 결제일")

# state로 옵션을 지정할수있다.
combobox1 = ttk.Combobox(root, height=10, values=values, state="readonly")
# 0번째 인덱스값 선택
combobox1.current(0)
combobox1.pack()

def btncmd():
    # 선택된 값 표시
    print(combobox.get())
    print(combobox1.get())

btn = Button(root, text="선택", command=btncmd)
btn.pack()


root.mainloop()

