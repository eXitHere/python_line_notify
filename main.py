import time
import psutil
import json
import sys
from termcolor import colored
from python_line_notify import send_msg
import datetime

try:
     f = open('settings.json',)
     setting = json.load(f)
     msg = setting['device_name'] + ': ' + datetime.datetime.now().strftime('%y %b,%a %I:%M %p') + ' is online.' +'\n'
     msg += 'CPU: ' + str(psutil.cpu_percent()) + '%\n' + 'RAM: ' + str(psutil.virtual_memory()[2]) + '%'
     print(msg)
     if send_msg(setting['token'], msg) == 200:
          print("Send message success!")
     else:
          print("Send message fail")
except:
     print("setting.json not fonud.\npress 1: create new setting\npress 2: exit")
     created_setting = False
     while not created_setting:
          command = input("Enter command: ")
          created_setting = False
          if command == '1':
               token = input("Enter token: ")
               device_name = input("Enter device name: ")
               print("Your token:", colored(token, "green"), "and device name:", colored(device_name, "green"))
               while True:
                    confirm = input("Do you want to save the changes ('yes', 'no'): ")
                    if confirm.lower() == 'yes' or confirm.lower() == 'no':
                         if confirm.lower() == 'yes':
                              try:
                                   with open("settings.json", "w") as outfile: 
                                        json.dump({
                                             "token": token,
                                             "device_name": device_name
                                        }, outfile)
                                   print("Saved file!")
                                   created_setting = True
                              except:
                                   print("Can't save file, exit...")
                                   sys.exit(0)

                         else:
                              print(colored("Please enter you token and device name again...", "red"), "\npress 1: create new setting\npress 2: exit")
                         break
          elif command == '2':
               sys.exit(0)
