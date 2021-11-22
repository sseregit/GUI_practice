import time
import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("GUI")
root.geometry("1024x768")

# maximum 최댓값
# indeterminate : 결정되지않고 언제끝날지 모름.
progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate")
# 10 ms 마다 움직인다.
progressbar.pack()

# determinate : 확실한
progressbar1 = ttk.Progressbar(root, maximum=100, mode="determinate")
# 10 ms 마다 움직인다.
progressbar1.pack()

p_var2 = DoubleVar()
# length = progressbar의 보여지는 길이
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
# 10 ms 마다 움직인다.
progressbar2.pack()


def btnstart():
    progressbar.start(10)
    progressbar1.start(10)
    for i in range(1,101):
        time.sleep(0.01)
        # 값을 넣어준다.
        p_var2.set(i)
        # update를 해야 매번 오를때마다 UI 를 업데이트함.
        progressbar2.update()

def btnstop():
    # 작동중지
    progressbar.stop()
    progressbar1.stop()
    p_var2.set(0)


btnstart = Button(root, text="시작", command=btnstart)
btnstop = Button(root, text="중지", command=btnstop)
btnstart.pack()
btnstop.pack()


root.mainloop()

