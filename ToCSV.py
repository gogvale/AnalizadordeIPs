import xml.etree.ElementTree as ET
from itertools import zip_longest
import csv

XML= ET.parse('logs.xml')
Root= XML.getroot()
Result= Root.find('result')

def StatusCheck():
    XML= ET.parse('logs.xml')
    Root= XML.getroot()
    Result= Root.find('result')
    Status= Result.find('job')

    for job in Status.getiterator():
        if job.tag=='status':
            Stat= job.text
    return Stat

def ListInitialization():
    Src=[]
    Dst=[]
    Rule=[]
    Country=[]
    App=[]
    DeviceName=[]
    
    return Src, Dst, Rule, Country, App, DeviceName

def GetEvents():

    Events= Result.find('log')

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

def SaveToCSV():
    Inicdents=[Src, Dst, Country , App, Rule, DeviceName]
    FinishedData= zip_longest(*Inicdents, fillvalue='')
    with open('Logs.csv', 'w') as f:
        w=csv.writer(f)
        w.writerow(("Source", "Destination", "Country", "App", "Rule", "Device Name"))
        w.writerows(FinishedData)
