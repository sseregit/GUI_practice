from tkinter import *

root = Tk()
root.title("GUI")
root.geometry("1024x768")

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

# yscrollcommand 상하의 스크롤
listbox = Listbox(frame, selectmode="extended", height=10, yscrollcommand=scrollbar.set)
for i in range(1,32):
    listbox.insert(END,f"{i}일")
listbox.pack(side="left")
# listbox와 scrollbar의 맵핑을 시켜줘야함
scrollbar.config(command=listbox.yview)
root.mainloop()
