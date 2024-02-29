#%%
import time

def alarm():
    print("30분 경과 알림입니다.")

now = time.time()
next_alarm = now + 30 * 60

while True:
    now = time.time()
    if now >= next_alarm:
        alarm()
        next_alarm = now + 30 * 60
        





