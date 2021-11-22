from tkinter import *

root = Tk()
root.title("JANG")
root.geometry("1024x768")

label1 = Label(root, text="안녕하세요")
label1.pack()

photo = PhotoImage(file="./image/img.png")
label2 = Label(root, image=photo)
label2.pack()

# btn을 눌렀을때 label이 변경됨.
def change():
    label1.config(text="또 만나요")   
    global photo2 
    photo2 = PhotoImage(file="./image/star.png")
    label2.config(image=photo2)

btn = Button(root, text="버튼", command=change)
btn.pack()

root.mainloop()