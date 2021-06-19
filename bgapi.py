import os
import datetime
import requests
from sloknum import *

# Getting Bhagavad Gita Chapter and Slok number based on current date
days,ch,sl = Slok_Num()
now = datetime.datetime.now()
print (now)

# Cleaing Slok data
def Shudh(slok):
    return slok.replace("\n", " ").replace(" .", ".").replace("  ", " ")

# Adding Slok Tegs
def Teg():
    adhyay = ["KarmaYoga"]
    return(f"#BG{ch}_{sl} #{adhyay[ch-1]}\n")

# Authenticate to Bhagavad Gita API and getting sloks as json
# Returning specific slok or translation based on time        
def Slokm():
    try:
        auth = {'x-api-key' : os.environ["xapikey"]}
        response = requests.get(f"https://bhagavadgitaapi.in/slok/{ch}/{sl}", headers=auth)
        data = response.json()
        if now.hour in range(0,2):
            return Teg()+data["slok"]
        elif now.hour in range(2,4):
            return "#SwamiTejomayananda "+Shudh(data["tej"]["ht"])
        elif now.hour in range(4,6):
            return "#SwamiSivananda "+Shudh(data["siva"]["et"])
        elif now.hour in range(6,8):
            return "#ShriPurohitSwami "+Shudh(data["purohit"]["et"])
        elif now.hour in range(8,10):
            return "#SwamiRamsukhdas "+Shudh(data["rams"]["ht"])
        elif now.hour in range(10,12):
            return "#SwamiAdidevananda "+Shudh(data["adi"]["et"])
        elif now.hour in range(12,14):
            return "#SwamiGambirananda "+Shudh(data["gambir"]["et"])
        else:
            return("Bhagavad Gita API")   
    except:
        print("Error during authentication")

#testing        
#print(Slokm())
