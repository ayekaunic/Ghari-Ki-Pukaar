import time
from playsound import playsound
import random
import datetime

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"


def print_time_left(seconds_to_print):
    remaining_time = seconds_to_print
    if remaining_time == 0:
        print(f"{CLEAR_AND_RETURN}00:00:00")
    else:
        hours = remaining_time // 3600
        minutes = (remaining_time % 3600) // 60
        seconds = remaining_time % 60
        print(f"{CLEAR_AND_RETURN}{hours:02d}:{minutes:02d}:{seconds:02d}")
        remaining_time = remaining_time - 1
        time.sleep(1)
        print_time_left(remaining_time)


def sound_random_alarm():
    random_alarm = random.choice(['alarm1.mp3', 'alarm2.mp3', 'alarm3.mp3', 'alarm4.mp3', 'alarm5.mp3'])
    playsound(random_alarm)
    print(CLEAR)


def timer():
    hours = int(input('hours: '))
    minutes = int(input('minutes: '))
    seconds = int(input('seconds: '))
    total_in_seconds = int((hours * 3600) + (minutes * 60) + seconds)
    print(f"{CLEAR}")
    print_time_left(total_in_seconds)
    sound_random_alarm()


def alarm():
    hours = int(input('hour (0-23): '))
    minutes = int(input('minutes (0-59): '))
    go_off_time = datetime.datetime(year=datetime.datetime.now().year, month=datetime.datetime.now().month, day=datetime.datetime.now().day, hour=hours, minute=minutes)
    seconds_left = (go_off_time-datetime.datetime.now()).seconds
    print(f"{CLEAR}")
    print_time_left(seconds_left)
    sound_random_alarm()


print(f"{CLEAR}")
print(f"{CLEAR_AND_RETURN}")

choice = int(input('enter (1) for timer or (2) for alarm: '))
if choice == 1:
    timer()
elif choice == 2:
    alarm()
else:
    print(f"{CLEAR}")
    print(f"{CLEAR_AND_RETURN}")
    print('invalid choice\n')
