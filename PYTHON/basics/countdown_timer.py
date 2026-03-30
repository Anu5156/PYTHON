"""---COUNTDOWN---"""
# import time
# my_time=int(input("Enter the time in seconds for countdown: "))
# for x in range(0, my_time):
#     print(x)
#     time.sleep(1) # pauses for 1 second
# print("Time's Up!")

# for reversed countdown
# for x in reversed(range(0, my_time)):
#     print(x)
#     time.sleep(1) # pauses for 1 second
# print("Time's Up!")

# for x in range(my_time, 0, -1):
#     seconds = x % 60
#     minutes = int(x / 60) % 60
#     hours = int(x / 3600)
#     print(f"{hours:02}:{minutes:02}:{seconds:02}")
#     time.sleep(1) # pauses for 1 second
# print("Time's Up!")

"""---TRAFFIC LIGHT"""
import time
from itertools import cycle
lights=[
    ('Green',2),
    ('Yellow',0.5),
    ('Red',2)

]

colors=cycle(lights)
while True:
    c,s=next(colors)
    print(c)
    time.sleep(s)

