from datetime import date
import os

# Generat Bhagavad Gita Chapter and Slok number based on current date
# os.environ["startdate"] =
startdate = "2021,7,17"
def Slok_Num():
    yy,mm,dd = startdate.split(",")
    start = date(int(yy),int(mm),int(dd))
    today = date.today()
    days = (today-start).days
    print(start)
    
    #slokcounts=[47,72,43,42,29,47,30,28,34,42,55,20,35,27,20,24,28,78]
    Slok_Count_Till_Chap = [47,119,162,204,233,280,310,338,372,414,469,489,524,551,571,595,623,701]
    chap,slok = 0,0
    if 702 > days > 0 :
        for i in range(0,18): 
            if days <= Slok_Count_Till_Chap[i]:
                chap = i+1
                if i>0 : 
                    slok = days-Slok_Count_Till_Chap[i-1] 
                else :
                    slok = days
                break
        return (days,chap,slok)    
    else:
        return (days,0,0)

#testing th Slok_NUM function
#def Test():
#    for i in range(0,705): 
#        print(Slok_Num(i));
#Test()
#print(Slok_Num())
