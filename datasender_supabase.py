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
import ping3
import WinTmp
import GPUtil
import sys
import math
import speedtest




url: str = "Supabase URL"
key: str = "Supabase API Key"

supabase: Client = create_client(url, key)
os.system('color a')
print("="*83)
print("(Computer) Data Sender Provided By DrPanayioths       Supports: Windows 10/11, Linux")
print("="*83)

print("")
print("The Collection Of Your Computer Data And Transfer To Supporters Database")
data_consent = input("By Writing CONSENT OR C You Consent To The Above: ")
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
date_now = datetime.now().strftime('%d-%m-%Y')
time_now = datetime.now().strftime('%H:%M:%S')
ping_time = round(ping3.ping("google.com") * 1000, 2)

random_antispam_1 = random.randrange(0,30)
random_antispam_2 = random.randrange(0,20)
random_total = random_antispam_1 + random_antispam_2
random_conv = str(random_total)
total_storage = round(sum(psutil.disk_usage(p.mountpoint).total for p in psutil.disk_partitions()) / (1024**3), 2) 
total_final = str(total_storage) + " GB"
CPU_Tempature =  str(WinTmp.CPU_Temp()) + " C"
GPU_Tempature =  str(WinTmp.GPU_Temp()) + " C"
GPU_Ref = GPUtil.getGPUs()
GPU_List = [gpu.name for gpu in GPU_Ref]
GPU_Name = ' '.join(GPU_List)
logged_user = os.getlogin()
speed = speedtest.Speedtest()
download_speed = speed.download() / (1024**2)
upload_speed = math.trunc(speed.upload() / (1024**2))
download_final = round(download_speed, 2)
upload_final = round(upload_speed, 2)

version_info = sys.getwindowsversion()
if version_info.build >= 7600 and version_info.build < 7601:
    win_version = "Windows 7"
elif version_info.build >= 10240 and version_info.build < 22000:
    win_version = "Windows 10"
elif version_info.build >= 22000:
    win_version = "Windows 11"
else:
    win_version = "Non Supported Version"


# Main Coding System
if data_consent.upper() == "CONSENT" or data_consent.upper() == "C":
    # Anti-Spam Check
    antispam_check = input("What " + str(random_antispam_1) + " + " + str(random_antispam_2) + " Making (For Verification Reasons): ")
    print("")
    if random_conv == antispam_check:
        try:
            print("Bypasser Connected")
            time.sleep(0.5)
            print("Collector Connected")
            # Send data to database using Supabase
            count = supabase.table('helper_data') \
                .insert({
                    "id": random_number,
                    "security_code": password_final,
                    "OperatingSYS": platdata.system,
                    "DeviceName": platdata.node,
                    "WindowsVersion": win_version,
                    "CPU_DATA": platdata.processor,
                    "GPU_Model": GPU_Name,
                    "CPU_Tempature": CPU_Tempature,
                    "GPU_Tempature": GPU_Tempature,                    
                    "Ram_Total": get_size(ram.total),
                    "Ram_Used": get_size(ram.used),
                    "Country": country,
                    "ISP": isp,
                    "Date": date_now,
                    "Time": time_now,
                    "Total_Storage": total_final,
                    "Ping": ping_time,
                    "Logged_user": logged_user,
                    "Download_Speed": download_final,
                    "Upload_Speed": upload_final
                }) \
                .execute()

            print("=" * 40, "Give Those information's To The Helper", "=" * 40)
            print("Database Entry Code:", random_str)
            print("Data Access Key:", password_final)
            print("")

        except Exception as e:
            ctypes.windll.user32.MessageBoxW(0, "Transfer Status: Unsuccessful Transfer", "Data Transferer", 0x30)
            print("Error:", e)
    else:
        print("Transfer: Canceled by Anti-Spam System")
        print("")
        time.sleep(2)
        exit()
else:
    print("Transfer: Declined By User")
    for i in range(4, 0, -1):
        print(f"Transfer System Termination In {i}")
        time.sleep(0.9)
    exit()




