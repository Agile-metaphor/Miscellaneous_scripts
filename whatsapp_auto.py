import pywhatkit
import time
import datetime

current_time = datetime.datetime.now()


print("Welcome to auto whatsapp!")
print("Put in the number, message and time to be sent \n make sure there are no spaces and to put the number in format: '+91xxxxxxxxxx' and time in 24-hour format eg '20:27'\n")
num = input("Number to send message to: ")
messg = input("Message: ")
print("The time now is:", current_time.hour, current_time.minute, current_time.second)
hour = int(input("Hour to send message: "))
minute = int(input("Minute to send message: "))
pywhatkit.sendwhatmsg(num,
					messg,
					hour, minute, 30, True, 5)