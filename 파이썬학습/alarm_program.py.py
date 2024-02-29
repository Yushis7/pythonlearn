# import tkinter as tk
# from tkinter import simpledialog
# import time
# import threading
# import winsound

# def set_alarm():
#     # 사용자에게 알람 설정 시간을 입력받음
#     alarm_time = simpledialog.askstring("알람 시간 설정", "알람 시간을 HH:MM 형식으로 입력하세요 (24시간 형식):")
    
#     try:
#         # 입력받은 시간을 파싱하여 시간 객체로 변환
#         alarm_time = time.strptime(alarm_time, "%H:%M")
        
#         # 현재 시간을 가져옴
#         current_time = time.localtime(time.time())
        
#         # 현재 날짜와 사용자가 설정한 시간을 합쳐서 알람 시간을 만듦
#         alarm_time = time.mktime((current_time.tm_year, current_time.tm_mon, current_time.tm_mday,
#                                   alarm_time.tm_hour, alarm_time.tm_min, 0, 0, 0, -1))
        
#         # 현재 시간과 알람 시간의 차이를 계산
#         time_difference = alarm_time - time.mktime(current_time)
        
#         # 알람 스레드를 시작
#         threading.Timer(time_difference, play_alarm).start()
        
#     except ValueError:
#         # 유효하지 않은 형식의 입력이 들어온 경우 예외 처리
#         tk.messagebox.showerror("에러", "올바른 형식으로 시간을 입력하세요 (HH:MM)")

# def play_alarm():
#     # 알람이 울릴 때 호출되는 함수
#     winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)
#     tk.messagebox.showinfo("알람", "알람이 울렸습니다!")

# # GUI 생성
# root = tk.Tk()
# root.title("알람 프로그램")

# # 버튼 생성
# set_alarm_button = tk.Button(root, text="알람 설정", command=set_alarm)
# set_alarm_button.pack(pady=20)

# # GUI 시작
# root.mainloop()

# import tkinter as tk
# from tkinter import simpledialog, messagebox
# import time
# import threading
# import winsound

# def set_alarm():
#     # 사용자에게 알람 설정 시간을 입력받음
#     alarm_time = simpledialog.askstring("알람 시간 설정", "알람 시간을 HH:MM 형식으로 입력하세요 (24시간 형식):")
    
#     try:
#         # 입력받은 시간을 파싱하여 시간 객체로 변환
#         alarm_time = time.strptime(alarm_time, "%H:%M")
        
#         # 현재 시간을 가져옴
#         current_time = time.localtime(time.time())
        
#         # 현재 날짜와 사용자가 설정한 시간을 합쳐서 알람 시간을 만듦
#         alarm_time = time.mktime((current_time.tm_year, current_time.tm_mon, current_time.tm_mday,
#                                   alarm_time.tm_hour, alarm_time.tm_min, 0, 0, 0, -1))
        
#         # 현재 시간과 알람 시간의 차이를 계산
#         time_difference = alarm_time - time.mktime(current_time)
        
#         # 알람 스레드를 시작
#         threading.Timer(time_difference, play_alarm).start()
        
#     except ValueError:
#         # 유효하지 않은 형식의 입력이 들어온 경우 예외 처리
#         messagebox.showerror("에러", "올바른 형식으로 시간을 입력하세요 (HH:MM)")

# def play_alarm():
#     # 알람이 울릴 때 호출되는 함수
#     winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)
#     messagebox.showinfo("알람", "알람이 울렸습니다!")

# def run_program():
#     # 프로그램 실행 버튼 클릭 시 실행되는 함수
#     messagebox.showinfo("프로그램 실행", "프로그램이 실행되었습니다!")

# # GUI 생성
# root = tk.Tk()
# root.title("알람 프로그램")

# # 알람 설정 버튼 생성
# set_alarm_button = tk.Button(root, text="알람 설정", command=set_alarm)
# set_alarm_button.pack(pady=20)

# # 프로그램 실행 버튼 생성
# run_program_button = tk.Button(root, text="프로그램 실행", command=run_program)
# run_program_button.pack(pady=20)

# # GUI 시작
# root.mainloop()


# cd C:\Users\sspea\Desktop
# pyinstaller --onefile alarm_program.py

# cd C:\Users\sspea\Downloads\CS
# pyinstaller --onefile alarm_program.py

# cd C:\Users\sspea\Desktop
# pyinstaller --onefile alarm_program.py


import tkinter as tk
from tkinter import simpledialog, messagebox
import time
import threading
import winsound

def set_alarm():
    # 사용자에게 알람 설정 시간을 입력받음
    alarm_time_str = simpledialog.askstring("알람 시간 설정", "알람 시간을 HH:MM 형식으로 입력하세요 (24시간 형식):")
    
    try:
        # 입력받은 시간을 파싱하여 시간 객체로 변환
        alarm_time = time.strptime(alarm_time_str, "%H:%M")
        
        # 현재 시간을 가져옴
        current_time = time.localtime(time.time())
        
        # 현재 날짜와 사용자가 설정한 시간을 합쳐서 알람 시간을 만듦
        alarm_time = time.mktime((current_time.tm_year, current_time.tm_mon, current_time.tm_mday,
                                  alarm_time.tm_hour, alarm_time.tm_min, 0, 0, 0, -1))
        
        # 현재 시간과 알람 시간의 차이를 계산
        time_difference = alarm_time - time.mktime(current_time)
        
        # 알람 스레드를 시작
        threading.Timer(time_difference, play_alarm).start()
        
        # 남은 시간 업데이트를 위한 함수 호출
        update_remaining_time(time_difference)
        
    except ValueError:
        # 유효하지 않은 형식의 입력이 들어온 경우 예외 처리
        messagebox.showerror("에러", "올바른 형식으로 시간을 입력하세요 (HH:MM)")

def play_alarm():
    # 알람이 울릴 때 호출되는 함수
    winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)
    messagebox.showinfo("알람", "알람이 울렸습니다!")

def update_remaining_time(time_difference):
    # 남은 시간을 초 단위로 표시하는 함수
    remaining_seconds = int(time_difference)
    remaining_hours, remaining_seconds = divmod(remaining_seconds, 3600)
    remaining_minutes, remaining_seconds = divmod(remaining_seconds, 60)
    
    remaining_time_str = f"남은 시간: {remaining_hours:02d}:{remaining_minutes:02d}:{remaining_seconds:02d}"
    
    # 라벨 업데이트
    remaining_time_label.config(text=remaining_time_str)
    
    # 1초 후에 다시 호출 (재귀 호출)
    if remaining_seconds > 0:
        root.after(1000, update_remaining_time, time_difference - 1)

def run_program():
    # 프로그램 실행 버튼 클릭 시 실행되는 함수
    messagebox.showinfo("프로그램 실행", "프로그램이 실행되었습니다!")

# GUI 생성
root = tk.Tk()
root.title("알람 프로그램")

# 알람 설정 버튼 생성
set_alarm_button = tk.Button(root, text="알람 설정", command=set_alarm)
set_alarm_button.pack(pady=20)

# 프로그램 실행 버튼 생성
run_program_button = tk.Button(root, text="프로그램 실행", command=run_program)
run_program_button.pack(pady=20)

# 남은 시간을 표시할 라벨 생성
remaining_time_label = tk.Label(root, text="", font=("Helvetica", 16))
remaining_time_label.pack(pady=20)

# GUI 시작
root.mainloop()