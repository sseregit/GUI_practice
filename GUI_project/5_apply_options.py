import os
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from tkinter import *
from tkinter import filedialog
from PIL import Image


root = Tk()
root.title("GUI")

# 파일 프레임 (파일 추가, 선택 삭제)
file_frame = Frame(root)
file_frame.pack(fill="x", padx=5, pady=5)

# 파일 추가
def add_file():
    # 파일 다이얼 로그는 tkinter에서 제공
    # filenames 복수개의 파일을 선택가능하게해준다.
    # filetypes (보여지는 파일 , 실제 파일확장자)
    # initialdir 최초로 보여지는 directory
    files = filedialog.askopenfilenames(title="이미지 파일을 선택하세요.", \
         filetypes=(("PNG 파일","*.png"),("모든파일","*.*")), \
         # r 탈출문자등 상관없이 그대로 사용하겟다는 의미.
         initialdir=r"D:\GUI_practice\image")
    for file in files:
        list_file.insert(END,file)

# 선택 삭제
def del_file():
    # curselection 선택한값의 인덱스를 반환한다.
    select_file = list_file.curselection()
    # index가 변하기 때문에 뒤에서부터 지워야한다.
    for index in select_file[-1::-1]:
        list_file.delete(index)

# 저장 경로 (폴더)
def browse_dest_path():
    folder_selected = filedialog.askdirectory()
    # 입력하지 않음.
    if folder_selected == "":
        return    
    txt_dest_path.delete(0,END)    
    txt_dest_path.insert(0, folder_selected)

# 이미지 통합 작업
def merge_images():
    try:
        # 각 옵션들 값을 확인한다.
        # 가로넓이
        img_width = cmb_widths.get()
        if img_width == "원본유지":
            img_width = -1
        else:
            img_width = int(img_width)

        # 간격
        img_space = cmb_space.get()
        if img_space == "좁게":
            img_space = 30
        elif img_space == "보통":
            img_space = 60
        elif img_space == "넓게":
            img_space = 90
        else:
            img_space = 0       

        # 포맷
        img_format = cmb_format.get().lower()

        # 이미지를 가져와 열어본다.
        images = [Image.open(x) for x in list_file.get(0,END)]
        # 이미지 사이즈 리스트에 넣어서 하나씩 처리
        image_sizes = [] 
        if img_width > -1:
            image_sizes = [(int(img_width),int((img_width*x.size[1])/x.size[0])) for x in images]
        else:
            image_sizes = [(x.size[0],x.size[1]) for x in images]

        # 계산식
        #  100 * 60 이미지가 있음 => width를 80 으로 줄이면 height 는?    
        # (원본 width : 원본 height) = (변경 width : 변경 height)
        # 원본 width * 변경 height == 원본 height * 변경 width 여야한다.
    
        # size 0 : width, 1: height
        widths, heights =  zip(*(image_sizes))
        
        # 가로로 제일큰것과 하나로 합칠것이니 heights를 모두 더해야한다.
        max_width, total_height = max(widths),sum(heights)
        # 이미지 간격 옵션 적용
        if img_space > 0:
            total_height += (img_space * (len(images) -1))

        # 모든 이미지를 합칠 도화지
        # 종류 , 사이즈 , 색상    
        result_img = Image.new("RGB",(max_width,total_height),(255,255,255))
        # y_offset 이미지를 붙이고나서 다음이아니라 그 아래로 내려가게끔 처리해주기위함.
        y_offset = 0    

        for idx, img in enumerate(images):
            # width가 원본유지가 아닐 때에는 이미지 크기 조정
            if img_width > -1:
                # resize 변경된 사이즈로 변경해준다.
                img = img.resize(image_sizes[idx])
            result_img.paste(img,(0, y_offset))
            # 이미지의 높이값을 더한다. 빈공간까지 추가
            y_offset += (img.size[1] + img_space)        
            # precent 계산
            progress = ((idx + 1 / len(images)) * 100)
            p_var.set(progress)
            progress_bar.update()

        # 두가지 경로를 합친다. 저장경로 + 저장될 파일 명
        dest_path = os.path.join(txt_dest_path.get(),"GUI_photo.{}".format(img_format))    
        # 경로에 저장한다.
        result_img.save(dest_path)
        msgbox.showinfo("알림","작업이 완료되었습니다.")
    except Exception as e:
        msgbox.showerror("에러",e)
        
# 시작
def start():
    # 파일 목록 확인
    if list_file.size() == 0:
        return msgbox.showwarning("경고", "이미지 파일을 추가하세요")
    # 저장 경로 확인
    if len(txt_dest_path.get()) == 0:
        return msgbox.showwarning("경고", "저장 경로를 선택하세요")
    
    # 이미지 통합 작업
    merge_images()
    

        

btn_add_file = Button(file_frame, text="파일 추가", padx=5, pady=5, width=12, command=add_file)
btn_del_file = Button(file_frame, text="선택 삭제", padx=5, pady=5, width=12, command=del_file)
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

btn_dest_path = Button(path_frame, text="찾아보기", width=10, command=browse_dest_path)
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

btn_start = Button(run_frame,text="시작", padx=5, pady=5, width=12, command=start)
btn_close = Button(run_frame,text="닫기",padx=5, pady=5, width=12, command=root.quit)
btn_close.pack(side="right")
btn_start.pack(side="right", padx=5)

root.resizable(False, False)
root.mainloop()