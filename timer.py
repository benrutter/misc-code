import time
import datetime
import os

time_isnt_number = True

while time_isnt_number:
    wait_time = input("time in minutes:")
    try:
        wait_time = float(wait_time)*60
        time_isnt_number = False
    except:
        pass

keep_on = True
start_time = datetime.datetime.now()

def timer(diff,total):
    through = diff/total
    timer_string = ['[']
    for i in range(30):
        if i/30 > through:
            timer_string.append(' ')
        else:
            timer_string.append('*')
    timer_string.append(']')
    return ''.join(timer_string)

while keep_on:
    diff = (datetime.datetime.now() - start_time).total_seconds()
    seconds_left = int(round(wait_time - diff, 0))
    if seconds_left <= 0:
        keep_on = False
    minutes_left = int((seconds_left - (seconds_left % 60)) / 60)
    seconds_left = seconds_left % 60
    print("{} {}:{} remaining".format(timer(diff,wait_time),minutes_left, seconds_left), end='\r')
    time.sleep(1)


print("\n\atimes up!")
