from colorama import Fore


print('\033[1;34m')



print ("Initializing Covid-19 Tracker")
print ("----------------------------")
print ("\n")


import datetime

now = datetime.datetime.now()
print(now)
print ("\n")


from bs4 import BeautifulSoup as soup
import requests



name = input("What is your name?")

print ("Welcome "+name)




password = str(input("What is the password?"))


if password == "1234":
	print("User Authenticated")


elif password != "1234":
	print("Password Denied")
	exit()
print ("\n")



url = "https://www.worldometers.info/coronavirus/"
r = requests.get(url)
s = soup(r.text, "html.parser")
data = s.find_all("div", class_="maincounter-number")
status = s.find_all("div", class_="number-table-main")
active = s.find_all("span", class_="number-table")
per = s.find_all("strong")
country = s.find_all("td")
cou=[]

for a in country:
    cou.append(a.text)
print("Covid-19 Python Tracker")
print("Please Enter Country Name Using The First Letter As A Capital Letter:")
c=input()
if c=="":
    c="World"
b=cou.index(c)


print(cou[b].upper()+" Total Number Of Cases:"+cou[b+1]+"   New Number Of Cases:"+cou[b+2]+"   Total Number Of Deaths:"+cou[b+3]+"   New Number Of Deaths:"+cou[b+4]+" Number Of People Recovered:"+cou[b+5]+"   Active Number Of Cases:"+cou[b+6]+"   Serious Number Of Cases:"+cou[b+7]+"   cases/1Mpop:"+cou[b+8]+"   deaths/1Mpop:"+cou[b+9]+"   tests:"+cou[b+10]+"  tests/1Mpop:"+cou[b+11])


print("\nGlobal Results")
print("Total Number Of Cases: " + data[0].text.strip())
print("Total Number Of Deaths: " + data[1].text.strip())
print("Total Number Of Recovered: " + data[2].text.strip())
print("Active Number Of Cases: " + status[0].text.strip() + "\t\t--Mild: " + active[0].text.strip() + " (" + per[
    2].text.strip() + "%)\t\t--Critical: " + active[1].text.strip() + " (" + per[3].text.strip() + "%)")
print("Closed Cases: " + status[1].text.strip() + "\t\t--Discharged: " + active[2].text.strip() + " (" + per[
    4].text.strip() + "%)\t--Deaths: " + active[3].text.strip() + " (" + per[5].text.strip() + "%)")

print ("\n")

import time
time.sleep(2)

print(" The Data Source this Program Is From is: https://www.worldometers.info/coronavirus/")

print ("\n")
import time
time.sleep(2)

print("For More Information On Covid-19, Please Visit: https://www.nhs.uk/conditions/coronavirus-covid-19/")

import time
time.sleep(60)
