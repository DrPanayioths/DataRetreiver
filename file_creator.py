import os
import sys
import time
os.system('color a')


creator_code = input("Input Your Name: ")
use_supabase = input("Do You Want To Use Supabase System, y or n: ")
if (use_supabase == "y"):
    Supabase_url = input("Input Your Supabase URL, Example:(https://xxxxxx.supabase.co): ")
    Supabase_key = input("Input Your Supabase KEY: ")
    Supabase_Table = input("Input The Name Of The Database Table You Want The Data To Be Saved: ")
use_discord = input("Do You Want To Use Discord System, y or n: ")
if (use_discord == "y"):
    Discord_url = input("Input Webhook URL, (If You Dont Know: https://rb.gy/ap8wtw): ")

if use_supabase == "" and use_discord == "":
    print("You Doesn't Selected Any System")
    time.sleep(1)
    sys.exit()
if use_supabase == "y":
    
    content = """
import time
import platform
import random
import psutil
from supabase import create_client, Client
from datetime import datetime
import ctypes
import string
import secrets
import os
import ping3
import requests

url: str = "{Supabase_url}"
key: str = "{Supabase_key}"

supabase: Client = create_client(url, key)
os.system('color a')
print("="*83)
print("(Computer) Data Sender Provided By DrPanayioths       Supports: Database / Discord")
print("="*83)

data_consent = input("By Writing Accept Or A You Accept To The Collection Of Your Computer Data And Transfer To The Database Of {creator_code}: ")
print("")

def get_country():
    try:
        response = requests.get('http://ip-api.com/json/')
        data = response.json()
        country = data.get('country')
        isp = data.get('isp')
        return country , isp
    except Exception as e:
        return None

def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

random_number = random.randrange(0,99999)
platdata = platform.uname()
ram = psutil.virtual_memory()
random_str = str(random_number)
password_final = secrets.choice(string.ascii_uppercase) + secrets.choice(string.ascii_lowercase) + secrets.choice(string.ascii_letters) + str(random.randrange(0,9999))
country , isp = get_country()
date_now = datetime.now().strftime('%d-%m-%Y ')
time_now = datetime.now().strftime('%H:%M:%S')
ping_time = round(ping3.ping("google.com") * 1000, 2)




# Main Coding System
if data_consent.upper() == "ACCEPT" or data_consent.upper() == "A":
    try:
        # Database Sender
        count = supabase.table('{Supabase_Table}') \
.insert({
    "id": random_number,
    "security_code": password_final,
    "OperatingSYS": platdata.system,
    "DeviceName": platdata.node,
    "WindowsVersion": platdata.release,
    "CPU_DATA": platdata.processor,
    "Ram_Total": get_size(ram.total),
    "Ram_Used": get_size(ram.used),
    "Country": country,
    "ISP": isp,
    "Date": date_now,
    "Time": time_now,
    "Ping": ping_time
})            .execute()
        print("="*40, "Provide Those To The Helper", "="*40)
        print("Database Entry Code: " + random_str)
        print("Data Access Key: " + password_final)
        print("") 
        
    except Exception as e:
        ctypes.windll.user32.MessageBoxW(0, "Data Transfer Status: Unsuccessful Transfer", "DRP Data Transferer", 0x30)
else:
    print("You Decline The Transfer, Program Will Close In 5")
    time.sleep(1)
    print("Program Close In 4")
    time.sleep(1)
    print("Program Close In 3")
    time.sleep(1)
    print("Program Close In 2")
    time.sleep(1)
    print("Program Close In 1")
    time.sleep(1)
    exit()






    
    
    
    
    
    
    
    
    
    
    
    
    
"""
    file_name = 'data_receiver.py'
    with open(file_name, 'w') as file:
        file.write(content)
    print(f'File {file_name} has been created.')       

if use_discord == "y":
    content = """
import time
import platform
import random
import psutil
from datetime import datetime
import ctypes
import string
import secrets
import os
import ping3
import requests

url: str = "{Supabase_url}"
key: str = "{Supabase_key}"

supabase: Client = create_client(url, key)
os.system('color a')
print("="*83)
print("(Computer) Data Sender Provided By DrPanayioths       Supports: Database / Discord")
print("="*83)

data_consent = input("By Writing Accept Or A You Accept To The Collection Of Your Computer Data And Transfer To The Database Of {creator_code}: ")
print("")

def get_country():
    try:
        response = requests.get('http://ip-api.com/json/')
        data = response.json()
        country = data.get('country')
        isp = data.get('isp')
        return country , isp
    except Exception as e:
        return None

def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

random_number = random.randrange(0,99999)
platdata = platform.uname()
ram = psutil.virtual_memory()
random_str = str(random_number)
password_final = secrets.choice(string.ascii_uppercase) + secrets.choice(string.ascii_lowercase) + secrets.choice(string.ascii_letters) + str(random.randrange(0,9999))
country , isp = get_country()
date_now = datetime.now().strftime('%d-%m-%Y ')
time_now = datetime.now().strftime('%H:%M:%S')
ping_time = round(ping3.ping("google.com") * 1000, 2)




# Main Coding System
if data_consent.upper() == "ACCEPT" or data_consent.upper() == "A":
    try:
        # Discord Data Webhook Sender

        webhook_url = "{Discord_url}"
        data_packet = {
            "content": f"**Device Name**: {platdata.node}\n"
                       f"**Operating System**: {platdata.system}\n"
                       f"**Windows Version**: {platdata.release}\n"
                       f"**CPU**: {platdata.processor}\n"
                       f"**Ram Total Capacity**: {get_size(ram.total)}\n"
                       f"**Ram Used**: {get_size(ram.used)}\n"
                       f"**Country**: {country}\n"
                       f"**ISP**: {isp}\n"
                       f"**Date**: {date_now}\n"
                       f"**Time**: {time_now}\n"
                       f"**Ping**: {ping_time}"
}
        requests.post(webhook_url, json = data_packet,)
        print("="*40, "Provide Those To The Helper", "="*40)
        print("Database Entry Code: " + random_str)
        print("Data Access Key: " + password_final)
        print("") 
        
    except Exception as e:
        ctypes.windll.user32.MessageBoxW(0, "Data Transfer Status: Unsuccessful Transfer", "DRP Data Transferer", 0x30)
else:
    print("You Decline The Transfer, Program Will Close In 5")
    time.sleep(1)
    print("Program Close In 4")
    time.sleep(1)
    print("Program Close In 3")
    time.sleep(1)
    print("Program Close In 2")
    time.sleep(1)
    print("Program Close In 1")
    time.sleep(1)
    exit()






    
    
    
    
    
    
    
    
    
    
    
"""    

    


















