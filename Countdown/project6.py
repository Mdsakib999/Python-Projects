#Countdown / Timer project in Python...

import time

def countDown(T):
    while T:

        min, sec = divmod(T, 60)
        
        timer = "{:02d}:{:02d}".format(min, sec)

        print(timer, end="\r")

        time.sleep(1)
        T -= 1


#ask user to enter second

T = input("Enter the time in second: ")

countDown(int(T))

print("Time off!!!")