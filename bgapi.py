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
    adhyay = ["VisadaYoga","SankhyaYoga","KarmaYoga","JnanaYoga","KarmaVairagyaYoga","AbhyasaYoga","ParamahamsaVijnanaYoga","AksaraParabrahmanYoga","RajaVidyaGuhyaYoga","VibhutiVistaraYoga","VisvarupaDarsanaYoga","BhaktiYoga","KsetraKsetrajnaVibhagaYoga","GunatrayaVibhagaYoga","PurusottamaYoga","DaivasuraSampadVibhagaYoga","SraddhatrayaVibhagaYoga","MoksaOpadesaYoga"]
    return(f"\n\n#BG{ch}_{sl} #{adhyay[ch-1]}")

# Authenticate to Bhagavad Gita API and getting sloks as json
# Returning specific slok or translation based on time        
def Slokm():
    try:
        response = requests.get(f"https://bhagavadgitaapi.in/slok/{ch}/{sl}")
        data = response.json()
        if now.hour in range(0,2):
            return data["slok"]+Teg()
        elif now.hour in range(2,4):
            return Shudh(data["tej"]["ht"])+" #SwamiTejomayananda"
        elif now.hour in range(4,6):
            return Shudh(data["siva"]["et"])+" #SwamiSivananda"
        elif now.hour in range(6,8):
            return Shudh(data["purohit"]["et"])+" #ShriPurohitSwami"
        elif now.hour in range(8,10):
            return Shudh(data["rams"]["ht"])+" #SwamiRamsukhdas"
        elif now.hour in range(10,12):
            return Shudh(data["adi"]["et"])+" #SwamiAdidevananda"
        elif now.hour in range(12,14):
            return Shudh(data["gambir"]["et"])+" #SwamiGambirananda"
        else:
            return("Bhagavad Gita API")   
    except:
        print("Error during Bgapi")

#testing        
#print(Slokm())
