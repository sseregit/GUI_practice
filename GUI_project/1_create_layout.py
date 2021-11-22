import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("GUI")

# 파일 프레임 (파일 추가, 선택 삭제)
file_frame = Frame(root)
file_frame.pack(fill="x", padx=5, pady=5)

btn_add_file = Button(file_frame, text="파일 추가", padx=5, pady=5, width=12)
btn_del_file = Button(file_frame, text="선택 삭제", padx=5, pady=5, width=12)
btn_add_file.pack(side="left")
btn_del_file.pack(side="right")

# 리스트 프레임
list_frame = Frame(root)
list_frame.pack(fill="x", padx=5, pady=5)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

list_file = Listbox(list_frame, selectmode="extended", height=15, yscrollcommand=scrollbar.set)
list_file.pack(side="left", fill="both", expand=True)
scrollbar.config(command=list_file.yview)

# 저장경로 프레임
path_frame = LabelFrame(root, text="저장경로")
path_frame.pack(fill="x", padx=5, pady=5, ipady=5)

txt_dest_path = Entry(path_frame)
# ipady 높이변경
txt_dest_path.pack(side="left", fill="x", expand=True, ipady=4, padx=5, pady=5)

btn_dest_path = Button(path_frame, text="찾아보기", width=10)
btn_dest_path.pack(side="right", padx=5, pady=5)

# 옵션 프레임
option_frame = LabelFrame(text="옵션")
option_frame.pack(fill="x", padx=5, pady=5, ipady=5)

# 가로넓이
# 레이블
lbl_widths = Label(option_frame, text="가로넓이", width=8)
lbl_widths.pack(side="left", padx=5, pady=5)
# 콤보
opt_widths = ["원본유지","1024","800","640"]
cmb_widths = ttk.Combobox(option_frame, state="readonly", values=opt_widths, width=10)
cmb_widths.current(0)
cmb_widths.pack(side="left", padx=5, pady=5)

# 간격
# 레이블
lbl_space = Label(option_frame, text="간격")
lbl_space.pack(side="left", padx=5, pady=5)
# 콤보
opt_space = ["없음","좁게","보통","넓게"]
cmb_space = ttk.Combobox(option_frame, state="readonly", values=opt_space)
cmb_space.current(0)
cmb_space.pack(side="left", padx=5, pady=5)

# 포맷
# 레이블
lbl_format = Label(option_frame, text="포맷")
lbl_format.pack(side="left", padx=5, pady=5)
# 콤보
opt_format = ("PNG","JPG","BMP")
cmb_format = ttk.Combobox(option_frame, state="readonly", values=opt_format)
cmb_format.current(0)
cmb_format.pack(side="left", padx=5, pady=5)

# 진행상황
progress_frame = LabelFrame(root, text="진행상황")
progress_frame.pack(fill="x", padx=5, pady=5, ipady=5)

p_var = DoubleVar()
progress_bar = ttk.Progressbar(progress_frame, maximum=100, variable=p_var)
progress_bar.pack(fill="x", padx=5, pady=5)

# 실행 프레임
run_frame = Frame(root)
run_frame.pack(fill="x", padx=5, pady=5)

btn_start = Button(run_frame,text="시작", padx=5, pady=5, width=12)
btn_close = Button(run_frame,text="닫기",padx=5, pady=5, width=12, command=root.quit)
btn_close.pack(side="right")
btn_start.pack(side="right", padx=5)

root.resizable(False, False)
root.mainloop()