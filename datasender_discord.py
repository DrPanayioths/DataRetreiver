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








os.system('color a')
print("="*83)
print("(Computer) Data Sender Provided By DrPanayioths       Supports: Windows 10/11, Linux")
print("="*83)

print("")
print("The Collection Of Your Computer Data And Post In The Discord Server Of The Supporter")
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

# Main Coding System
if data_consent.upper() == "CONSENT" or data_consent.upper() == "C":
    # Anti-Spam Check
    antispam_check = input("What " + str(random_antispam_1) + " + " + str(random_antispam_2) + " Making (For Verification Reasons): ")
    print("")
    if random_conv == antispam_check:
        try:
            #           Send data to Discord webhook
            webhook_url = "https://discord.com/api/webhooks/..."
            data_packet = {
            "content": f"**Device Name**: {platdata.node}\n"
                        f"**Ram Total Capacity**: {get_size(ram.total)}\n"
                        f"**Ram Used**: {get_size(ram.used)}\n"
                        f"**Country**: {country}\n"
                        f"**Operating System**: {platdata.system}\n"
                        f"**Device Name**: {platdata.node}\n"
                        f"**WindowsVersion**: {platdata.release}\n"
                        f"**CPU information's**: {platdata.processor}\n"
                        f"**GPU Name:**: {GPU_Name}\n"
                        f"**CPU_Tempature**: {CPU_Tempature}\n"
                        f"**GPU_Tempature**: {GPU_Tempature}\n" 
                        f"**ISP**: {isp}\n"
                        f"**Date**: {date_now}\n"
                        f"**Time**: {time_now}\n"
                        f"**Ping**: {ping_time}"  
            }
            requests.post(webhook_url, json=data_packet)
        
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
