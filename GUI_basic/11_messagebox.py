import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title("GUI")
root.geometry("1024x768")

# 기차 예메 시스템 
# show box
def info():
    # 첫번째는 title 두번째가 메시지내용
    msgbox.showinfo("알림","정상적인 예매 완료")
def warn():
    msgbox.showwarning("경고","해당 좌석 매진")
def error():
    msgbox.showerror("에러","결제 오류 발생")
Button(root, command=info, text="알림").pack()
Button(root, command=warn, text="경고").pack()
Button(root, command=error, text="에러").pack()

# ask box
def okcancel():
    # ask 요청한다.
    msgbox.askokcancel("확인 / 취소","유아 동반석 예매?")
def retrycancel():
    # ask 요청한다.
    msgbox.askretrycancel("재시도 / 취소","일시적 오류 다시시도하실?")
def yesno():
    # ask 요청한다.
    msgbox.askyesno("예 / 아니요","예매 하시겟습니까?")
def yesnocancel():
    # ask 요청한다.
    # title없이 처리하는법.
    response = msgbox.askyesnocancel(title=None,message="예매 내역 저장안됨 \n 다시하실?")
    # 예 True 1 아니요 False 0 취소 None 
    if response == 1:
        print("예")
    elif response == 0:
        print("아니요")
    else:
        print("취소")
Button(root, command=okcancel, text="확인취소").pack()
Button(root, command=retrycancel, text="재시도").pack()
Button(root, command=yesno, text="예 아니요").pack()
Button(root, command=yesnocancel, text="예 아니요 취소").pack()

root.mainloop()
