import os
from tkinter import *

root = Tk()
root.title("제목 없음 - Windows 메모장")
root.geometry("1024x768")

frame = Frame(root, relief="solid", bd=0)
scrollbar = Scrollbar(frame)
text = Text(frame,yscrollcommand=scrollbar.set)
filename = "mynote.txt"

def open_file():
    # 파일이 존재하는지 확인
    if os.path.isfile(filename):
        with open(filename,"r",encoding="UTF-8") as open_file:
            # 초기화
            text.delete("1.0", END)
            text.insert(END,open_file.read())

def save_file():
    save_text = text.get("1.0",END)    
    if save_text:
        with open("mynote.txt","w") as file:
            file.write(save_text)        

# 메뉴바
menu = Menu(root)
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="열기", command=open_file)
menu_file.add_command(label="저장", command=save_file)
menu_file.add_separator()
menu_file.add_command(label="끝내기", command=root.quit)


menu.add_cascade(label="파일",menu=menu_file)
menu.add_cascade(label="편집")
menu.add_cascade(label="서식")
menu.add_cascade(label="보기")
menu.add_cascade(label="도움말")

# 텍스트 & 스크롤바 
scrollbar.pack(side="right",fill="y")
text.pack(side="left",fill="both",expand=True)
scrollbar.config(command=text.yview)
root.config(menu=menu)
frame.pack(fill="both",expand=True)
root.mainloop()