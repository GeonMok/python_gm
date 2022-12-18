import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from tkinter import *


#학점 변수 생성
demanded_total = 130    # 컴퓨터학과 기준
demanded_major_essential = 18
demanded_major_selective = 54 # 심화전공 기준

current_total = 0
current_major_essential = 0
current_major_selective = 0 
score = 0

root = Tk()
root.title("GeonMok GUI") #창 제목 설정
root.geometry("640x480+300+300") #창 크기 설정(가로*세로)+ x좌표 + y좌표
root.resizable(True, True)

#학기 프레임
frame_semester = LabelFrame(root, text = "학기 선택")
frame_semester.pack(padx = 7, pady= 7, fill="x")

# 학기 선택
lbl_semester = Label(frame_semester, text = "과목 수강 시기를 선택하세요", width = 30)
lbl_semester.pack(side = "left",padx = 6, pady = 6)

opt_semester = ["1-1","1-2","2-1","2-2","3-1","3-2","4-1","4-2","초과 학기"]
cmb_semester = ttk.Combobox(frame_semester, state = "readonly", values = opt_semester, width = 10)
cmb_semester.current(0)
cmb_semester.pack(side = "left", padx = 6, pady= 6)

#옵션 프레임
frame_option = LabelFrame(root, text = "옵션")
frame_option.pack(padx = 5, pady= 5, ipady=5) 

# 1. 과목명 (텍스트)
course = Text(frame_option, width = 10, height=1) #텍스트 위젯
course.pack(side = "left", padx = 6, pady= 6)
course.insert(END, "과목명")

# 2. 전공 여부 옵션
lbl_major = Label(frame_option, text = "전공 여부", width = 9)
lbl_major.pack(side = "left", padx = 6, pady= 6)

opt_major = ["전공필수", "전공선택", "기타"]
cmb_major = ttk.Combobox(frame_option, state = "readonly", values = opt_major, width = 10)
cmb_major.current(0)
cmb_major.pack(side = "left", padx = 6, pady= 6)

# 3. 학점 옵션 
lbl_credit = Label(frame_option, text = "학점", width = 9)
lbl_credit.pack(side = "left", padx = 6, pady= 6)

opt_credit = ["1", "2", "3"]
cmb_credit = ttk.Combobox(frame_option, state = "readonly", values = opt_credit, width = 10)
cmb_credit.current(0)
cmb_credit.pack(side = "left", padx = 6, pady= 6)

# 4. 성적 옵션 
lbl_grade = Label(frame_option, text = "성적", width = 9)
lbl_grade.pack(side = "left", padx = 6, pady= 6)

score_per_credit = [4.5,4.0,3.5,3.0,2.5,2.0,1.5,1.0]
opt_grade = ["A+", "A", "B+", "B", "C+", "C", "D+", "D"] #Pass Fail?
grade_dict = dict(zip(opt_grade, score_per_credit))
cmb_grade = ttk.Combobox(frame_option, state = "readonly", values = opt_grade, width = 10)
cmb_grade.current(0)
cmb_grade.pack(side = "left", padx = 6, pady= 6)

#진행 상황 프로그레스 바
frame_major_essential = LabelFrame(root, text = "진행 상황(전공 필수)")
frame_major_essential.pack(fill="x", padx = 5, pady= 5, ipady=5)

p_var_M = DoubleVar()
pbar_M = ttk.Progressbar(frame_major_essential, maximum = demanded_major_essential, variable=p_var_M)
pbar_M.pack(fill="x", padx = 5, pady= 5)


frame_major_selective = LabelFrame(root, text = "진행 상황(전공 선택)")
frame_major_selective.pack(fill="x", padx = 5, pady= 5, ipady=5)

p_var_m = DoubleVar()
pbar_m = ttk.Progressbar(frame_major_selective, maximum = demanded_major_selective, variable=p_var_m)
pbar_m.pack(fill="x", padx = 5, pady= 5)


frame_total = LabelFrame(root, text = "진행 상황(Total)")
frame_total.pack(fill="x", padx = 5, pady= 5, ipady=5)

p_var_T = DoubleVar()
pbar_T = ttk.Progressbar(frame_total, maximum = demanded_total, variable=p_var_T)
pbar_T.pack(fill="x", padx = 5, pady= 5)

#필요 함수
def addcmd():
    global current_major_essential
    global current_major_selective
    global current_total
    global score

    major_info  = cmb_major.get()
    idx = opt_major.index(major_info)
    print(cmb_semester.get(), course.get(1.0, END)) # 학기 내 중복 과목은 없다고 가정
    credit_taken = int(cmb_credit.get())
    if idx == 0 : # 전공필수
        current_major_essential += credit_taken
    if idx == 1 : # 전공선택
        current_major_selective += credit_taken
    current_total += credit_taken
    score += credit_taken*grade_dict[cmb_grade.get()] # score value like 4.5, 4.0 ... 

def calcmd():
    global current_major_essential
    global current_major_selective
    global current_total
    global score

    p_var_M.set(current_major_essential)
    p_var_m.set(current_major_selective)
    p_var_T.set(current_total)

    pbar_T.update()
    pbar_m.update()
    pbar_M.update()

    print("Credit Score(total): %.2f" %(score/current_total))


# 실행 프레임
frame_run = Frame(root)
frame_run.pack(fill = "x", padx = 5, pady= 5)

btn_close = Button(frame_run, padx = 5, pady = 5, text = "닫기", width = 12, command = root.quit)
btn_close.pack(side = "right", padx = 5, pady= 5)
btn_start = Button(frame_run, padx = 5, pady = 5, text = "계산", width = 12, command=calcmd)
btn_start.pack(side = "right", padx = 5, pady= 5)
btn_start = Button(frame_run, padx = 5, pady = 5, text = "추가", width = 12, command=addcmd)
btn_start.pack(side = "right", padx = 5, pady= 5)


root.mainloop() #loop를 통해서 창이 닫히지 않도록 함.
