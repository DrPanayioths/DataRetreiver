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
import requests

url: str = "Supabase URL"
key: str = "Supabase API Key"

supabase: Client = create_client(url, key)
os.system('color a')
print("="*80)
print("(Computer) Data Sender Provided By DrPanayioths")
print("Support's: Database / Discord")
print("="*80)

data_consent = input("By Writing Accept Or A You Accept To The Collection Of Your Computer Data And Transfer To The Database Of The Helper: ")
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





# Main Coding System
if data_consent.upper() == "ACCEPT" or data_consent.upper() == "A":
    try:
        # Database Sender
        count = supabase.table('helper_data') \
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
    "Time": time_now
})            .execute()
        print("="*40, "Provide Those To The Helper", "="*40)
        print("Database Entry Code: " + random_str)
        print("Data Access Key: " + password_final)
        print("") 
        
        # Discord Data Webhook Sender (Enable it By Removing the ''' and ''')
        '''
        webhook_url = "Replace With Your Webhook URL"
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
                       f"**Date**: {time_now}"
}
        requests.post(webhook_url, json = data_packet,)
        '''
        ctypes.windll.user32.MessageBoxW(0, "Data Transfer Status: Successful Transfer", "DRP Data Transferer", 0x40)
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





