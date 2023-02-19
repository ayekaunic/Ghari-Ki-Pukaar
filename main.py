import time
from playsound import playsound
import random

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


print(f"{CLEAR}")
print(f"{CLEAR_AND_RETURN}")
timer()
