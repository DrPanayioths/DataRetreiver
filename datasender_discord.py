import time
import platform
import random
import psutil
from datetime import datetime
import ctypes
import os
import requests
import ping3
import WinTmp
import GPUtil
import sys
import math
import speedtest






os.system('color a')
print("="*83)
print("(Computer) Data Sender Provided By DrPanayioths       Supports: Windows 10/11, Linux")
print("="*83)

print("")
print("The Collection Of Your Computer Data And Post In The Discord Server Of The Supporter")
data_consent = input("By Writing CONSENT OR C You Consent To The Above: ")
print("")
print("Collecting Informations (May Take Some Time)")

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

platdata = platform.uname()
ram = psutil.virtual_memory()
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
            # Send data to Discord webhook
            webhook_url = "https://discord.com/api/webhooks/..."
            data_packet = {
    "embeds": [
        {
            "title": "System Details Collected (Consented by User)",
            "description": "Details collected about the device:",
            "color": 3066993,
            "fields": [
                {"name": "Device Name", "value": str(platdata.node), "inline": False},
                {"name": "RAM Total Capacity", "value": str(get_size(ram.total)), "inline": True},
                {"name": "RAM Used", "value": str(get_size(ram.used)), "inline": True},
                {"name": "Country", "value": str(country), "inline": False},
                {"name": "Operating System", "value": str(platdata.system), "inline": False},
                {"name": "Windows Version", "value": str(win_version), "inline": False},
                {"name": "CPU Information", "value": str(platdata.processor), "inline": False},
                {"name": "GPU Name", "value": str(GPU_Name), "inline": False},
                {"name": "CPU Temperature", "value": CPU_Tempature, "inline": True},
                {"name": "GPU Temperature", "value": GPU_Tempature, "inline": True},
                {"name": "ISP", "value": str(isp), "inline": False},
                {"name": "Date", "value": str(date_now), "inline": True},
                {"name": "Time", "value": str(time_now), "inline": True},
                {"name": "Ping", "value": str(ping_time), "inline": False},
                {"name": "Logged User", "value": str(logged_user), "inline": True},
                {"name": "Total Storage", "value": str(total_final), "inline": True},
                {"name": "Download Speed", "value": str(download_final) + " MB/s", "inline": False},
                {"name": "Upload Speed", "value": str(upload_final) + " MB/s", "inline": True}
            ],
            "footer": {
                "text": "| Tool Created By DrPanayioths |",
                "icon_url": "https://i.ibb.co/2WCw4Wx/DR-Logo-Straight.png",
            }
        }
    ]
}
            response = requests.post(webhook_url, json=data_packet)
        
    #   Send data to Discord webhook


            print("=" * 40, "Data Posted On The Discord Server Of The Supporter", "=" * 40)
            print("")

        except Exception as e:
            ctypes.windll.user32.MessageBoxW(0, "Transfer Status: Unsuccessful Transfer", "DRP Data Transferer", 0x30)
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
