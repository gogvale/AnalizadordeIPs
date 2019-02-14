import xml.etree.ElementTree as ET
from itertools import zip_longest
import csv

XML= ET.parse('logs.xml')
Root= XML.getroot()
Result= Root.find('result')
Events= Result.find('log')
Status= Result.find('job')

for job in Status.getiterator():
    if job.tag=='status':
        print(job.text)

Src=[]
Dst=[]
Rule=[]
Country=[]
App=[]
DeviceName=[]

for event in Events.getiterator():
    if event.tag=='src':
        Src.append(event.text)
    elif event.tag=='dst':
        Dst.append(event.text)
    elif event.tag=='rule':
        Rule.append(event.text)
    elif event.tag=="srcloc":
        Ctry= event.attrib
        Country.append(Ctry['code'])
    elif event.tag=='app':
        App.append(event.text)
    elif event.tag=='device_name':
        DeviceName.append(event.text)

Inicdents=[Src, Dst, Rule, Country, App, DeviceName]
FinishedData= zip_longest(*Inicdents, fillvalue='')

with open('Logs.csv', 'w') as f:
    w=csv.writer(f)
    w.writerow(("SOURCE", "DESTINATION", "RULE", "COUNTRY", "APP", "DEVICE NAME"))
    w.writerows(FinishedData)
