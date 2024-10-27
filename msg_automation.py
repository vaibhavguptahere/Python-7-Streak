""" Whatsapp Automating Message"""


# pip install pywhatkit
# Library used- pywhatkit

import pywhatkit as pyw

# Taking user input for phone number, message, and time
phone_no = input("Enter Phone No. (with country code): ")
type_msg = input("Enter the message you want to send: ")
time_hour = int(input("Enter the hour (24-hour format): "))
time_minute = int(input("Enter the minutes : "))

# Sending the WhatsApp message
pyw.sendwhatmsg(phone_no, type_msg, time_hour, time_minute)
