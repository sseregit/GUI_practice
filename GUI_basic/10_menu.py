from tkinter import *

root = Tk()
root.title("GUI")
root.geometry("1024x768")

def create_new_file():
    print("새 파일을 만듭니다.")

# 메인 메뉴
menu = Menu(root)

# File Menu
# 메인 메뉴 안에 메뉴 목록을 넣는다.
menu_file = Menu(menu, tearoff=0)
# 메뉴의 종류
menu_file.add_command(label="새파일", command=create_new_file)
menu_file.add_command(label="새 창")
# 메뉴 구분자 <hr />
menu_file.add_separator()
menu_file.add_command(label="파일 열기...")
menu_file.add_separator()
# state="disable" 비활성화
menu_file.add_command(label="모두 저장", state="disable")
menu_file.add_separator()
# root.quit 종료한다.
menu_file.add_command(label="종료", command=root.quit)
# 메인 메뉴에 메뉴 목록을 추가한다.
menu.add_cascade(label="파일", menu=menu_file)

# Edit Menu
menu.add_cascade(label="편집")

# Menu에 Radio button 추가
menu_lang = Menu(menu, tearoff=0)
menu_lang.add_radiobutton(label="Python")
menu_lang.add_radiobutton(label="Java")
menu_lang.add_radiobutton(label="C++")
menu.add_cascade(label="언어", menu=menu_lang)

# Menu에 CheckBox 추가
menu_view = Menu(menu, tearoff=0)
menu_view.add_checkbutton(label="Show Minimap")
menu.add_cascade(label="보기", menu=menu_view)



# root.config로 메인 메뉴를 추가한다.
root.config(menu=menu)
root.mainloop()
