import xml.etree.ElementTree as ET
from itertools import zip_longest
import csv


class toCSV():
    def __init__(self, file='logs.xml'):
        self.file = file
        self.ListInitialization()
        self.setup()
    
    def setup(self):
        self.XML = self.ParseFile(self.file)
        self.Root = self.XML.getroot()
        self.Result = self.Root.find('result')
        

    def ParseFile(self, file):
        return ET.parse(file)

    def StatusCheck(self):
        Status = self.Result.find('job')

        for job in Status.getiterator():
            if job.tag == 'status':
                Stat = job.text
        return Stat

    def ListInitialization(self):
        self.Src = []
        self.Dst = []
        self.Rule = []
        self.Country = []
        self.App = []
        self.DeviceName = []

        # return Src, Dst, Rule, Country, App, DeviceName

    def GetEvents(self):

        Events = self.Result.find('log')

        for event in Events.getiterator():
            if event.tag == 'src':
                self.Src.append(event.text)
            elif event.tag == 'dst':
                self.Dst.append(event.text)
            elif event.tag == 'rule':
                self.Rule.append(event.text)
            elif event.tag == "srcloc":
                Ctry = event.attrib
                self.Country.append(Ctry['code'])
            elif event.tag == 'app':
                self.App.append(event.text)
            elif event.tag == 'device_name':
                self.DeviceName.append(event.text)

    def SaveToCSV(self):
        Inicdents = [self.Src, self.Dst, self.Country,
                     self.App, self.Rule, self.DeviceName]
        FinishedData = zip_longest(*Inicdents, fillvalue='')
        with open('Logs.csv', 'w') as f:
            w = csv.writer(f)
            w.writerow(("Source", "Destination", "Country",
                        "App", "Rule", "Device Name"))
            w.writerows(FinishedData)
