# Ghari Ki Pukaar
The code is a Python script for a timer/alarm program. It imports necessary libraries, including **time**, **playsound**, **random**, and **datetime**. It defines several functions such as **print_time_left**, **sound_random_alarm**, **timer**, and **alarm**, and uses them to implement the timer and alarm functionalities.

**print_time_left** is a recursive function that prints the remaining time in hours, minutes, and seconds format. It takes the total remaining seconds as input and recursively calls itself with one second less, until the remaining time becomes 0.

**sound_random_alarm** plays a randomly selected alarm sound from a list of predefined sound files.

**timer** takes user input for hours, minutes, and seconds, converts the time to seconds, and calls **print_time_left** and **sound_random_alarm** to display the remaining time and play an alarm sound when the timer ends.

**alarm** takes user input for the desired alarm time, calculates the remaining time in seconds, and calls **print_time_left** and **sound_random_alarm** to display the remaining time and play an alarm sound when the alarm goes off.

The main part of the code asks the user to choose between timer and alarm functionality and calls the corresponding function. If the user enters an invalid choice, it displays an error message.
