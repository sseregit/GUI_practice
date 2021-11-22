from tkinter import *

root = Tk()
root.title("GUI")
root.geometry("1024x768")
# selectmode 옵션 / height의 적힌 숫자만큼만 표기한다. 값은다 추가됨.
list_box = Listbox(root, selectmode="extended", height=0)
# index를 조절할수있음.
list_box.insert(0,"사과")
list_box.insert(1,"딸기")
list_box.insert(2,"바나나")
# END로 맨마지막에추가할수있음.
list_box.insert(END,"수박")
list_box.insert(END,"포도")
list_box.pack()

def btncmd():
    # 첫번째 arg는 index / 맨뒤에 항목을 삭제한다.
    list_box.delete(END)
    # 갯수확인
    print(list_box.size())

    # 항목 확인 시작 index ~ 끝 index
    print(list_box.get(0, 2))

    # 선택된 항목 확인하기 index값을 리턴함.
    print(list_box.curselection())

btn = Button(root, text="버튼", command=btncmd)
btn.pack()


root.mainloop()