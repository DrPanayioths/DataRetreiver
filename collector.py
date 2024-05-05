import time
import platform
import random
import psutil
from supabase import create_client, Client
import ctypes

url: str = "Supabase URL"
key: str = "Supabase API Key"
supabase: Client = create_client(url, key)
print("(Computer) Data Sender Provided By DrPanayioths")
print("")

data_consent = input("By Writing Accept Or A You Accept To The Collection Of Your Computer Data And Transfer To DrPanayioths Database: ")
print("")

def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

random_number = random.randrange(0,9999)
platdata = platform.uname()
ram = psutil.virtual_memory()
random_str = str(random_number)

if data_consent.upper() == "ACCEPT" or data_consent.upper() == "A":
    try:
        count = supabase.table('helper_data') \
            .insert({"id": random_number, "OperatingSYS": platdata.system, "DeviceName": platdata.node, "WindowsVersion": platdata.release, "CPU_DATA": platdata.processor, "Ram_Total": get_size(ram.total), "Ram_Used": get_size(ram.used), }) \
            .execute()
        print("="*40, "Provide Code To The Helper", "="*40)
        print("Database Entry Code: " + random_str)
        print("") 
        ctypes.windll.user32.MessageBoxW(0, "Data Status: Succesful Transfer", "DRP Data Transferer", 1)
    except Exception as e:
        print("Error:", e)
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





