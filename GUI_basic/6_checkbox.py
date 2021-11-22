from tkinter import *

root = Tk()
root.title("GUI")
root.geometry("1024x768")

# chkvar 에 int형으로 값을 저장한다.
chkvar = IntVar()
# variable이 필요함. Check 했는지 안했는지에 대한 값을 알아야함.
chkbox = Checkbutton(root, text="오늘 하루 보지 않기", variable=chkvar)
# 자동 선택처리.
chkbox.select()
# 선택 해제 처리.
chkbox.deselect()
chkbox.pack()

chkvar2 = IntVar()
# variable은 같은 변수를 공유하면 안됨.
chkbox2 = Checkbutton(root, text="일주일동안 보지 않기", variable=chkvar2)
chkbox2.pack()

def btncmd():
    print(chkvar.get())
    print(chkvar2.get())    

btn = Button(root, text="버튼", command=btncmd)
btn.pack()


root.mainloop()
