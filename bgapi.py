import os
import datetime
import requests
from sloknum import *

# Getting Bhagavad Gita Chapter and Slok number based on current date
days,ch,sl = Slok_Num()
now = datetime.datetime.now()

# Cleaing Slok data
def Shudh(slok):
    return slok.replace("\n", " ").replace(" .", ".").replace("  ", " ")

# Authenticate to Bhagavad Gita API and getting sloks as json
def Slokm():
    try:
        auth = {'x-api-key' : os.environ["xapikey"]}
        response = requests.get(f"https://bhagavadgitaapi.in/slok/{ch}/{sl}", headers=auth)
        data = response.json()
        if now.hour in range(0, 2):
            return data["slok"]
        elif now.hour in range(2, 4):
            return Shudh(data["transliteration"])
        elif now.hour in range(4, 6):
            return Shudh(data["tej"]["ht"])
        elif now.hour in range(6, 8):
            return Shudh(data["siva"]["et"])
        elif now.hour in range(8, 10):
            return Shudh(data["purohit"]["et"])
        elif now.hour in range(10, 12):
            return Shudh(data["adi"]["et"])
        elif now.hour in range(12, 14):
            return Shudh(data["gambir"]["et"])
        elif now.hour in range(14, 17):
            return Shudh(data["rams"]["ht"])
        else:
            return("Bhagavad Gita API\n #GitaSlok #BhagavadGitaApi #iskcon #radhe #krishna #ptprashanttripathi")  
    except:
        print("Error during authentication")

#testing        
print(Slokm())