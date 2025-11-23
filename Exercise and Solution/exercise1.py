import time

t = time.strftime('%H:%M:%S')
print("The time of starting the code execution is :", t)
# hour=int (time.strftime('%H'))
hour=int(input("Enter the hourin 24 hour format: "))

if hour>0 and hour<12:
    print("Good Morning Jagjeet!")
elif hour>=12 and hour<18:
    print("Good Afternoon Jagjeet!")
elif hour>=18 and hour<21:
    print("Good Evening Jagjeet!")
else:
    print("Good Night Jagjeet!")
  