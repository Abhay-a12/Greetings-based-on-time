import time

name = input("Enter your Name : ")

timestamp_hr = int(time.strftime('%H'))

if (timestamp_hr < 12 ):
    print("Good Morning", name, "!")
elif (timestamp_hr >= 12 and timestamp_hr < 18):
    print("Good Afternoon", name, "!")
else :
    print("Good Evening", name,"!")