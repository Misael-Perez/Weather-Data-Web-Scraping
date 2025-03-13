import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

url="https://www.timeanddate.com/weather/usa/new-york"

r=requests.get(url)
html_doc =r.text
soup = BeautifulSoup(html_doc, "html.parser")
condition=[]
Timeofday=[]
temperature=[]

table= soup.find('table', class_="zebra tb-wt tc sep")
for tr in table.find_all("td",class_="smaller"):
    Old = tr.get_text()
    Old = Old.replace('\t', '')
    Old = Old.replace("\xa0", '')
    Old = Old.replace('.', '')
    condition.append(Old.replace('\n', ''))
    
thh=[]

for n in table.find_all('th'):
    Old = n.get_text()
    Old = Old.replace('\t', '')
    Old = Old.replace("\xa0", '')
    Old = Old.replace('.', '')
    thh.append(Old.replace('\n',''))


    
 #Getting Temperature
tdd=[]
for tr in table.find_all("td"):
    Old = tr.get_text()
    Old = Old.replace('\t', '')
    Old = Old.replace("\xa0", '')
    Old = Old.replace('.', '')
    tdd.append(Old.replace('\n', ''))
#take out empty spots
for n in range(4,11):
    Timeofday.append(thh[n]) 
    #modify temp for it's data
    temperature.append(tdd[n+3])
 
 
print(temperature)    


Weather_info={
    "Time of Day":Timeofday,
    "Temperature":temperature,
    "Condition":condition
}
data=pd.DataFrame(Weather_info)

data.to_csv("Weather_data.csv")

print(data)

