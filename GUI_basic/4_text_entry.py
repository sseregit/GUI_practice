from tkinter import *

root = Tk()
root.title("jang")
root.geometry("1024x768")

# Text를 만든다.
txt = Text(root, width=30, height=5)
txt.pack()
# Text에 값을 넣어준다
txt.insert(END, "글자를 입력하세요")

# entry는 한줄의 값
e = Entry(root, width=30)
e.pack()
# entry에 값을 넣어준다.
e.insert(0, "한 줄만 입력해요")
def btncmd():
    # get = Text, entrty값을 가져온다
    # 1 첫번째 줄, 0 Column 기준으로 0번째부터 END 끝까지 가져와라.
    print(txt.get("1.0", END))
    print(e.get())
    # 내용삭제
    txt.delete("1.0", END)
    e.delete(0, END)

btn = Button(root, text="클릭", command=btncmd)
btn.pack()
root.mainloop()
