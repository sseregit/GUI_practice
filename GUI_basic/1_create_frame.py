import tkinter

root = tkinter.Tk()
# title
root.title("Jang GUI")
# 가로 * 세로 + x의 좌표 + y의 좌표
root.geometry("640x480+600+200")
# x(너비), y(높이) (창 크기 변경 불가)
root.resizable(False,False)
# 창이 닫히지 않게끔 해준다.
root.mainloop()